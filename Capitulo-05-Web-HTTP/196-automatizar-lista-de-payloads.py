# Diapositiva 196: 5.3 Pruebas automatizadas sobre aplicaciones web vulnerables (introduccion)
# Muestra que conviene automatizar lo repetitivo: recorrer una lista de
# payloads. El criterio humano decide despues cuales hallazgos son reales.

# Lista de entradas de prueba (payloads) que un humano se cansaria de teclear.
payloads = ["'", "' OR '1'='1", "<script>alert(1)</script>"]
# Un humano se cansa tras unas pocas; un script prueba todas y registra cada resultado.
# El criterio humano decide DESPUES cuales hallazgos son reales y como encadenarlos.
for p in payloads:   # recorremos cada payload de la lista
    # {p!r} muestra el payload con sus comillas visibles, para ver exactamente que se envia
    print(f"Probar payload: {p!r}  (solo contra DVWA/laboratorio autorizado)")
