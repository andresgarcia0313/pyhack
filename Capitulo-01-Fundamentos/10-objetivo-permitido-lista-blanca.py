# Diapositiva 10: Capitulo 1, Fundamentos de Python para hacking
# Muestra una lista blanca: el curso solo trabaja contra destinos autorizados
# y una funcion que confirma si un destino esta permitido.

# "set" (conjunto) con los unicos destinos autorizados; las llaves {} definen el conjunto.
DESTINOS_AUTORIZADOS = {"127.0.0.1", "localhost", "scanme.nmap.org"}


# "def" define una funcion; recibe "destino" (texto, por eso ": str") y promete devolver un bool (-> bool).
def esta_autorizado(destino: str) -> bool:
    """Devuelve True solo si el destino esta en la lista blanca del curso."""
    # ".lower()" pasa el texto a minusculas; "in" pregunta si esta dentro del conjunto.
    return destino.lower() in DESTINOS_AUTORIZADOS


# "for" recorre uno por uno los elementos de la lista entre corchetes.
for d in ["localhost", "scanme.nmap.org", "banco-real.com"]:
    # f"..." es una cadena con formato; {d:<20} alinea a la izquierda en 20 espacios.
    print(f"{d:<20} autorizado={esta_autorizado(d)}")
