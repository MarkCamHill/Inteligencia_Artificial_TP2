class Nodo: #implementación de la estructura de datos árbol (García Serrano, A. (2012). Inteligencia artificial. Fundamentos, práctica y aplicaciones. España: RC Libros.)
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.coste = None
        if hijos:
            self.set_hijos(hijos)

    def set_hijos(self, hijos):
        self.hijos = hijos
        for h in self.hijos:
            h.padre = self

    def get_hijos(self):
        return self.hijos

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_coste(self, coste):
        self.coste = coste

    def get_coste(self):
        return self.coste

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        return any(self.igual(n) for n in lista_nodos)

    def __str__(self):
        return str(self.get_datos())
