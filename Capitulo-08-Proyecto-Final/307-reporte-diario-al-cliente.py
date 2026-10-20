# Diapositiva 307: Comunicacion con el cliente, protocolo minimo
# Muestra como armar el texto de un correo de estado diario con las tareas
# completadas, en curso, los bloqueos y los hallazgos criticos.

# date permite trabajar con fechas sin hora.
from datetime import date

# Diccionario con el estado del dia: listas por categoria.
estado = {"completadas": ["T-01 DNS y crt.sh"], "en_curso": ["T-02 Banners"],
          "bloqueos": ["T-03 sin credenciales de prueba"],
          "criticos": []}

# Armamos el cuerpo del correo con triple comilla, que permite texto de varias lineas.
# join une las listas separando con coma; el "or 'ninguna'" pone un texto si la lista esta vacia.
correo = f"""Asunto: [PYT_HACK] Estado diario {date(2026, 10, 19).isoformat()}
Completadas: {', '.join(estado['completadas']) or 'ninguna'}
En curso: {', '.join(estado['en_curso']) or 'ninguna'}
Bloqueos: {', '.join(estado['bloqueos']) or 'ninguno'}
Hallazgos criticos preliminares: {', '.join(estado['criticos']) or 'ninguno'}
Canal de emergencia: instructor del curso"""
# Mostramos el correo en pantalla.
print(correo)
