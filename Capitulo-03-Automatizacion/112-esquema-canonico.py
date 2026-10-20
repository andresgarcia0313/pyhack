# Diapositiva 112: Esquema canonico, contrato del pipeline
# Muestra el esquema canonico: un diccionario que fija los campos, sus
# tipos y los valores por defecto a los que todo registro debe ajustarse.

# esquema_canonico.py -- el contrato unico de todos los registros.

# SCHEMA asocia cada campo con el tipo de dato que esperamos.
SCHEMA = {
    "timestamp": str,   # ISO 8601, ej: "2024-06-15T14:32:00Z"
    "source": str,      # origen del dato: "shodan", "whois", "dns"
    "target": str,      # dominio o IP objetivo
    "ip_address": str,  # IPv4 o IPv6 ya normalizada
    "port": int,        # entero; None si no aplica
    "service": str,     # "http", "ssh", etc.
    "banner": str,      # texto del banner del servicio
    "country": str,     # codigo de pais ISO 3166-1 alpha-2, ej: "CO"
    "tags": list,       # etiquetas libres
}

# DEFAULTS genera los valores por defecto recorriendo el esquema:
# lista vacia para los campos de tipo list y None para el resto.
DEFAULTS = {k: ([] if v == list else None) for k, v in SCHEMA.items()}
