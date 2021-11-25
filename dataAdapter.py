def dataAdapter(data):
    dictAdapter = {}
    dictAdapter["###NAME_PORTADA###"] = data["nombres"]
    dictAdapter["###NACIONALIDAD###"] = data["nacionalidad"]
    dictAdapter["###DOCUMENTO_IDENTIDAD###"] = data["he"]
    dictAdapter["###NUMERO_IDENTIDAD###"] = data["autoApertura"]
    dictAdapter["###FECHA###"] = data["fecha"]
    return dictAdapter