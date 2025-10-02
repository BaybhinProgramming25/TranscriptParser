import pymupdf
import requests 

from SemesterMapper.GetMapping import get_sem_mapping
from Apps.ParserService.ContentMapper.GetCourses import get_content_from_each_sem

if __name__ == "__main__":
    doc = pymupdf.open("../../PDFs/Test1.pdf")

    pdf_pages_list = []
    for page in doc:
        text = page.get_text("text").strip("").split('\n')
        pdf_pages_list.extend(text)

    # Call sememster mapping function
    sm_ll = get_sem_mapping(pdf_pages_list)

    # All semester data 
    sem_data = get_content_from_each_sem(sm_ll, pdf_pages_list)

    # Now we send this data to the backend 
    response = requests.post('http://localhost:3000/studentdata', json=sem_data)
    print(response.json())

        
      
