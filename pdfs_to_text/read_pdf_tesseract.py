import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

PDFS = "pdfs/a.pdf"
# convert to image using resolution 600 dpi
pages = convert_from_path(PDFS, 600)

# extract text
text_data = ''
for page in pages:
    text = pytesseract.image_to_string(page)
    text_data += text + '\n'
print(text_data)

# remove , . _ - from text_data
text_data = text_data.replace(
    ',', '').replace('_', '').replace('-', '').replace(
        ']', '').replace('[', '').replace(':', '')

# write text_data to a file
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text_data)
