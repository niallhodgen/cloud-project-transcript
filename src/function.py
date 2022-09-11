from fpdf import FPDF
from flask import make_response



def createPDF(arr):

    pdf = FPDF()
    pdf.add_page()

    # Convert int to String for use in FPDF
    for values in arr:
        arr[values] = str(arr[values])

    # Logo
    logo = 'https://static.wixstatic.com/media/6d341b_ea9f36014d9c41e9942b516714a1d37c~mv2.png/v1/fill/w_420,h_236,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/QUB-EEECS-LOGO-PNG.png'
    pdf.image(logo, x=70, y=None, w=80, h=40)
    # Set font
    pdf.set_font('Courier', 'B', 15)

    # Title
    pdf.cell(200, 10, txt="Unofficial Transcript",
             ln=2, align='C')
    # Line break
    pdf.ln(20)

    # add another cell
    pdf.cell(200, 10, txt="MSc Software Development",
             ln=2, align='C')

    # add name
    pdf.cell(200, 10, txt=arr.get("Student Name"),
             ln=2, align='C')

    # add student number
    pdf.cell(200, 10, txt=arr.get("Student Number"),
             ln=2, align='C')

    # add spacing
    pdf.cell(200, 10, ln=2, align='C')

    pdf.set_font('Courier', 'B', 12)

    # Iterate through dictionary
    for x, y in arr.items():
        if (y != arr['Student Number'] and y != arr['Student Name']):
            # save value
            module = x, y
            # convert to plain string via json
            module = str(module)
            # Remove brackets, etc.
            module = module.replace("(", "")
            module = module.replace(")", "")
            module = module.replace(",", ": ")
            module = module.replace("'", "")
            # print to page
            pdf.cell(200, 10, txt=module,
                     ln=2, align='C')

    # save the pdf with student number in name
    fileName = arr['Student Number'] + "_transcript.pdf"
    # create response headers for PDF content and encode
    
    response = make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers.set('Content-Disposition',
                         'attachment', filename=fileName)
    response.headers.set('Content-Type', 'application/pdf')
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Expose-Headers"] = "*"
    
    return response
