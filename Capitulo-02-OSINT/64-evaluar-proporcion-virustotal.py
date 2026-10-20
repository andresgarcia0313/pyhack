# Diapositiva 64: Criterios de confiabilidad por servicio
# Muestra como interpretar VirusTotal por la proporcion de motores que marcan
# algo como malicioso, en vez de reaccionar ante una sola deteccion aislada.


def evaluar_virustotal(maliciosos: int, total_motores: int) -> str:  # recibe dos numeros y devuelve un texto
    if total_motores == 0:  # si no hay motores, no podemos calcular nada
        return "sin datos"  # avisamos que no hay informacion
    proporcion = maliciosos / total_motores  # dividimos para obtener la fraccion de coincidencias
    if proporcion >= 0.15:  # si al menos el 15 por ciento marca malicioso
        return f"indicador fuerte ({proporcion:.0%})"  # lo tratamos como senal fuerte, con el porcentaje
    if proporcion >= 0.10:  # si esta entre 10 y 15 por ciento
        return f"a revisar ({proporcion:.0%})"  # queda como caso a revisar
    return f"senal debil o falso positivo ({proporcion:.0%})"  # por debajo de 10 por ciento, senal debil


print(evaluar_virustotal(2, 70))   # 2 de 70 motores: senal debil o falso positivo (3%)
print(evaluar_virustotal(45, 70))  # 45 de 70 motores: indicador fuerte (64%)
