# Diapositiva 140: Cabeceras HTTP para fingerprinting
# Muestra como deducir la tecnologia del backend por el nombre de la cookie de sesion
# (PHPSESSID -> PHP, JSESSIONID -> Java, ASP.NET_SessionId -> .NET).

# Deducir la plataforma por el nombre de la cookie de sesion
def plataforma_por_cookie(set_cookie: str) -> str:  # recibe el texto de la cabecera Set-Cookie
    pistas = {  # diccionario: nombre de cookie -> tecnologia asociada
        "PHPSESSID": "PHP",
        "JSESSIONID": "Java (JSP/servlets)",
        "ASP.NET_SessionId": ".NET",
    }
    for nombre, tecnologia in pistas.items():  # recorre cada pista conocida
        if nombre in set_cookie:  # si el nombre de la cookie aparece en el texto recibido
            return tecnologia  # devuelve la tecnologia correspondiente y termina
    return "desconocida"  # si no coincide ninguna, devuelve "desconocida"


print(plataforma_por_cookie("Set-Cookie: JSESSIONID=ABC123; Path=/"))  # prueba con una cookie de Java
# Salida: Java (JSP/servlets)
