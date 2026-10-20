# Diapositiva 253: Conexion RPC y busqueda de modulos SMB
# Muestra como conectarse al servidor RPC de Metasploit con pymetasploit3
# y buscar modulos auxiliares (no destructivos) relacionados con SMB.

from pymetasploit3.msfrpc import MsfRpcClient  # traemos la clase que habla con Metasploit por RPC
import time  # modulo del sistema para manejar pausas y tiempos (se usa mas adelante)

# 1. Conexion al servidor RPC de Metasploit
client = MsfRpcClient(  # creamos el cliente; aqui empieza la conexion con el daemon msfrpcd
    password="miPassword123",  # contrasena que configuramos al levantar msfrpcd
    username="msf",  # usuario con el que nos autenticamos ante el RPC
    port=55553,  # puerto donde escucha el servidor RPC de Metasploit
    ssl=False,  # sin cifrado TLS: solo valido en laboratorio local aislado
)
print("[+] Conexion establecida con Metasploit RPC")  # avisamos que la conexion funciono

# 2. Buscar modulos auxiliares relacionados con SMB
resultados = client.modules.search("smb")  # pedimos la lista de modulos que coinciden con "smb"
modulos_auxiliares = [m for m in resultados if m["type"] == "auxiliary"]  # dejamos solo los de tipo auxiliar
print(f"[*] Modulos auxiliares SMB encontrados: {len(modulos_auxiliares)}")  # mostramos cuantos quedaron
