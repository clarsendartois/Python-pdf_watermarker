# Use your Terminal, if you are on
# Windows type: python pdf_watermarker.py
import PyPDF2

template = PyPDF2.PdfReader(open("model.pdf", "rb"))
watermark = PyPDF2.PdfReader(open("watermark.pdf", "rb"))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open("watermarked_output.pdf", "wb") as file:
        output.write(file)
