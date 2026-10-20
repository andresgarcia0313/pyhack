# Diapositiva 73: Consultas DNS con dnspython
# Consulta varios tipos de registro DNS (A, MX, TXT) de un dominio y captura
# las excepciones para que un registro o dominio ausente no detenga el programa.

import dns.resolver  # modulo de dnspython que resuelve consultas DNS detalladas

objetivo = "example.com"  # dominio publico de ejemplo que vamos a consultar
for tipo in ("A", "MX", "TXT"):  # recorremos los tipos de registro que nos interesan
    try:  # protegemos cada consulta ante posibles fallos
        for registro in dns.resolver.resolve(objetivo, tipo):  # pedimos los registros de ese tipo
            print(f"{tipo}: {registro.to_text()}")  # mostramos el tipo y el contenido del registro
    except dns.resolver.NoAnswer:  # el dominio existe pero no tiene ese tipo de registro
        print(f"{tipo}: sin registros")  # avisamos que no hay ese registro
    except dns.resolver.NXDOMAIN:  # el dominio no existe en absoluto
        print(f"{tipo}: el dominio no existe")  # avisamos que el dominio no existe
        break  # no tiene sentido seguir consultando otros tipos
