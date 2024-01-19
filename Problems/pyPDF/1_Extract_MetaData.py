from pypdf import PdfReader

reader = PdfReader("file.pdf")
meta = reader.metadata
print(meta)
