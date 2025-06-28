import os 
from src.resume_parser import extract_text_from_pdf

def test_extract_text_from_sample_pdf():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    sample_pdf_path = os.path.join(base_dir, "sample_resume.pdf")

    text = extract_text_from_pdf(sample_pdf_path)

    assert isinstance(text, str), "Output should be a string"
    assert len(text.strip()) > 0, "Extracted text should not be empty"
