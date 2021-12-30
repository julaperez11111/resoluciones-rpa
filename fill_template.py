import re

# carpeta de destino para los archivos generados
target_destination = "C:\\desarrollo\\rpa_resoluciones\\outputs\\"

## fill_template.py es una función que recibe un objecto de documento
## de python-docx, y un diccionario y en su proceso reemplaza los valores
## del diccionario en el documento.
## Al final entrega los documentos con los datos del diccionario
def fill_template(document, data, file_name):
    paragraphs = document.paragraphs
    for paragraph in paragraphs:
        for key in data:
            match = re.search(key, paragraph.text)
            if match:
                ## paragraph.text = paragraph.text.replace(key, data[key])
                for element in paragraph.runs:
                    element.text = element.text.replace(key, data[key])
    document.save(target_destination + file_name)