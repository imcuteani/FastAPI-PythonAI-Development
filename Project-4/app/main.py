from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.crud import create_student, get_student_progress, update_student_progress, count_students

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    total = await count_students()
    return templates.TemplateResponse("index.html", {"request": request, "total": total})

@app.get("/register", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register_submit(request: Request, name: str = Form(...)):
    student = await create_student(name)
    return templates.TemplateResponse("register.html", {"request": request, "message": f"Welcome, {student.name}!"})

@app.get("/progress", response_class=HTMLResponse)
async def progress_form(request: Request):
    return templates.TemplateResponse("progress.html", {"request": request})

@app.post("/progress", response_class=HTMLResponse)
async def progress_submit(request: Request, name: str = Form(...)):
    student = await get_student_progress(name)
    progress = []

    if student and  "progress" in student:
       for week, status in student["progress"].items():
          progress.append({"week": week, "status": status})
    return templates.TemplateResponse("progress.html", {"request": request, "progress": progress, "name": name})

@app.get("/update", response_class=HTMLResponse)
async def update_form(request: Request):
    return templates.TemplateResponse("update.html", {"request": request})

@app.post("/update", response_class=HTMLResponse)
async def update_submit(
    request: Request,
    name: str = Form(...),
    week: str = Form(...),
    status: str = Form(...)
):
    await update_student_progress(name, week, status)
    return templates.TemplateResponse("update.html", {"request": request, "message": "Progress updated successfully!"})
