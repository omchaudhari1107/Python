from pypdf import PdfWriter

merger = PdfWriter()
pdf1 = open('file1.pdf', 'rb')
pdf2 = open('file2.pdf', 'rb')
pdf3 = open('file3.pdf', 'rb')
for pdf in [pdf1, pdf2, pdf3]:
    merger.append(pdf)

merger.write("pdfs/merged-pdf.pdf")
merger.close()
