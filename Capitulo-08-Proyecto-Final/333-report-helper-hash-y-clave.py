# Diapositiva 333: Script report_helper.py, hash SHA-256 y cifrado con Fernet
# Muestra la funcion que calcula el hash de un archivo leyendolo en bloques y
# la que genera y guarda una clave Fernet (nunca junto a las evidencias).

# hashlib calcula la huella SHA-256.
import hashlib
# Fernet genera la clave de cifrado.
from cryptography.fernet import Fernet


# Funcion que calcula el hash SHA-256 de un archivo sin cargarlo entero en memoria.
def hash_archivo(ruta: str) -> str:
    """Calcula SHA-256 en bloques de 64 KB para no cargar archivos grandes en memoria."""
    # Creamos un objeto hash vacio.
    sha256 = hashlib.sha256()
    # Abrimos el archivo en modo binario.
    with open(ruta, "rb") as f:
        # Leemos bloques de 65536 bytes (64 KB) hasta que read devuelve bytes vacios (fin).
        for bloque in iter(lambda: f.read(65536), b""):
            # Vamos actualizando el hash con cada bloque.
            sha256.update(bloque)
    # Devolvemos la huella en hexadecimal.
    return sha256.hexdigest()


# Funcion que genera una clave Fernet y la guarda en un archivo.
def generar_clave(ruta_clave: str) -> bytes:
    """Genera una clave Fernet y la guarda en disco (nunca junto a las evidencias)."""
    # Creamos una clave nueva y aleatoria.
    clave = Fernet.generate_key()
    # La guardamos en el archivo indicado, en modo binario.
    with open(ruta_clave, "wb") as f:
        f.write(clave)
    # Avisamos donde quedo guardada.
    print(f"[+] Clave guardada en: {ruta_clave}")
    # Devolvemos la clave para usarla enseguida.
    return clave
