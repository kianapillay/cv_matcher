import pdfplumber

def extract_text_from_pdf(uploaded_file):

    text = ""

    # Open PDF properly (better text reconstruction)
    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    # CLEANING (VERY IMPORTANT)
    text = text.lower()
    text = text.replace("\n", " ")
    text = " ".join(text.split())

    return text