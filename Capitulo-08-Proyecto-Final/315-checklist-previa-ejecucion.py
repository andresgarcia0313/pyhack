# Diapositiva 315: Lista de chequeo previa, niveles documental y tecnico
# Muestra como una lista de chequeo en codigo impide avanzar si falta algun
# control, reuniendo el nivel documental y el nivel tecnico.

# Nivel documental: los permisos y papeles que deben existir.
checklist_documental = {
    "loa_firmada": True,            # carta de autorizacion firmada
    "nda_vigente": True,           # acuerdo de confidencialidad en vigor
    "scope_json_con_hash": True,   # alcance tecnico con su huella registrada
}
# Nivel tecnico: que los controles del codigo esten listos.
checklist_tecnico = {
    "scope_guard_probado": True,       # las guardas se probaron en el laboratorio
    "ips_origen_registradas": False,   # aun no se registraron en el cliente
    "canal_emergencia_activo": True,   # el contacto de emergencia esta disponible
}

# Recorremos los dos diccionarios y juntamos las claves cuyo valor es False (lo pendiente).
pendientes = [k for d in (checklist_documental, checklist_tecnico)
              for k, v in d.items() if not v]
# Si queda algo pendiente, no se puede iniciar.
if pendientes:
    print("[NO INICIAR] Pendientes:", ", ".join(pendientes))
# Si todo esta en True, los controles previos estan superados.
else:
    print("[LISTO] Todos los controles previos superados.")
