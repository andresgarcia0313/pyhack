# Diapositiva 267: Rotacion con stem, funcion rotar_identidad_tor() parte 2
# Completa la rotacion (autenticar, senalar NEWNYM y esperar) y agrega una
# funcion para consultar la IP de salida actual y comprobar que cambio.

from stem import Signal  # senales que podemos enviarle a TOR
from stem.control import Controller  # objeto que controla TOR por el Control Port
import requests, time  # requests para peticiones HTTP, time para pausas

TOR_PROXY = {"http": "socks5h://127.0.0.1:9050",  # proxy TOR para HTTP con DNS incluido
             "https": "socks5h://127.0.0.1:9050"}  # proxy TOR para HTTPS con DNS incluido

def rotar_identidad_tor(password: str = "mi_password_segura") -> None:  # funcion que pide un circuito nuevo
    try:  # intentamos la operacion y capturamos errores
        with Controller.from_port(port=9051) as controlador:  # abrimos conexion al Control Port (9051)
            controlador.authenticate(password=password)  # nos autenticamos con la contrasena en claro
            controlador.signal(Signal.NEWNYM)  # enviamos la senal NEWNYM: pide un circuito nuevo
            print("[*] Nuevo circuito TOR solicitado.")  # avisamos que pedimos la nueva identidad
            time.sleep(10)  # espera minima de 10 segundos que impone TOR entre rotaciones
    except Exception as e:  # si algo falla, atrapamos el error
        print(f"[!] Error al rotar identidad: {e}")  # mostramos el mensaje del error

def obtener_ip_actual() -> str:  # funcion que devuelve, como texto, la IP de salida actual
    """Devuelve la IP de salida actual a traves de TOR."""  # texto de ayuda de la funcion
    try:  # intentamos la consulta y capturamos errores
        r = requests.get("https://api.ipify.org?format=json",  # servicio que devuelve tu IP publica
                         proxies=TOR_PROXY, timeout=30)  # la consulta sale por TOR con plazo generoso
        return r.json().get("ip", "Desconocida")  # extraemos el campo "ip"; si no esta, devolvemos "Desconocida"
    except Exception as e:  # si algo falla, atrapamos el error
        return f"Error: {e}"  # devolvemos el error como texto
