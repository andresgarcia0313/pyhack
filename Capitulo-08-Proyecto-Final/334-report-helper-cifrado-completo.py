# Diapositiva 334: Script report_helper.py, hash SHA-256 y cifrado con Fernet, parte 2
# Muestra el script completo (partes 331 a 334): clasifica severidad, calcula
# el hash de una evidencia, la cifra con Fernet y comprueba que descifra bien.

# hashlib para el hash, datetime para fechas y Fernet para cifrar.
import hashlib
from datetime import datetime, timezone
from cryptography.fernet import Fernet


# Traduce el puntaje CVSS a su etiqueta de severidad.
def clasificar_severidad(cvss: float) -> str:
    if cvss >= 9.0:
        return "Critica"
    if cvss >= 7.0:
        return "Alta"
    if cvss >= 4.0:
        return "Media"
    if cvss > 0.0:
        return "Baja"
    return "Informativa"


# Calcula el hash SHA-256 de un archivo leyendolo en bloques de 64 KB.
def hash_archivo(ruta: str) -> str:
    sha256 = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            sha256.update(bloque)
    return sha256.hexdigest()


# Cifra un archivo con Fernet y devuelve el hash del archivo cifrado.
def cifrar_evidencia(ruta_original: str, ruta_cifrada: str, clave: bytes) -> str:
    # Creamos el objeto Fernet con la clave recibida.
    fernet = Fernet(clave)
    # Leemos el contenido original en bytes.
    with open(ruta_original, "rb") as f:
        datos = f.read()
    # Escribimos la version cifrada en el archivo de destino.
    with open(ruta_cifrada, "wb") as f:
        f.write(fernet.encrypt(datos))
    # Calculamos el hash del archivo cifrado para probar su integridad.
    hash_cifrado = hash_archivo(ruta_cifrada)
    print(f"[+] Cifrado: {ruta_cifrada} | SHA-256: {hash_cifrado[:16]}...")
    # El original NO se borra aqui; se elimina con 'shred' tras verificar el cifrado.
    return hash_cifrado


# Programa de prueba: solo corre si ejecutamos el archivo directamente.
if __name__ == "__main__":
    # Creamos un archivo de evidencia de ejemplo.
    with open("evidencia.txt", "w", encoding="utf-8") as f:
        f.write("Captura de la inyeccion SQL en /login\n")
    # Generamos una clave de cifrado nueva.
    clave = Fernet.generate_key()
    # Mostramos la severidad de un CVSS 9.8.
    print("Severidad de 9.8:", clasificar_severidad(9.8))
    # Mostramos el inicio del hash del archivo original.
    print("SHA-256 original:", hash_archivo("evidencia.txt")[:16], "...")
    # Ciframos la evidencia.
    cifrar_evidencia("evidencia.txt", "evidencia.txt.enc", clave)
    # Verificacion: leemos el original y desciframos la copia cifrada.
    original = open("evidencia.txt", "rb").read()
    descifrado = Fernet(clave).decrypt(open("evidencia.txt.enc", "rb").read())
    # Comprobamos que el descifrado coincide con el original.
    print("El descifrado coincide con el original?", original == descifrado)
