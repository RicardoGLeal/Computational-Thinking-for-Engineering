def verifyCurp(curp):
    if len(curp) != 18:
        return "ERROR"
    else:
        estados = {"AS":"Aguascalientes","BC":"Baja California","BS":"Baja California Sur","CC":"Campeche","CS":"Chiapas","CH":"Chihuahua","CL":"Coahuila","CM":"Colima","DF":"Distrito Federal","DG":"DURANGO","GT":"GUANAJUATO","GR":"GUERRERO","HG":"HILDAGO","JC":"JALISCO","MC":"MEXICO","MN":"MICHOACAN","MS":"MORELOS","NT":"NAYARIT","NL":"NUEVO LEON", "OC":"OAXACA","PL":"PUEBLA","QT":"QUERETARO","QR":"QUINTANA ROO","SP":"SAN LUIS POTOSI","SL":"SINALOA","SR":"SONORA","TC":"TABASCO","TL":"TLAXCALA","TS":"TAMAULIPAS","VZ":"VERACRUZ","YN":"YUCATAN","ZS":"ZACATECAS", "NE":"NACIDO EN EL EXTRANJERO"}
        if curp[11:13] in estados:
            return estados[curp[11:13]].upper()
        else:
            return "ERROR"
        
curp = input()
print(verifyCurp(curp))