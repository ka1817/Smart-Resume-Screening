from fastapi import FastAPI, UploadFile, Form, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import tempfile
import os

from src.resume_parser import extract_text_from_pdf
from src.screening import screen_candidate

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/screen")
async def screen_resume(
    request: Request,
    resume: UploadFile,
    job_description: str = Form(...)
):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        content = await resume.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        resume_text = extract_text_from_pdf(tmp_path)
    finally:
        os.remove(tmp_path)

    result = screen_candidate(resume_text, job_description)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
    })
