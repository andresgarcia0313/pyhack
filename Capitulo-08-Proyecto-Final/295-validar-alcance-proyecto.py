# Diapositiva 295: Validacion de alcance en Python
# Muestra como detener un proyecto si falta algun campo obligatorio del
# documento de alcance, por ejemplo la autorizacion firmada.

# Lista con los nombres de todos los campos que un proyecto debe tener para arrancar.
CAMPOS_OBLIGATORIOS = [
    "nombre_cliente", "contacto_tecnico", "tipo_prueba",
    "activos_en_alcance", "activos_fuera_alcance",
    "fecha_inicio", "fecha_fin", "autorizacion_firmada",
]

# Diccionario con los datos de un proyecto de ejemplo.
proyecto_ejemplo = {
    "nombre_cliente": "Laboratorio Netec",
    "contacto_tecnico": "instructor@lab.local",
    "tipo_prueba": "caja_gris",
    "activos_en_alcance": ["192.168.56.0/24"],
    "activos_fuera_alcance": ["192.168.56.1"],   # puerta de enlace
    "fecha_inicio": "2026-10-19",
    "fecha_fin": "2026-10-21",
    "autorizacion_firmada": False,               # el cliente aun no firma
}


# Funcion que devuelve la lista de campos que faltan o estan vacios.
def validar_alcance(proyecto: dict) -> list[str]:
    """Devuelve la lista de campos obligatorios ausentes o vacios."""
    # proyecto.get(c) es None o vacio si el campo no existe o esta sin valor; not lo convierte en True.
    return [c for c in CAMPOS_OBLIGATORIOS if not proyecto.get(c)]


# Funcion principal que organiza el programa.
def main() -> None:
    # Pedimos la lista de campos faltantes del proyecto de ejemplo.
    faltantes = validar_alcance(proyecto_ejemplo)
    # Si la lista NO esta vacia, hay campos sin llenar.
    if faltantes:
        print("[ERROR] Campos faltantes:")
        # Mostramos uno por uno los campos que faltan.
        for campo in faltantes:
            print(f"  -> {campo}")
        # return termina la funcion aqui para no seguir adelante.
        return
    # Si no faltaba nada, avisamos que el proyecto puede iniciar.
    print("[OK] Validacion completada. El proyecto puede iniciar.")


# Esta linea hace que main() solo se ejecute cuando corremos el archivo directamente.
if __name__ == "__main__":
    main()
