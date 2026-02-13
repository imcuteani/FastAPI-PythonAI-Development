import os
import hvac
import motor.motor_asyncio

# Get Vault details from environment
vault_addr = os.getenv("VAULT_ADDR")
role_id = os.getenv("VAULT_ROLE_ID")
secret_id = os.getenv("VAULT_SECRET_ID")

if not all([vault_addr, role_id, secret_id]):
    raise EnvironmentError("Missing one or more Vault environment variables (VAULT_ADDR, VAULT_ROLE_ID, VAULT_SECRET_ID)")

# Connect to Vault and login with AppRole
try:
    vault_client = hvac.Client(url=vault_addr)
    login_response = vault_client.auth.approle.login(role_id=role_id, secret_id=secret_id)
    vault_client.token = login_response['auth']['client_token']
except Exception as e:
    raise RuntimeError(f"Vault login failed: {e}")

# Read MongoDB URI from Vault
try:
    read_response = vault_client.secrets.kv.v2.read_secret_version(path="student01")
    MONGO_URI = read_response["data"]["data"]["MONGO_URI"]
except Exception as e:
    raise RuntimeError(f"Error reading MongoDB URI from Vault: {e}")

# Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client["student_project_tracker"]
student_collection = database.get_collection("students")
