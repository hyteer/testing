from reportlab.pdfgen import canvas

c = canvas.Canvas("E:/Temp/first.pdf")
def hello(c):
    c.drawString(100,100,"First PDF")
    c = canvas.Canvas("first.pdf")


c.drawString(100,750,"Welcome to Reportlab!")
c.save()

'''
hello(c)
c.showPage()
c.save()
'''


