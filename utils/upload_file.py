from ironpdf import *
from docx2pdf import convert
import os

base_dir=os.getcwd()

def pdf_to_jpg(filename):
    pdf = PdfDocument.FromFile(filename)
    file_name = os.path.basename(filename)
    file_name = file_name.split(".")[0]
    os.chdir(base_dir)
    pdf.RasterizeToImageFiles(f"image/{file_name}/*.jpg", DPI=96)

    return


def docx_pdf_jpg(filename):
    file_name = os.path.basename(filename)
    file_name = file_name.split(".")[0]
    # print('-----------------------------------')
    word_path=r"D:\architecture_description\word_pdf"
    # os.chdir("D:\azure_arch\word_pdf")
    os.chdir(word_path)
    
    
    # print('-----------------------------------')
    
    path = r"D:\architecture_description\word_pdf"
    
    output = os.getcwd() + f"/{file_name}.pdf"
    output = os.path.join(path, output)

    convert(filename, output)

    

    return output
