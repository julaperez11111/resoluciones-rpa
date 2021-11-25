import json
from document_object import document_object
from fill_template import fill_template
from dataAdapter import dataAdapter
import argparse

# template_data es un string en formato json que debe ser parseado
def main(template_file, template_data):
    # TODO: Validacion de los datos
    document = document_object(template_file)
    json_template_data = template_data.replace("'", "\"")
    data = json.loads(json_template_data)
    dictPortada = dataAdapter(data)
    fill_template(document, dictPortada)

if __name__ == "__main__":
    ## debe tener un archivo.docx, la extension es importante
    ## y debe tener un archivo data.json que es como los datos que van
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('-t', "--template-file", type=str, dest="template_file",
                        help='template_file')
    parser.add_argument('-d', "--data", type=str, dest="data",
                        help='data que sera procesada')
    
    args = parser.parse_args()
    ## folder_name es args.template_folder = "portada"
    ## args.data_file = "data.json"
    ## args.file_name = "archivo.docx"
    template_file = args.template_file
    # template_folder = os.getcwd() + "\\templates\\" + "portada"
    ## template_file = template_folder + "\\" + args.file_name
    template_data = args.data

    main(template_file, template_data)