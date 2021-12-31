import json
import argparse
import time
from document_object import document_object
from fill_template import fill_template
from adapters import portada, formulacion, apertura, resolucion

# template_data es un string en formato json que debe ser parseado


def main(template_data):
    # TODO: Validacion de los datos
    portadaDoc = document_object(
        "C:\\desarrollo\\rpa_resoluciones\\templates\\PORTADA.docx")
    formulacionDoc = document_object(
        "C:\\desarrollo\\rpa_resoluciones\\templates\\FORMULACION.docx")
    aperturaDoc = document_object(
        "C:\\desarrollo\\rpa_resoluciones\\templates\\APERTURA.docx")
    resolucionDoc = document_object(
        "C:\\desarrollo\\rpa_resoluciones\\templates\\RESOLUCION.docx")
    json_template_data = template_data.replace("'", "\"")
    data = json.loads(json_template_data)

    nowTime = str(int(time.time()))
    fill_template(portadaDoc, portada.portadaAdapter(
        data), "PORTADA_" + nowTime + "_" + data["numID"] + ".docx")
    fill_template(formulacionDoc, formulacion.formulacionAdapter(
        data), "FORMULACION_" + nowTime + "_" + data["numID"] + ".docx")
    fill_template(aperturaDoc, apertura.aperturaAdapter(
        data), "APERTURA_" + nowTime + "_" + data["numID"] + ".docx")
    fill_template(resolucionDoc, resolucion.resolucionAdapter(
        data), "RESOLUCION_" + nowTime + "_" + data["numID"] + ".docx")


if __name__ == "__main__":
    # debe tener un archivo.docx, la extension es importante
    # y debe tener un archivo data.json que es como los datos que van
    parser = argparse.ArgumentParser(description='Description.')
    parser.add_argument('-d', "--data", type=str, dest="data",
                        help='data que sera procesada')

    args = parser.parse_args()
    # template_folder = os.getcwd() + "\\templates\\" + "portada"
    ## template_file = template_folder + "\\" + args.file_name
    template_data = args.data

    main(template_data)
