meses = {
    "Enero": "01",
    "Febrero": "02",
    "Marzo": "03",
    "Abril": "04",
    "Mayo": "05",
    "Junio": "06",
    "Julio": "07",
    "Agosto": "08",
    "Septiembre": "09",
    "Octubre": "10",
    "Noviembre": "11",
    "Diciembre": "12"
}


def convertir_fecha(fecha):
    if "/" in fecha:
        mes, dia, año = fecha.split("/")
        return f"{año.zfill(4)}-{mes.zfill(2)}-{dia.zfill(2)}"
    
    else:
        fecha = fecha.replace(",", "")  # Eliminar la coma
        mes_nombre, dia, año = fecha.split(" ")
        mes = meses[mes_nombre]
        return f"{año.zfill(4)}-{mes}-{dia.zfill(2)}"

fecha_entrada = input("Ingrese una fecha (formato MM/DD/AAAA o Mes Día, AAAA): ")
print("Fecha en formato AAAA-MM-DD:", convertir_fecha(fecha_entrada))
