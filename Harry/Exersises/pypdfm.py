# merge pdf files using pypdf library
from pypdf import PdfReader, PdfWriter

reader = PdfReader('E:/Documents/frankenstein.pdf')
page = reader.pages[0]
print(page.extract_text())

merger = PdfWriter()

for pdf in ['E:/Documents/frankenstein.pdf', "E:/Documents/07. Reaper's Gale.pdf"]:
    merger.append(pdf)

merger.write("E:/Documents/merged-pdf.pdf")
merger.close()
