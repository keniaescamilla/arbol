
# DICCIONARIO CON ARBOL BINARIO KENIA ESCAMILLA SM42

# raiz
class Nodo:
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado
        self.izquierda = None
        self.derecha = None

# se crea la clase diccionario, tendra como atributo a raiz que inicia con valor de "ninguno" 
class Diccionario:
    def __init__(self):
        self.raiz = None

        #  este método recibe una palabra y su significado. Si la raíz es nula, se crea un nuevo nodo y se asigna como raíz. Si no es nula, se llama 
        # al siguiente metodo: agregar_recursivo

    def agregar_palabra(self, palabra, significado):
        self.raiz = self._agregar_recursivo(self.raiz, palabra, significado)


        # Si el nodo es nulo se crea un nuevo nodo con la palabra y el significado proporcionados, si  no es nulo, se desciende por el arbol izquierdo o derecho 
        # dependiendo de la comparación entre la palabra actual y la del nodo actual.

    def _agregar_recursivo(self, nodo, palabra, significado):
        if nodo is None:
            return Nodo(palabra, significado)
        if palabra < nodo.palabra:
            nodo.izquierda = self._agregar_recursivo(nodo.izquierda, palabra, significado)
        else:
            nodo.derecha = self._agregar_recursivo(nodo.derecha, palabra, significado)
        return nodo

    def buscar_significado(self, palabra):
        return self._buscar_recursivo(self.raiz, palabra)

    def _buscar_recursivo(self, nodo, palabra):
        if nodo is None or nodo.palabra == palabra:
            if nodo:
                return nodo.significado
            else:
                return "Palabra no encontrada"
        if palabra < nodo.palabra:
            return self._buscar_recursivo(nodo.izquierda, palabra)
        return self._buscar_recursivo(nodo.derecha, palabra)

if __name__ == "__main__":
    diccionario = Diccionario()
    diccionario.agregar_palabra("casa", "Lugar donde vive una persona")
    diccionario.agregar_palabra("perro", "Animal doméstico")
    diccionario.agregar_palabra("gato", "Animal doméstico similar al perro pero mejor")
    diccionario.agregar_palabra("ut", "es la universidad tecnologica")
    diccionario.agregar_palabra("computadora", "Dispositivo electrónico para procesar información.")
    diccionario.agregar_palabra("teléfono", "Dispositivo de comunicación para hablar a distancia.")
    diccionario.agregar_palabra("internet", "Red de comunicación global que permite intercambiar información.")
    diccionario.agregar_palabra("programación", "Proceso de escribir código para crear software.")
    diccionario.agregar_palabra("base de datos", "Conjunto organizado de datos.")
    diccionario.agregar_palabra("arbol binario", "Una estructura de datos en la que cada nodo tiene, como máximo, dos hijos: uno izquierdo y uno derecho. El nodo superior se llama raíz, y los nodos sin hijos se denominan hojas.")
    diccionario.agregar_palabra("inorden ", "Recorrido en el que primero visitamos el subárbol izquierdo, luego el nodo raíz y finalmente el subárbol derecho.")
    diccionario.agregar_palabra("preorden", "Es un recorrido de un árbol en el que primero visitamos el nodo raíz, luego el subárbol izquierdo y finalmente el subárbol derecho.")
    diccionario.agregar_palabra("postorden", "Recorrido en el que primero visitamos el subárbol izquierdo, luego el subárbol derecho y finalmente el nodo raíz.")
    diccionario.agregar_palabra("hojas", "Son los nodos que no tienen hijos en un árbol. Son los nodos terminales sin nodos hijos debajo de ellos.")
    diccionario.agregar_palabra("nodos", " Son los elementos individuales en un árbol. Cada nodo tiene un valor y puede tener referencias a otros nodos (hijos).")



# esto permitira visualizar al usuario el programa: (ejecutar : python arbolbin.py )
    while True:
        palabra = input("Ingrese la palabra  para buscar su significado (o 'salir' para terminar): ").lower()
        if palabra == 'salir':
            break
        significado = diccionario.buscar_significado(palabra)
        print(f"Significado de '{palabra}': {significado}")
