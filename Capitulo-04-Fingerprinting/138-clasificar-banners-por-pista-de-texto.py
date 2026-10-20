# Diapositiva 138: Ejemplos de banners por servicio
# Muestra como identificar que servicio emitio un banner buscando pistas
# en el texto (prefijos como "SSH-", palabras como "ESMTP" o "Apache").

# Clasificar banners de ejemplo segun una pista en el texto
ejemplos = [  # lista de banners de ejemplo, uno por servicio
    "220 ProFTPD 1.3.5 Server",       # banner tipico de FTP
    "SSH-2.0-OpenSSH_8.2p1",          # banner tipico de SSH
    "220 mail.example.com ESMTP Postfix",  # banner tipico de correo (SMTP)
    "Apache/2.4.41 (Ubuntu)",         # cabecera tipica de un servidor web
]
for b in ejemplos:  # recorre cada banner de la lista
    if b.startswith("SSH-"):  # si el texto empieza por "SSH-"
        print(f"{b[:25]:25s} -> servicio SSH")  # es SSH
    elif "ESMTP" in b:  # si contiene la palabra "ESMTP"
        print(f"{b[:25]:25s} -> servicio de correo (SMTP)")  # es correo
    elif b.startswith("220"):  # si empieza por el codigo "220"
        print(f"{b[:25]:25s} -> servicio FTP")  # lo tomamos como FTP
    elif "Apache" in b or "nginx" in b:  # si menciona Apache o nginx
        print(f"{b[:25]:25s} -> servidor web")  # es un servidor web
