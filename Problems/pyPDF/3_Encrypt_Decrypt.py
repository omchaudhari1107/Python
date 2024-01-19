from pypdf import PdfReader, PdfWriter

reader = PdfReader("file.pdf")
writer = PdfWriter()
print(reader.pages)
# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add a password to the new PDF
writer.encrypt("my-secret-password")

# Save the new PDF to a file
with open("encrypted-pdf.pdf", "wb") as f:
    writer.write(f)
