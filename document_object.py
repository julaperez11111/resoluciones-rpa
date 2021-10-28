from docx import Document

## document_object es una funcion que recibe la dirección de un archivo,
## y retorna un objecto documento de python-docx
def document_object(filename):
    return Document(filename)
