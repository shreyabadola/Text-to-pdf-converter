from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

c = canvas.Canvas("text_to_pdf.pdf", pagesize=letter)
c.setFont("Helvetica-Bold", 16)  
c.setFillColor(colors.darkblue)
c.drawString(100, 750, "Hello, this is a text-to-PDF converter example!")
c.save()
