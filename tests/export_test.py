import scribus
import sys

def export_pdf():
    scribus.openDoc("/home/runner/test.sla")
    
    if not scribus.haveDoc():
        print("Still no document open")
        sys.exit(1)

    pdf = scribus.PDFfile()
    pdf.file = "/home/runner/output_test.pdf"
    pdf.version = 4
    pdf.useDocBleeds = True
    pdf.compress = True
    pdf.save()
    print("PDF exported successfully")

export_pdf()
