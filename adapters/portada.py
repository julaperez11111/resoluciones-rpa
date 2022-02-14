def portadaAdapter(data):
    print("[INFO] Adaptando archivo de portada")
    dictAdapter = {}
    dictAdapter["###NAME_PORTADA###"] = data["nombres"]
    dictAdapter["###FECHA###"] = data["fecha"]
    dictAdapter["###NACIONALIDAD###"] = data["nacionalidad"]
    dictAdapter["###NUMERO_UNICO###"] = data["numUnico"]
    return dictAdapter
