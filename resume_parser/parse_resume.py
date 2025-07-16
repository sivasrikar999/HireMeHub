from pdfminer.high_level import extract_text

def parse_resume(pdf_path):
    text = extract_text(pdf_path)
    return {
        "raw_text": text[:500] + "..."  # Just a preview of the resume
    }
