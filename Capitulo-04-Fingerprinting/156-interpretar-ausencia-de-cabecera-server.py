# Diapositiva 156: Interpretacion de banners - vision general
# Muestra que la ausencia de una cabecera tambien es informacion: si no viene "Server",
# probablemente alguien la oculto a proposito (administrador consciente de la seguridad).

# La ausencia de 'Server' tambien se interpreta
def interpretar_server(cabeceras: dict) -> str:  # recibe el diccionario de cabeceras recibidas
    valor = cabeceras.get("Server")  # .get devuelve None si la cabecera "Server" no esta
    if valor is None:  # si no vino la cabecera
        return "Sin cabecera Server: probablemente ocultada a proposito (admin consciente)"  # la ausencia informa
    return f"Servidor declarado: {valor}"  # si vino, mostramos su valor


print(interpretar_server({"Content-Type": "text/html"}))  # prueba con cabeceras que NO incluyen "Server"
# Sin cabecera Server: probablemente ocultada a proposito (admin consciente)
