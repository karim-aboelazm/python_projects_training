# PyPDF2 --> pip install PyPDF2
import PyPDF2

def get_text_from_pdf(pdf_path):
    with open(pdf_path,'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        text = ''
        for page in range(2):
            text += pdf.pages[page].extract_text()
        return text

print(get_text_from_pdf("new.pdf"))