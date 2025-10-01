from SemesterMapper.SemLinkedList import SemLinkedList

from Constants import SEASONS
from Constants import TEST_CREDITS
from Constants import TRANSFER_CREDITS
from Constants import TRANSCRIPT_BEGINNING
from Constants import TRANSCRIPT_END

def get_sem_mapping(pdf_pages_list):

    sm_ll = SemLinkedList()
    parse_reg_undergrad = False
    
    for index, value in enumerate(pdf_pages_list):

        if value == TEST_CREDITS:
            sm_ll.add((TEST_CREDITS, index))
        elif value == TRANSFER_CREDITS:
            sm_ll.add((TRANSFER_CREDITS, index))
        
        elif value.startswith(TRANSCRIPT_BEGINNING):
            parse_reg_undergrad = True
        elif value.startswith(TRANSCRIPT_END):
            sm_ll.add((TRANSCRIPT_END, index))
        
        elif parse_reg_undergrad:
            for semester in SEASONS:
                if value.startswith(semester):
                    semester_info = value[len(semester):].strip()
                    semester_label = f"{semester} {semester_info}"
                    sm_ll.add((semester_label, index))
                    break
    return sm_ll