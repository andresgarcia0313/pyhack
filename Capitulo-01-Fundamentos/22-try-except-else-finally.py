# Diapositiva 22: Estructura try / except / else / finally
# Muestra el orden de ejecucion de los cuatro bloques del manejo de errores,
# convirtiendo texto a numero de puerto.

# Recibe texto y devuelve un entero o None (int | None).
def leer_puerto(texto: str) -> int | None:
    # "try": aqui va lo que puede fallar.
    try:
        # int(texto) intenta convertir el texto a numero; falla si no es un numero.
        puerto = int(texto)
    # "except": corre solo si hubo ese error (texto no numerico).
    except ValueError:
        print(f"  except: {texto!r} no es un numero")
        return None
    # "else": corre solo si NO hubo error.
    else:
        print(f"  else: convertido {puerto}")
        return puerto
    # "finally": corre siempre, haya error o no.
    finally:
        print("  finally: siempre")


# Prueba con un valor valido ("443") y uno invalido ("https").
for t in ["443", "https"]:
    # Muestra la entrada y el resultado de la funcion.
    print(f"Entrada {t!r} ->", leer_puerto(t))
