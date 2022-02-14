def resolucionAdapter(data):
    print("[INFO] Adaptando archivo de resolucion")
    dictAdapter = {}
    dictAdapter["###RESOLUCION###"] = data["resolucion"]
    dictAdapter["###FECHA_RESOLUCION###"] = data["fechaResolucion"]
    dictAdapter["###EXPEDIENTE###"] = data["expediente"]
    dictAdapter["###NAME_PORTADA###"] = data["nombres"]
    dictAdapter["###TIPO_DOCUMENTO###"] = data["tipoID"]
    dictAdapter["###NUMERO_IDENTIDAD###"] = data["numID"]
    dictAdapter["###NACIONALIDAD###"] = data["nacionalidad"]
    dictAdapter["###INFORME_CASO###"] = data["informeCaso"]
    dictAdapter["###AUTO_APERTURA###"] = data["autoApertura"]
    dictAdapter["###FECHA###"] = data["fecha"]
    dictAdapter["###AUTO_FORMULACION###"] = data["autoFormulacion"]
    dictAdapter["###VALOR_MULTA###"] = data["valorMulta"]
    return dictAdapter
