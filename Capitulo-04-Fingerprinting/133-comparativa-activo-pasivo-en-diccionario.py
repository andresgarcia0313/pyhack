# Diapositiva 133: Comparativa activo vs. pasivo (tabla)
# Muestra la tabla de diferencias como un diccionario de Python y la recorre
# para imprimirla ordenada, util para generar documentacion del informe.

comparativa = {  # diccionario: cada clave es un criterio y su valor es otro diccionario
    "Interaccion con objetivo": {"activo": "Si", "pasivo": "No"},        # fila 1
    "Detectabilidad":           {"activo": "Alta", "pasivo": "Muy baja"},  # fila 2
    "Precision":                {"activo": "Alta", "pasivo": "Media-alta"},# fila 3
    "Requiere sniffing":        {"activo": "No", "pasivo": "Si"},          # fila 4
    "Velocidad":                {"activo": "Rapido", "pasivo": "Depende del trafico"},  # fila 5
}
for criterio, valores in comparativa.items():  # recorre cada par criterio/valores del diccionario
    print(f"{criterio:28s} | activo: {valores['activo']:11s} | pasivo: {valores['pasivo']}")  # imprime la fila alineada en columnas
