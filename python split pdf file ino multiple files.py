import PyPDF2
from PyPDF2 import PdfWriter, PdfReader

pdf = PyPDF2.PdfReader("file.pdf")
NumPages = len(pdf.pages)

for i in range(0, NumPages):
    
    # get names
    PageObj = pdf.pages[i]
    Text = PageObj.extract_text() 
    splitText= Text.split("\n")
    name=splitText[0]+splitText[1]
    
    #print(splitText[0]+splitText[1])
    
    # save pdf files
    output = PdfWriter()
    output.add_page(pdf.pages[i])
    with open("%s.pdf" % name, "wb") as outputStream:
        output.write(outputStream)
    
    
    
