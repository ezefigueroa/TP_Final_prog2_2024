import heapq
from .models import City, Route

#def dijkstra(start_city):
 #   distances = {start_city:0}
  #  previous_cities = {start_city:None}
    # completar
    
   # return distances, previous_cities

def dijkstra(start_city):
    ciudades = City.objects.all()
    distances = {ciudad: float('inf') for ciudad in ciudades}
    distances[start_city] = 0
    previous_cities = {ciudad: None for ciudad in ciudades}
    
    visitar = []
    heapq.heappush(visitar, (0, start_city))

    while visitar != []:
        distancia_actual, ciudad_actual = heapq.heappop(visitar)

        if distancia_actual > distances[ciudad_actual]:
            continue

        rutas = Route.objects.filter(start_city=ciudad_actual)

        for ruta in rutas:
            vecino = ruta.end_city
            nueva_distancia = distancia_actual + ruta.distance

            if nueva_distancia < distances[vecino]:
                distances[vecino] = nueva_distancia
                previous_cities[vecino] = ciudad_actual
                heapq.heappush(visitar, (nueva_distancia, vecino))

    return distances, previous_cities








def get_shortest_path(start_city, end_city):
    distances, previous_cities = dijkstra(start_city)
    path = []
    city = end_city

    while previous_cities[city]:
        path.insert(0, city)
        city = previous_cities[city]
    path.insert(0, city)

    return path, distances[end_city]

