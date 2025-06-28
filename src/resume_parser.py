import fitz  
import os
def extract_text_from_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(__file__))  
    resume_path = os.path.join(base_dir, "sample_resume.pdf")

    if os.path.exists(resume_path):
        parsed_text = extract_text_from_pdf(resume_path)
        print("===== RESUME TEXT STARTs =====")
        print(parsed_text)
        print("===== RESUME TEXT END =====")
    else:
        print(f"File not found: {resume_path}")
    
