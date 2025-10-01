import pymupdf

from SemesterMapper.GetMapping import get_sem_mapping
from ContentMapper.GetContent import get_content_from_each_sem

if __name__ == "__main__":
    doc = pymupdf.open("../../PDFs/Test1.pdf")

    pdf_pages_list = []
    for page in doc:
        text = page.get_text("text").strip("").split('\n')
        pdf_pages_list.extend(text)

    # Call sememster mapping function
    sm_ll = get_sem_mapping(pdf_pages_list)

    # With linked list, we then parse the data
    get_content_from_each_sem(sm_ll, pdf_pages_list)

        
      
