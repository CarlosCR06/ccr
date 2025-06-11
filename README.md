[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7HRTZu-P)
# Reentrega examen Git: Control de versiones


1.  Clona este repositorio y sigue estas instrucciones del README. Se adjuntan códigos en Python.
   
2.  Entrega la url en el moodle y sincroniza el repositorio local con este. Trabajarás con los comandos git desde  **gitBash** y con el flujo de trabajo **GitFlow**. Comienza creando la rama "develop" a partir de la `main`. Trabajarás en ella los cambios del código.

## Feature. Añade método a Estudiante.

1. Crea un issue para añadir el siguiente método a la clase Estudiante
   - Créalo referenciando a la **línea del código** a la que afecta. 
   - Crea una etiqueta nueva y etiqueta el issue. 
   - Usa las menciones para que me llegue una notificación.

```python
def __str__(self) -> str:
    return f"Estudiante: {self.nombre} {self.apellidos}, NIF: {self.nif}, Curso: {self.curso}"    
```
2. Crea la **rama "feat-add-str-method-to-estudiante"** a partir de la rama "develop". 
   
3. Realiza un commit con el mensaje adecuado que cierre el issue directamente desde el mensaje.

4. Fusiona en la rama "develop" 
5. Entrega aquí un pantallazo con los comandos en GitBash.
6. Entrega aquí un pantallazo con el comando en GitBash donde muestres todos los commits hasta el momento.


## Refactorizar. Nombre del autor.


1. Crea la **rama "refactor-update-author-name"** a partir de la rama "develop". Trabajarás en ella para cambiar el nombre del autor.
2. Crea dos issues para cambiar el autor en los ficheros Gato.py y Estudiante.py. 
   - Créalos referenciando a la **línea del código** a la que afecta. 
   - Etiqueta el issue con la **etiqueta** adecuada. 
   - Usa las menciones para que me llegue una notificación.
3. Cierra ambos issues directamente desde el mismo mensaje del commit.
4. Fusiona en la rama "develop" 
5. Entrega aquí un pantallazo con los comandos en GitBash.
6. Entrega aquí un pantallazo con el comando en GitBash donde muestres todos los commits hasta el momento.


## Documentación. Documenta el método.
16. Este apartado lo harás íntegramente desde Visual Studio Code, y no con los comandos desde GitBash
17. Crea la **rama "documentation"** a partir de la rama "develop". Trabajarás en ella la documentación. Entrega aquí el pantallazo de Visual Studio Code.
18. Crea otro issue para comentar el método añadido a Esdudiante. 

- Créalo referenciando a la **línea del código** a la que afecta. 
- Etiqueta el issue con la **etiqueta** adecuada. 
- Usa las menciones para que me llegue una notificación.

19. El método comentado quedaría así.

```python
def __str__(self) -> str:
        """
        Método que devuelve una representación en cadena del estudiante.

        :return: Una cadena con la información del estudiante.
        """
        return f"Estudiante: {self.nombre} {self.apellidos}, NIF: {self.nif}, Curso: {self.curso}"
        
```

1.  Realiza un commit con el mensaje adecuado que cierre el issue directamente desde el mensaje. Entrega aquí el pantallazo de Visual Studio Code.
2.  Muestra la diferencia mediante `git diff`. Entrega aquí el pantallazo de Visual Studio Code.
3.  Fusiona la rama "documentation" en la rama "develop". Entrega aquí el pantallazo de Visual Studio Code.
4.  Fusiona la rama "develop" en la rama main. Entrega aquí el pantallazo de Visual Studio Code.

## GitHub Pages

23. Sube el repositorio a GitHub (Añade aquí la url) y activa el hosting (GitHub Pages)(Añade aquí la url). Selecciona la carpeta docs como inicio. Debe visualizarse tu nombre en un `<h1>` y tus apellidos en un  `<h2>` 

## BitBucket

24. Crea en tu servidor Bitbucket una copia del repositorio actual. Añade aquí la url para que al menos yo pueda verla (mlmagarin@iesgrancapitan.org). El mismo repositorio ha de estar en ambos servidores, y deben verse todas las ramas.
25.  Entrega aquí un pantallazo con los commits y ramas del repositorio