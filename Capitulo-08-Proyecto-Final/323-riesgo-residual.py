# Diapositiva 323: Matriz de riesgos operativos del proyecto
# Muestra como calcular el riesgo residual (lo que queda tras aplicar el
# control) y decidir si es aceptable o si necesita decision del cliente.

# Lista de riesgos con su nivel inherente y cuanto lo reduce el control (escala 1 a 5).
riesgos = [
    {"id": "DoS", "inherente": 4, "reduccion_control": 3},
    {"id": "Fuga", "inherente": 5, "reduccion_control": 3},
]
# Recorremos cada riesgo para calcular su valor residual.
for r in riesgos:
    # Restamos la reduccion al nivel inherente; max con 1 evita que baje de 1.
    residual = max(r["inherente"] - r["reduccion_control"], 1)  # nunca baja de 1
    # Consideramos aceptable un residual de 2 o menos.
    aceptable = residual <= 2
    # Mostramos el riesgo, su valor residual y si es aceptable o requiere decision.
    print(f"{r['id']}: residual={residual} -> "
          f"{'aceptable' if aceptable else 'requiere decision del cliente'}")
