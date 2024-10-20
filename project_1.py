import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors


pdf_path = "D:\python\python_Project\Text-to-pdf-converter\text_to_pdf.pdfpy"

directory = os.path.dirname(pdf_path)
if not os.path.exists(directory):
    os.makedirs(directory)
    
c = canvas.Canvas(pdf_path, pagesize=letter)
c.setFont("Helvetica-Bold", 16)
c.setFillColor(colors.darkblue)
c.drawString(100, 750, "Hello, this is a text-to-PDF converter example!")
c.save()

print(f"PDF saved successfully at {pdf_path}")
