from docx import Document
import json
import re
import os

def main(template_file, template_data, folder_name):
    with open(template_data) as f:
        data = json.load(f)
    document = Document(template_file)
    paragraphs = document.paragraphs
    for paragraph in paragraphs:
        for key in data:
            match = re.search(key, paragraph.text)
            if match:
                paragraph.text = paragraph.text.replace(key, data[key])
    document.save(".\\outputs\\" + folder_name + "\\" + "archivo.docx")

if __name__ == "__main__":
    ## debe tener un archivo.docx, la extension es importante
    ## y debe tener un archivo data.json que es como los datos que van
    
    folder_name = "portada"
    template_folder = os.getcwd() + "\\templates\\" + folder_name
    template_file = template_folder + "\\archivo.docx"
    template_data = template_folder + "\\data.json"

    main(template_file, template_data, folder_name)