import re
import create_file_name

# carpeta de destino para los archivos generados
target_destination = "C:\\Users\\EMIMED\\desarrollo\\rpa_resoluciones\\outputs\\portada\\"

## fill_template.py es una función que recibe un objecto de documento
## de python-docx, y un diccionario y en su proceso reemplaza los valores
## del diccionario en el documento.
## Al final entrega los documentos con los datos del diccionario
def fill_template(document, data):
    paragraphs = document.paragraphs
    for paragraph in paragraphs:
        for key in data:
            match = re.search(key, paragraph.text)
            if match:
                ## paragraph.text = paragraph.text.replace(key, data[key])
                for element in paragraph.runs:
                    element.text = element.text.replace(key, data[key])
    file_name = create_file_name.create_file_name("")
    document.save(target_destination + file_name)