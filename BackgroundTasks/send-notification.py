# Create a Task function in FastAPI 

# It can be async def or normal def function. FastAPI will handle correctly based on return type 

# The task function will write to a file (showing end user sending an email as a notification)

# As the write operation doesn't use async and await, the normal function with def: can be used 

from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

# defining the function for sending email and showing user sending email as notification 

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    # .add_task() receives the arguments 
    # a task function is to be run in the background (write_notification)
    # any sequence of arguments which should be passed to the task function in order (email)
    # Any keyword arguments should be passed to the task function 
    background_tasks.add_task(write_notification, email, message="some background tasks notification")
    return {"message": "Notification send in the background of FastAPI app"}        