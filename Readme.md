## TFI de Programación II: Proyecto Plataforma de Turismo Nacional

# Sobre el Proyecto
A partir de este proyecto se desarrolla un portal de turismo para la provincia de Mendoza, con el fin de aplicar los conocimientos aprendidos sobre POO, estructuras de datos, arboles binarios, grafos y complejidad de algoritmos, contenidos abordados a lo largo de la materia Programación II.
A través de este portal los usuarios podrán ingresar a informarse sobre la provincia de Mendoza, sus principales ciudades y atractivos turísticos. Además podrán encontrar la ruta más corta entre dos ciudades.

# ¿Qué se realizó?
Para su realización utilizamos el administrador de Django para cargar  datos de las ciudades de Mendoza con información turística relevante y rutas. Modificamos la clase City en el archivo models.py para poder realizarlo. Para mostrar la información nueva modificamos el template city_detail.html.
Por otra parte,  implementamos el algoritmo de Dijkstra para encontrar la ruta más corta entre dos ciudades y utilizamos árboles binarios de búsqueda (ABB) para ordenar la lista de ciudades antes de pasar los datos al frontend.
Para el diseño del portal utilizamos el framework Bootstrap y Django para la gestión de datos dinámicos. Creamos un contenedor principal que organiza el contenido en una estructura de filas y columnas. El contenido incluye imagen de portada, nombre de la provincia, un sistema de pestañas que contiene información de la provincia, atractivos, rutas de salida y rutas de llegada. El contenido es dinamico.

# Analisis de complejidad algoritmica de Dijkstra
Sobre el analisis de complejidad algoritmica de Dijkstra, al utilizar heap (cola de prioridad) tiene un orden  O(n log n) ya que necesita recorrer los vertices de un grafo (esto da O(n)) y luego para cada vértice, si la distancia se actualiza, se realiza una operación en el heap para insertar o actualizar el valor y esto da un O(log n). 

# Mejoras
El proyecto cumple con los requerimientos de la consigna. Sin embargo podemos visualizar mejoras como modificar el menu para agregar nuevas funcionalidades y modificar la carga de rutas para que al agregar una ruta ciudad1->ciudad2 50km también agregue la ruta ciudad2->ciudad1 50km.
