# pyhack - Ejemplos de Python para seguridad defensiva

Ejemplos de código comentados del curso **Hacking con Python**, pensados para aprender
Python aplicado a la seguridad. Cada archivo corresponde a una diapositiva del curso, trae
el número de diapositiva en el nombre y un comentario en cada linea, para quien ve Python
por primera vez.

Aqui estan solo los ejemplos **completos y autoejecutables** (163 de los del curso). Los
que son fragmentos de una construcción más larga se trabajan en el material del curso.

## Marco etico (importante)

Este material es para **hacking etico y defensa**: aprender a encontrar fallas, con permiso
y en entornos controlados, para cerrarlas. Todos los ejemplos apuntan a destinos propios o
autorizados: `localhost`, la maquina virtual del laboratorio, Metasploitable 2 en una red
aislada, o `scanme.nmap.org` (que Nmap autoriza para pruebas). Usar estas tecnicas contra
sistemas de terceros sin autorización escrita es un delito; en Colombia lo tipifica la Ley
1273 de 2009. Uselo con responsabilidad.

## Estructura

| Carpeta | Tema |
|---|---|
| Capitulo-01-Fundamentos | Fundamentos de Python para seguridad |
| Capitulo-02-OSINT | Reconocimiento con fuentes abiertas (OSINT) |
| Capitulo-03-Automatización | Automatización de consultas y escaneos pasivos |
| Capitulo-04-Fingerprinting | Identificación de servicios y banners |
| Capitulo-05-Web-HTTP | Automatización HTTP y pruebas web en laboratorio |
| Capitulo-06-Networking-Scapy | Redes con sockets, Scapy y SSH |
| Capitulo-07-Integración-Frameworks | Integración con frameworks y TOR |
| Capitulo-08-Proyecto-Final | Proyecto final, empaquetado y buenas practicas |

## Como ejecutarlos

Cada ejemplo corre con Python 3.11 o superior. Algunos usan bibliotecas externas que se
instalan en un entorno virtual:

```
python3 -m venv .venv
source .venv/bin/activate
pip install requests beautifulsoup4 lxml dnspython python-whois shodan \
            scapy paramiko pymetasploit3 PySocks stem aiohttp backoff
```

Luego, por ejemplo:

```
python3 Capitulo-01-Fundamentos/15-clasificar-ip-privada-publica.py
```

## Licencia de uso

Material educativo. Uselo para aprender y para proteger sistemas propios o autorizados.
