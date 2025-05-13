import heapq #Estructura de cola de prioridad

# Busqueda Heurística donde se estima la distancia entre posición actual y objetivo
def heuristica(pos_actual, pos_objetivo):
    return abs(pos_actual - pos_objetivo)

def a_estrella(inicio, objetivo):
    # Cola de prioridad: (f, g, posicion)
    # f = g + h
    frontera = []
    heapq.heappush(frontera, (heuristica(inicio, objetivo), 0, inicio))
    visitados = set()#Lista de posiciones ya visitadas.

    while frontera:
        f, g, actual = heapq.heappop(frontera)

        if actual == objetivo:
            return actual  # Se alcanzó el objetivo

        if actual in visitados:
            continue
        visitados.add(actual)

        # Generar posiciones vecinas (izquierda y derecha)
        for vecino in [actual - 1, actual + 1]:
            if vecino not in visitados:
                nuevo_g = g + 1
                nuevo_f = nuevo_g + heuristica(vecino, objetivo)
                heapq.heappush(frontera, (nuevo_f, nuevo_g, vecino))

#Ejemplo
if __name__ == "__main__":
    inicio = 0
    objetivo = 15

    resultado = a_estrella(inicio, objetivo)

    if resultado is not None:
        print(f"Posición alcanzada: {resultado}")

