# Proyecto Final de Programación 2

## Objetivo
Desarrollo de una plataforma de turismo nacional utilizando Django, aplicando conceptos aprendidos durante la materia como: 
- Programación orientada a objetos
- Estructuras de datos
- Árboles binarios
- Grafos
- Complejidad de algoritmos

## Objetivos específicos
- Carga de datos de las ciudades con información turística relevante.
- Implementación del algoritmo de Dijkstra para encontrar la ruta más corta entre dos ciudades.
- Utilización de árboles binarios de búsqueda (BST) para ordenar la lista de ciudades antes de pasar los datos al frontend.

## Instrucciones de instalación

1. Clonar el repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_PROYECTO>
    ```

2. Crear y activar un entorno virtual:
    ```bash
    python3 -m venv .venv # En Windows: python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```

3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplicar las migraciones:
    ```bash
    cd gps_simulation
    python manage.py migrate
    ```

5. Crear usuario y contraseña para el admin: 
    ```bash
    python manage.py createsuperuser
    ```

6. Iniciar el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

7. Acceder al administrador de Django en `http://localhost:8000/admin` para cargar las ciudades.

## Estructura del Proyecto

El proyecto sigue la estructura estándar de Django:

```
/gps_simulation/
    /routes/
        models.py   # Modelos del proyecto
        views.py    # Lógica de las vistas
        urls.py     # Rutas del proyecto
        templates/  # Templates HTML
    /static/
        css/        # Archivos de estilo
    settings.py     # Configuraciones del proyecto
```

## Funcionalidades Implementadas

- **Carga de ciudades**: Utilizando el administrador de Django, se puede ingresar información sobre las ciudades.
- **Carga de runtas**: Utilizando el administrador de Django, tambien se permite la carga a traves de la url /load para cargar cosas rapidos, se tiene que poner todas las rutas en el formato "id_ciudad1 id_ciudad2 distancia" si los id de ciudades no existen falla.
  
## Funcionalidades a Implementar

Los estudiantes deberán completar:
1. **Agregar información sobre las ciudades**: Moddificar el modelo de ciudades apra cargar información relevante para el turismo de la provincia
2. **Árboles Binarios de Búsqueda**: Comentar todos los metodos del arbol binario de busqueda explicando apra que sirven y como funcionan.
3. **Algoritmo de Dijkstra**: Implementar desde cero el algoritmo para encontrar la ruta más corta entre dos ciudades. La entrada serán las ciudades cargadas previamente, y la salida, la ruta óptima y la distancia.

### Notas Importantes

- **Carga de datos**: Se realiza desde el administrador de Django, y los datos de las rutas deben cargarse después de registrar las ciudades.
- **Frontend**: Los docentes proporcionarán el diseño del frontend, los estudiantes deben centrarse en la lógica del backend.

## Testing

El proyecto utiliza las herramientas de testing de Django. Para ejecutar los tests:

```bash
python manage.py test
```

Asegúrate de que todas las pruebas pasen antes de realizar una entrega.

## Sugerencias para la Implementación

- Para agrgar la informacion de las ciudades van a tener que modificar la clase City en el archivo models.py y luego hacer la migracion para que impacten los cambios en la base de datos. Luego van a tener que modificar el template city_detail.html para mostrar la información nueva.
- Lean y comenten la clase ABB que esta en el archivo utils.py, estudien la implementacion completa que despues la van a tener que defender.
- Para calcular las rutas van a tener que implementar la función def dijkstra(start_city) y def get_shortest_path(start_city, end_city) en el archivo utils.py

## Cronograma:
4 entregas y la defensa

### Entrega 1: Resumen de proyecto
Llenar formulario con:
+ Miembros del grupo
+ nombre del grupo
+ descripción del proyecto
+ funcionalidades

### Entrega 2: Entrega preliminar:
+ poner una etiqueta al git v0.0.1
+ Documento contando que se tiene y que falta implementar (estado de situación del proyecto)
- que anda
- que no anda
- que falta implementar

### Entrega 3: Código fuente y documentación del proyecto
- Codigo fuente
- Comentarios en el código
- Decisiones de diseño y analisis de complejidad

### Entrega 4 : Video
- Video de 10 minutos presentando el proyecto (link al video)
* opcional entregar presentacion si usan durante el video

### Defensa orales

# Recomentaciones para la implementación:
Entrega 1
- Usar el programa Agenda entenderla y documentarla (ponerles comentarios que expliquen que hace)
- Diseñar el programa de usteedes en base a los visto en la clase Agenda (clases y metodos necesarios)
- Entregar el borrador de proyecto

Entrega 2
- Armar el esqueleto de las clases que necesitan
- primero las clases mas sencillas del tipo de dato especifico y despues la de administracion (ej primero contacto y después agenda)
- ir usando el archivo test para ir probando el funcionamiento, pueden hacer un archivo de test por clase tambien

Entrega 3
- agregar descripcion de cada clase y metodo
- agregar los test de cada metodo
- corregir lo que no este funcionando
- modificar el menu para agregar nuevas funcionalidades

Entrega 4:
- armar una presentacion con una diapositiva por cada uno de los puntos mencionados
- repartir aprtes
- ensayar la presentacion y medir el tiempo
- grabar la presentacion con un meet y grabando la pantalla, por ejemplo con obs o vokoscreen

## Criterios de Evaluación

1. Claridad y comentarios en el código.
2. Manejo de errores y excepciones.
3. Trabajo en equipo.
4. Implementación de tests unitarios.
5. Presentación oral del proyecto.
6. Preguntas teóricas sobre lo implementado.

# Puntos extras
+ modificar la carga de rutas para que al agregar una ruta ciudad1->ciudad2 50km también agregue la ruta ciudad2->ciudad1 50km
+ modificar el pryecto apra que puedan cargarse una foto de la ciudad y mostrarla en la página de la ciudad (ver manejo de archivos estaticos publicos en django)
