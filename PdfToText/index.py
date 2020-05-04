import PyPDF2

pdfobj = open('path_to_pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdfobj)
# assing page no. at getPage(0)

pageobj = pdf_reader.getPage(0)
print(pageobj.extractText())
