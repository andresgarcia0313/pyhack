# Diapositiva 262: Verificacion del trafico por TOR
# Muestra la diferencia entre socks5h:// (enruta tambien el DNS por TOR, sin fugas)
# y socks5:// (resuelve el DNS localmente, lo que puede filtrar los dominios).

# socks5h:// enruta tambien el DNS por TOR (evita fuga de DNS)
proxies_correcto = {"http": "socks5h://127.0.0.1:9050",  # trafico HTTP por TOR con DNS incluido
                    "https": "socks5h://127.0.0.1:9050"}  # trafico HTTPS por TOR con DNS incluido

# socks5:// resuelve el DNS localmente -> posible fuga de DNS (evitar)
proxies_con_fuga = {"http": "socks5://127.0.0.1:9050",  # aqui el DNS se resuelve en tu equipo (riesgo)
                    "https": "socks5://127.0.0.1:9050"}  # misma fuga para HTTPS
