import json
import os
from document_object import document_object
from fill_template import fill_template
import argparse

def main(template_file, template_data, folder_name):
    with open(template_data, encoding='utf-8') as f:
        data = json.load(f)
    document = document_object(template_file)
    fill_template(document, data, folder_name)

if __name__ == "__main__":
    ## debe tener un archivo.docx, la extension es importante
    ## y debe tener un archivo data.json que es como los datos que van
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('-t', "--template-folder", type=str, dest="template_folder",
                        help='template_folder')
    parser.add_argument('-d', "--data-file", type=str, dest="data_file",
                        help='data_file')
    parser.add_argument('-f', "--file-name", type=str, dest="file_name",
                        help='file_name')
    
    args = parser.parse_args()
    ## folder_name es args.template_folder = "portada"
    ## args.data_file = "data.json"
    ## args.file_name = "archivo.docx"
    folder_name = args.template_folder
    template_folder = os.getcwd() + "\\templates\\" + folder_name
    template_file = template_folder + "\\" + args.file_name
    template_data = template_folder + "\\" + args.data_file

    main(template_file, template_data, folder_name)