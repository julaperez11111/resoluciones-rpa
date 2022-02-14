def formulacionAdapter(data):
    print("[INFO] Adaptando archivo de formulacion")
    dictAdapter = {}
    dictAdapter["###FECHA###"] = data["fecha"]
    dictAdapter["###AUTO_APERTURA###"] = data["autoApertura"]
    dictAdapter["###EXPEDIENTE###"] = data["expediente"]
    dictAdapter["###NAME_PORTADA###"] = data["nombres"]
    dictAdapter["###TIPO_DOCUMENTO###"] = data["tipoID"]
    dictAdapter["###NUMERO_IDENTIDAD###"] = data["numID"]
    dictAdapter["###NACIONALIDAD###"] = data["nacionalidad"]
    dictAdapter["###INFORME_CASO###"] = data["informeCaso"]
    return dictAdapter
