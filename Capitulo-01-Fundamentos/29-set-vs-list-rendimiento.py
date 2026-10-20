# Diapositiva 29: Cuatro estructuras clave para hacking etico
# Mide la diferencia de velocidad entre buscar en una lista (O(n)) y en un
# conjunto (O(1)) con 200.000 direcciones.

# timeit mide cuanto tarda un pedazo de codigo.
import timeit

# Comprension que genera 200.000 IP de texto; // es division entera y % es el resto.
ips_lista = [f"10.{i // 65536}.{i // 256 % 256}.{i % 256}" for i in range(200_000)]
# Convierte la lista en conjunto (set), que usa tabla hash.
ips_set = set(ips_lista)
# Toma la ultima IP: el peor caso para la lista, que la revisa toda.
buscada = ips_lista[-1]                       # el peor caso para la lista

# Mide 100 busquedas en la lista con "in" (recorre uno por uno).
t_lista = timeit.timeit(lambda: buscada in ips_lista, number=100)
# Mide 100 busquedas en el conjunto con "in" (salto directo).
t_set = timeit.timeit(lambda: buscada in ips_set, number=100)
# Muestra ambos tiempos y cuantas veces es mas rapido el conjunto.
print(f"lista: {t_lista:.4f} s | set: {t_set:.6f} s | el set es ~{t_lista / t_set:,.0f} veces mas rapido")
