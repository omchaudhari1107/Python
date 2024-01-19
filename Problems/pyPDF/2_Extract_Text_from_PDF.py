from pypdf import PdfReader

reader = PdfReader('file.pdf')
page = reader.pages[0]
print(page.extract_text(0))  # fetch text only
