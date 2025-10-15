import pymupdf
import requests

from SemesterMapper.GetMapping import get_sem_mapping
from ContentMapper.GetCourses import get_content_from_each_sem

from fastapi import APIRouter, File, UploadFile 

router = APIRouter()

@router.post("/parse")
async def parse(file: UploadFile = File(...)):

    pdf_bytes = await file.read()
    doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")

    pdf_pages_list = []
    for page in doc:
        text = page.get_text("text").strip("").split('\n')
        pdf_pages_list.extend(text)

    sm_ll = get_sem_mapping(pdf_pages_list)

    sem_data = get_content_from_each_sem(sm_ll, pdf_pages_list)

    requests.post(
        url='http://127.0.0.1:8001/setup-db',
        json=sem_data,
        timeout=10
    )
    
