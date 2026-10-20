# Diapositiva 182: Clientes HTTP en Python: tres niveles de abstraccion
# Muestra el mismo GET resuelto en tres niveles: requests (alto),
# urllib (medio) y socket (bajo, control total).

import socket, urllib.request, requests  # tres librerias, una por cada nivel

# Alto nivel (requests): todo en una sola linea, comodo y potente.
print(requests.get("http://127.0.0.1").status_code)   # imprime el codigo de estado

# Nivel medio (urllib): viene con Python pero es mas verboso.
with urllib.request.urlopen("http://127.0.0.1") as r:  # abre la conexion y la cierra sola
    print(r.status)                                    # imprime el codigo de estado

# Bajo nivel (socket): control byte a byte, util para peticiones malformadas.
s = socket.socket(); s.settimeout(3); s.connect(("127.0.0.1", 80))  # creamos socket, timeout y conectamos
s.send(b"GET / HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n")  # enviamos la peticion cruda en bytes
print(s.recv(100).decode(errors="replace").splitlines()[0]); s.close()    # leemos, mostramos la 1a linea y cerramos
