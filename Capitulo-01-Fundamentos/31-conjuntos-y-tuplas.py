# Diapositiva 31: Conjuntos y tuplas, deduplicacion e inmutabilidad
# Muestra las cuatro operaciones de conjuntos sobre fuentes OSINT y una tupla
# inmutable de configuracion que se desempaqueta.

# Conjunto con los subdominios de la fuente A (sin duplicados).
fuente_a = {"mail.ejemplo.com", "www.ejemplo.com", "vpn.ejemplo.com"}
# Conjunto con los subdominios de la fuente B.
fuente_b = {"www.ejemplo.com", "api.ejemplo.com", "dev.ejemplo.com"}

# Union "|": todos los unicos de ambas fuentes; len cuenta cuantos son.
print(f"[+] Unicos (|): {len(fuente_a | fuente_b)}")
# Interseccion "&": lo que esta en ambas fuentes.
print(f"[+] Confirmados por ambas (&): {fuente_a & fuente_b}")
# Diferencia "-": lo que esta en B pero no en A; sorted lo ordena.
print(f"[+] Solo en B (-): {sorted(fuente_b - fuente_a)}")
# Diferencia simetrica "^": lo que esta en una sola fuente.
print(f"[+] En una sola (^): {len(fuente_a ^ fuente_b)}")

# Tupla: configuracion fija (host, puerto); no se puede modificar.
SERVIDOR_LAB = ("127.0.0.1", 4444)       # tupla: configuracion fija
# Desempaqueta la tupla: cada posicion va a una variable.
host, puerto = SERVIDOR_LAB
print(f"[*] Escucharia en {host}:{puerto}")
# Intenta modificar la tupla, lo cual no esta permitido.
try:
    # Asignar un elemento de una tupla lanza TypeError.
    SERVIDOR_LAB[1] = 8080
except TypeError as e:
    print(f"[!] {e}")
