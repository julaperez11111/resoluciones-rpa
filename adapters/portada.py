def portadaAdapter(data):
    dictAdapter = {}
    dictAdapter["###NAME_PORTADA###"] = data["nombres"]
    dictAdapter["###FECHA###"] = data["fecha"]
    dictAdapter["###NACIONALIDAD###"] = data["nacionalidad"]
    dictAdapter["###NUMERO-UNICO###"] = data["numUnico"]
    return dictAdapter
