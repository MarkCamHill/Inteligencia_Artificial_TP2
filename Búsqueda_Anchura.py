from arbol import Nodo  # clase en arbol.py

#Funcion de busqueda en anchura BFS
def buscar_posicion_BFS(estado_inicial, estado_objetivo, limite_izq, limite_der):
    solucionado = False #Variable para ver si se lleg[o a la solucion
    nodos_visitados = [] #Lista de nodos visitado
    nodos_frontera = []# Lista de nodos a visitar

    nodo_inicial = Nodo(estado_inicial) #Toamos el primer nodo
    nodos_frontera.append(nodo_inicial) 

    while not solucionado and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)

        if nodo.get_datos() == estado_objetivo:
            solucionado = True
            return nodo.get_datos()  # Solo se devuelve la posición final

        actual = nodo.get_datos()
        hijos = []

        # Movimiento hacia la izquierda
        if actual - 1 >= limite_izq:
            hijo_izq = Nodo(actual - 1)
            hijo_izq.set_padre(nodo)
            if not hijo_izq.en_lista(nodos_visitados) and not hijo_izq.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izq)
                hijos.append(hijo_izq)

        # Movimiento hacia la derecha
        if actual + 1 <= limite_der:
            hijo_der = Nodo(actual + 1)
            hijo_der.set_padre(nodo)
            if not hijo_der.en_lista(nodos_visitados) and not hijo_der.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_der)
                hijos.append(hijo_der)

        nodo.set_hijos(hijos)

    return None  # No se encontró solución

# ---------- Prueba del algoritmo -----------
if __name__ == "__main__":
    estado_inicial = 0
    estado_objetivo = 3
    limite_izq = -20
    limite_der = 20

    posicion_final = buscar_posicion_BFS(estado_inicial, estado_objetivo, limite_izq, limite_der)

    if posicion_final is not None:
        print("Posición final encontrada:", posicion_final)
    else:
        print("No se encontró una solución.")