# Con la clase ArbolBinarioBusqueda, se representa un ABB y se especifican los métodos que se podrá realizar con ellos.
class ArbolBinarioBusqueda:

    def __init__(self): #se define el constructor de la clase para inicializar un ABB con sus respectivos atributos: raiz y tamano.
        self.raiz = None #atributo que va a almacenar la raiz del ABB, es decir el nodo inicial. Se asigna None ya que al crear un nuevo objeto de ABB, el árbol está vacio.
        self.tamano = 0 #atributo que va a indicar el tamano del ABB, es decir, cuántos nodos va a tener el árbol. Se asigna 0 ya que inicialmente el árbol está vacio.

    def agregar(self,clave,valor): #este método permite agregar, insertar un nuevo nodo al árbol. Toma cómo parámetros una clave (identificador del nodo) y un valor (dato asociado a la clave)
        if self.raiz: #se evalúa si el nodo raiz está vacio (None) o no. Si no está vacio...
            self._agregar(clave,valor,self.raiz) #si el nodo raíz no está vacio ingresa a esta condición y se llama al método _agregar para insertar el nuevo nodo en un lugar que corresponda.        
        else: #en caso contrario, es decir, si el árbol está vacio...
            self.raiz = NodoArbol(clave,valor) #se crea un nodo y pasa a ser la raíz del árbol. Para ello, se le pasa como argumento una clave y un valor. 
        self.tamano = self.tamano + 1 #cada vez que se agrega un nuevo nodo al árbol se incrementa 1 para llevar el conteo de la cantidad de nodos que hay en el árbol.

    def _agregar(self,clave,valor,nodoActual): #este método es recursivo y permite insertar un nodo en el ABB buscando el lugar adecuado. Toma como parámetros la clave, valor y nodoActual en el que se encuentra el método durante la búsqueda.
        if clave < nodoActual.clave: #se compara la clave que se quiere agregar con la clave del nodoActual; si la clave a agregar es menor a la clave del nodoActual entra a la condición...
            if nodoActual.tieneHijoIzquierdo(): #si el nodo actual tiene un Hijo Izquierdo, entra a la condición...
                self._agregar(clave,valor,nodoActual.hijoIzquierdo) #se llama al método de manera recursiva sobre el hijo izquierdo para encontrar donde insertar el nuevo nodo.
            else: #en caso contrario, si el nodo actual no tiene un hijo izquierdo....
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual) #como no hay un hijo izquierdo, se crea un nuevo nodo, se lo asigna como hijo izquierdo del nodo actual y se inserta el nuevo nodo en esa posicion. El nuevo nodo tendrá como padre al nodoActual
        else: #si la clave  que se quiere agregar no es menor a la clave del nodoActual, el nuevo nodo debe ir de lado derecho del nodo actual.
            if nodoActual.tieneHijoDerecho(): #si el nodo actual tiene un Hijo Derecho, entra a la condición...
                self._agregar(clave,valor,nodoActual.hijoDerecho) #se llama al método de manera recursiva sobre el hijo derecho para encontrar donde insertar el nuevo nodo.
            else: #en caso contrario, si el nodoActual no tiene un hijo derecho...
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual) #como no hay un hijo derecho, se crea un nuevo nodo, se lo asigna como hijo derecho del nodo actual y se inserta el nuevo nodo en esa posicion. El nuevo nodo tendrá como padre al nodoActual

    def __setitem__(self,c,v): #método para agregar nodos al ABB utilizando sintaxis de acceso de un diccionario, tomando como parámetro c (clave) que se utiliza para insertar un valor en el árbol y v (valor) que se asocia con la clave c en el ABB
        self.agregar(c,v) #Se llama al método agregar que comentamos anteriormente para insertar un nuedo nodo en el ABB

    def obtener(self,clave): #este método toma como argumento una clave para buscar un valor en el ABB
        if self.raiz: # si el árbol tiene una raiz (no es None)
            res = self._obtener(clave,self.raiz) #se llama a este método para realizar una búsqueda de la clave en el árbol.
            if res: #si res es un nodo, la clave fue encontrada
                return res.cargaUtil #retorna el valor asociado a la clave encontrada
            else: #si res no es un nodo, la clave no fue encontrada
                return None #retorna None
        else: #si el árbol no tiene una raíz, está vacio...
            return None #retorna None, ya que no se puede buscar claves en un árbol vacio.

    def _obtener(self,clave,nodoActual): #este método es recursivo y busca un nodo en un ABB. Toma como parámetros la clave que se está buscando en el árbol y el nodo del árbol actual donde comienza la búsqueda.
        if not nodoActual: #si el nodoActual es None...
            return None #retorna None, no hay nodos
        elif nodoActual.clave == clave: #si la clave del nodo actual es igual a la clave que estamos buscando...
            return nodoActual #retorna el nodoActual ya que encuentra el nodo con la clave
        elif clave < nodoActual.clave: #si la clave que se busca es menor a la clave del nodo actual...
            return self._obtener(clave,nodoActual.hijoIzquierdo) #se llama al método _obtener de manera recursiva pasando como argumento nodoActual hijo izquierdo para seguir buscando en la rama izquierda del ABB
        else: #si las anteriores condiciones ninguna fue verdadera, es decir que la clave buscada es mayor que la del nodo actual...
            return self._obtener(clave,nodoActual.hijoDerecho) #se llama al método _obtener de manera recursiva pasando como argumento nodoActual hijo derecho para seguir buscando en la rama derecha del ABB
    
    def obtener_claves(self): #este método recorre el ABB y devuelve todas las claves en una lista
        claves = [] #se crea una lista vacía llamada claves para almacenar las claves de los nodos del ABB
        self._obtener_claves(self.raiz, claves) #se llama al método _obtener_claves pasando dos parámetros: la raiz del árbol y la lista que guardará las claves encontradas al recorrer el ABB
        return claves #devuelve la lista claves con todas las claves de los nodos del ABB obtenidas al recorrerlo

    def _obtener_claves(self, nodoActual, claves): #método recursivo que recorre en inorden el ABB para agregar sus claves a la lista claves, para ello toma como parámetros el nodoActual que está visitando actualmente en el recorrido y claves, que es la lsita en donde se guardarán las claves de los nodos.
        if nodoActual: #si el nodoActual no es None...el nodo actual existe
            self._obtener_claves(nodoActual.hijoIzquierdo, claves)  # se llama recursivamente al método _obtener_claves para recorrer el lado izquierdo del nodoActual. Recorre hijo izquierdo
            claves.append(nodoActual.clave)  # Añadir la clave del nodo actual a la lista claves
            self._obtener_claves(nodoActual.hijoDerecho, claves)  # se llama recursivamente al método _obtener_claves para recorrer el lado derecho del nodoActual. Recorrer el hijo derecho

    def obtener_lista(self): #método pra obtener una lista de los valores asociados a todas las claves del ABB
        return [self.obtener(clave) for clave in self.obtener_claves()] #llama a los métodos obtener y obtener_claves para obtener las claves ordenadas y los valores asociados a esas claves.

    def __getitem__(self,clave): #método para acceder a los valores almacenados en el árbol utilizando sintaxis de índice
        res = self.obtener(clave) #se llama al método obtener para recuperar el valor de la clave proporcionada y se guarda en res
        if res: #si res no es None...
            return res #se devuelve el valor guardado en res que se encontró
        else: #si res es None...
            raise KeyError('Error, la clave no está en el árbol') # la clave no se encontró en el árbol y figura una excepcion KeyError

    def __contains__(self,clave): #método que verifica si una clave existe en el ABB empleando la sintaxis in
        if self._obtener(clave,self.raiz): #se llama al método _obtener para buscar la clave en el árbol comenzando desde la raíz
            return True #si la clave existe, retorna True
        else: # si no se encuentra la clave y devuelve None...
            return False #se retorna False.

    def longitud(self): #método que devuelve el número de nodos del ABB
        return self.tamano #retorna el atributo de la clase que contiene el conteo de la cantidad de nodos en el árbol

    def __len__(self): #método especial de Python que devuelve el número de nodos del ABB
        return self.tamano #retorna el atributo de la clase que contiene el conteo de la cantidad de nodos en el árbol

    def __iter__(self): #método para iterar el árbol
        return self.raiz.__iter__() #se llama recursivamente para recorrer los nodos  

    def eliminar(self,clave): #este método elimina un nodo del ABB, toma como parámetro la clave que se quiere eliminar del árbol
        if self.tamano > 1: #si él arbol tiene más de un nodo porque self.tamano es mayor a 1...
            nodoAEliminar = self._obtener(clave,self.raiz) #se llama al método _obtener para bsucar el nodo que tiene la clave que se busca comenzando desde la raíz
            if nodoAEliminar: #si el nodo con la clave (a eliminar) fue encontrado...
                self.remover(nodoAEliminar) #llama al método remover para eliminar ese nodo del árbol
                self.tamano = self.tamano-1 #luego de la eliminación se actualiza el tamaño del árbol decrementando el valor de self.tamano en 1
            else: # si no se encontró el nodo a eliminar....
                raise KeyError('Error, la clave no está en el árbol') #se muestra una excepción KeyError 
        elif self.tamano == 1 and self.raiz.clave == clave: #si el árbol tiene un nodo y la clave que se quiere eliminar corresonde a la clave del nodo raíz...
            self.raiz = None #si el nodo a eliminar es la raíz y el árbol tiene solo un nodo, se establece self.raiz == None, eliminando así la raíz del árbol
            self.tamano = self.tamano - 1 #luego de la eliminación se actualiza el tamaño del árbol decrementando el valor de self.tamano en 1
        else: #si el árbol tiene un sólo nodo pero no coincide con la clave de la raíz
            raise KeyError('Error, la clave no está en el árbol') #se muestra una excepción KeyError

    def __delitem__(self,clave): #método especial de Python que busca eliminar un elemento de un objeto mediante el uso de la sintaxis del
        self.eliminar(clave) #llama al método eliminar

    def remover(self,nodoActual): #método para eliminar un nodo de un ABB, que toma como parámetro al nodoActual
        if nodoActual.esHoja(): #si el nodo que se esta eliminado es una hoja (nodo sin hijos)...
            if nodoActual == nodoActual.padre.hijoIzquierdo: #si el nodo es hijo izquierdo de su padre, se debe eliminar de la lista de hijos del padre
                nodoActual.padre.hijoIzquierdo = None #se asigna None al hijo izdquierdo del padre.
            else: #si el nodo no es el hijo izquierdo, y es el hijo derecho del padre...
                nodoActual.padre.hijoDerecho = None #Se elimina el nodo de la lista de hijos derechos del padre.
        elif nodoActual.tieneAmbosHijos(): #si el nodo tiene ambos hijos, se realiza una sustitución del nodo por su sucesor
            suc.empalmar() #se llama al mérodo empalmar sobre el sucesor para remover el sucesor del arbol y conecta sus hijos al lugar adecuadno en el árbol
            suc = nodoActual.encontrarSucesor() #Se busca el sucesor del nodo a eliminar, es decir, el nodo con la clave más pequeña en el subárbol derecho del nodo actual.
            nodoActual.clave = suc.clave #Después de obtener el sucesor, la clave del nodo actual es reemplazada por la clave del sucesor.
            nodoActual.cargaUtil = suc.cargaUtil #Similar a la clave, el valor del nodo actual se reemplaza con el valor del sucesor.
        else: # este nodo tiene un (1) hijo..
            if nodoActual.tieneHijoIzquierdo(): #Se verifica si el nodo tiene un hijo izquierdo.
                if nodoActual.esHijoIzquierdo(): #Se comprueba si el nodo a eliminar es el hijo izquierdo de su padre.
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre #Reemplazar la referencia del padre para que apunte correctamente al hijo izquierdo.
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo #Actualizar la estructura del árbol para que el nodo padre apunte al hijo izquierdo del nodo eliminado.
                elif nodoActual.esHijoDerecho(): #Si el nodo es el hijo derecho del padre, el hijo izquierdo del nodo actual reemplazará a ese nodo.
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre #se actualiza el padre del hijo izquierdo.
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo #El padre debe apuntar a su hijo izquierdo.
                else: #si el nodo no es ni hijo izquierdo ni hijo derecho...
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho)
            else: # Si tiene hijo derecho
                if nodoActual.esHijoIzquierdo():  # Si el nodo actual es el hijo izquierdo del padre
                    nodoActual.hijoDerecho.padre = nodoActual.padre #se actualiza el padre del hijo derecho
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho # El padre apunta al hijo derecho
                elif nodoActual.esHijoDerecho(): # Si el nodo actual es el hijo derecho del padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else:
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho)

    def inorden(self): #método que define el metodo que inicia el recorrido en inorden
        self._inorden(self.raiz) # Llama a la función recursiva _inorden con la raíz del árbol

    def _inorden(self,arbol): # Define el metodo para el recorrido en inorden
        if arbol != None: # Si el nodo actual no es None
            self._inorden(arbol.hijoIzquierdo) # Llama a _inorden para recorrer el subárbol izquierdo
            print(arbol.clave) # Imprime la clave del nodo actual
            self._inorden(arbol.hijoDerecho) # Llama a _inorden para recorrer el subárbol derecho


    def postorden(self): # Define el metodo que inicia el recorrido en post orden 
        self._postorden(self.raiz) # Llama a la función recursiva _postorden con la raíz del árbol


    def _postorden(self, arbol): # Define el metodo para el recorrido en postorden
        if arbol:# Si el nodo actual no es None
            self._postorden(arbol.hijoDerecho) # Llama a _postorden para recorrer el subárbol derecho
            self._postorden(arbol.hijoIzquierdo) # Llama a _postorden para recorrer el subárbol izquierdo
            print(arbol.clave) # Imprime la clave del nodo actual

    def preorden(self): # Define el metodo que inicia el recorrido en preorden
        self._preorden(self.raiz) # Llama a la función recursiva _preorden con la raíz del árbol

    def _preorden(self,arbol):  # Define el metodo para el recorrido en preorden
        if arbol: # Si el nodo actual no es None...
            print(arbol.clave) # Imprime la clave del nodo actual
            self._preorden(arbol.hijoIzquierdo) #Llama a _preorden para recorrer el subárbol izquierdo 
            self._preorden(arbol.hijoDerecho) # Llama a _preorden para recorrer el subárbol derecho

