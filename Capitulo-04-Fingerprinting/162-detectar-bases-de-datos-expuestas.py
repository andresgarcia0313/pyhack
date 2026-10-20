# Diapositiva 162: Clasificacion de servicios - concepto
# Muestra las dos dimensiones de la clasificacion (tipo y exposicion) respondiendo
# una pregunta concreta del cliente: hay bases de datos expuestas directamente a Internet?

# Las dos dimensiones de la clasificacion, aplicadas a una pregunta del cliente
servicios = [  # lista de servicios detectados; cada uno es un diccionario
    {"puerto": 3306, "tipo": "Base de datos", "expuesto_internet": True},  # MySQL abierto a Internet
    {"puerto": 80,   "tipo": "Servicio web",  "expuesto_internet": True},  # servidor web abierto a Internet
]
# Pregunta: hay bases de datos expuestas directamente a Internet?
expuestas = [s for s in servicios if s["tipo"] == "Base de datos" and s["expuesto_internet"]]  # filtra las bases de datos expuestas
print(f"Bases de datos expuestas a Internet: {len(expuestas)} -> {'ALERTA' if expuestas else 'OK'}")  # cuenta y avisa
# Bases de datos expuestas a Internet: 1 -> ALERTA
