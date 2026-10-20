# Diapositiva 177: HTTP, protocolo base de la web
# Muestra que HTTP es "sin estado": dos peticiones sueltas no se
# relacionan entre si; el servidor no recuerda la anterior.

import requests  # libreria para enviar peticiones HTTP

# Primera peticion: el servidor atiende y responde, pero no guarda nada sobre nosotros.
requests.get("http://127.0.0.1/pagina1")   # el servidor no sabe quienes somos

# Segunda peticion: llega como si fuera la primera vez; no recuerda la anterior.
requests.get("http://127.0.0.1/pagina2")   # tampoco relaciona esta con la de arriba

# Para que el servidor "recuerde", el cliente debe reenviar una cookie o un token
# en CADA peticion. Eso es lo que hace un navegador y lo que veremos con sesiones.