# Con la clase NodoArbol se crea un árbol binario
class NodoArbol: 
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None): #se define el constructor de la clase para inicializar un árbol con sus respectivos atributos.
        self.clave = clave #atributo que va a almacenar la clave del nodo
        self.cargaUtil = valor #atributo que va a almacenar el valor del nodo
        self.hijoIzquierdo = izquierdo #hijo izquierdo del nodo
        self.hijoDerecho = derecho #hijo derecho del nodo
        self.padre = padre #nodo padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self): #método que verifica si el nodo tiene un hijo izquierdo, devolviendo True o False.
        return self.hijoIzquierdo 

    def tieneHijoDerecho(self): #método que verifica si el nodo tiene un hijo derecho, devolviendo True o False.
        return self.hijoDerecho

    def esHijoIzquierdo(self): #método que verifica si el nodo es hijo izquierdo de su padre.
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self): #método que verifica si el nodo es hijo derecho de su padre.
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self): #método que verifica si el nodo es la raíz del árbol (no tiene padre)
        return not self.padre

    def esHoja(self): #método que verifica si el nodo es una hoja (si no tiene hijos ni izquierdo ni derecho)
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self): #método que verifica si el nodo tiene un hijo izquierdo o un hijo derecho
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self): #método que verifica si el nodo tiene ambos hijos izquierdo y derecho
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder): #método que reemplaza los datos del nodo (clave, valor) y sus hijos izquierdo y derecho.
        self.clave = clave # Reemplaza la clave del nodo.
        self.cargaUtil = valor # Reemplaza el valor asociado a la clave.
        self.hijoIzquierdo = hizq # Reemplaza el hijo izquierdo del nodo.
        self.hijoDerecho = hder # Reemplaza el hijo derecho del nodo.
        if self.tieneHijoIzquierdo(): #si el nodo tiene hijo izquierdo, actualiza el padre de ese hijo.
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho(): #si el nodo tiene hijo derecho, actualiza el padre de ese hijo.
            self.hijoDerecho.padre = self

    def encontrarSucesor(self): #método que busca el sucesor inorden del nodo (es decir, el nodo con la siguiente clave mayor).
        suc = None
        if self.tieneHijoDerecho(): # Si el nodo tiene hijo derecho, el sucesor es el nodo con el valor mínimo en el subárbol derecho.
            suc = self.hijoDerecho.encontrarMin()
        else: # Si no tiene hijo derecho, sube por el árbol buscando el primer ancestro que sea hijo izquierdo de su padre.
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre.encontrarSucesor() # El sucesor es el padre si este nodo es hijo izquierdo.
                else: # Si el nodo es hijo derecho, sube al padre y busca su sucesor.
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def empalmar(self):
        # Elimina el nodo del árbol, "empalmando" sus hijos con su padre.
        if self.esHoja(): # Si el nodo es una hoja, simplemente elimina la referencia de su padre a él.
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo(): # Si el nodo tiene un hijo (izquierdo o derecho), reemplaza el nodo con su único hijo.
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo # Si es hijo izquierdo, el padre apunta al hijo izquierdo.
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo # Si es hijo derecho, el padre apunta al hijo izquierdo.
                self.hijoIzquierdo.padre = self.padre # Actualiza el padre del hijo izquierdo.
            else:
                if self.esHijoIzquierdo(): 
                    self.padre.hijoIzquierdo = self.hijoDerecho # Si es hijo izquierdo, el padre apunta al hijo derecho.
                else:
                    self.padre.hijoDerecho = self.hijoDerecho # Si es hijo derecho, el padre apunta al hijo derecho.
                self.hijoDerecho.padre = self.padre # Actualiza el padre del hijo derecho.

    def encontrarMin(self): #método que # Encuentra el nodo con la clave mínima en el subárbol (el más a la izquierda).
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo # Baja al hijo izquierdo hasta llegar al nodo más a la izquierda.
        return actual

    def __iter__(self): # Permite la iteración sobre el árbol inorden (izquierda, raíz, derecha).
        if self:
            if self.tieneHijoIzquierdo(): # Si tiene hijo izquierdo, itera sobre él.
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.clave # Luego devuelve la clave del nodo actual.
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho: # Si tiene hijo derecho, itera sobre él.
                    yield elem