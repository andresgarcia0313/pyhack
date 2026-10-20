# Diapositiva 26: Script integrado, escaneo de puertos (continuacion)
# Prueba el caso de error: un dominio .invalid que nunca resuelve. Muestra
# que el escaner informa y devuelve vacio sin caerse.
# Nota: requiere escaner_puertos.py en la misma carpeta (el del ejemplo 25,
# renombrado o copiado como escaner_puertos.py).

# Importa las dos funciones del script de la diapositiva 25.
from escaner_puertos import escanear_puertos, mostrar_resultados

# Escanea un dominio reservado que no existe; .invalid esta reservado por el RFC 2606.
resultado = escanear_puertos("objetivo.invalid", [80])
# Muestra el resultado, que sera un diccionario vacio.
print(f"[*] Resultado: {resultado}")
# Presenta el resultado: no imprime nada porque esta vacio, pero no falla.
mostrar_resultados(resultado)        # no imprime nada, pero no falla
