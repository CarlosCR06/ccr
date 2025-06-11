# Archivo: Estudiante.py

"""
Clase Estudiante.
Representa a un estudiante con atributos básicos como NIF, curso, nombre y apellidos.

Atributos de clase:
- nif (str): Identificador único del estudiante.
- curso (str): Curso en el que está inscrito el estudiante.
- nombre (str): Nombre del estudiante.
- apellidos (str): Apellidos del estudiante.

:author: Roberto Cano Estévez
:date: 2025-04-27
"""

class Estudiante:
    """
    Clase que modela un estudiante.
    """

    nif = "11111111Z"
    curso = "Primaria"
    nombre = "Nombre"
    apellidos = "Apellidos"

    def __init__(self, nif: str, curso: str, nombre: str, apellidos: str):
        """
        Constructor de la clase Estudiante.

        :param nif: Identificador único del estudiante.
        :param curso: Curso en el que está inscrito el estudiante.
        :param nombre: Nombre del estudiante.
        :param apellidos: Apellidos del estudiante.
        """
        self.nif = nif
        self.curso = curso
        self.nombre = nombre
        self.apellidos = apellidos

    @property
    def nif(self) -> str:
        """
        Obtiene el NIF del estudiante.

        :return: El NIF del estudiante.
        """
        return self.__nif

    @nif.setter
    def nif(self, value: str):
        """
        Establece el NIF del estudiante.

        :param value: El nuevo NIF del estudiante.
        """
        self.__nif = value

    @property
    def curso(self) -> str:
        """
        Obtiene el curso del estudiante.

        :return: El curso del estudiante.
        """
        return self.__curso

    @curso.setter
    def curso(self, value: str):
        """
        Establece el curso del estudiante.

        :param value: El nuevo curso del estudiante.
        """
        self.__curso = value

    @property
    def nombre(self) -> str:
        """
        Obtiene el nombre del estudiante.

        :return: El nombre del estudiante.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str):
        """
        Establece el nombre del estudiante.

        :param value: El nuevo nombre del estudiante.
        """
        self.__nombre = value

    @property
    def apellidos(self) -> str:
        """
        Obtiene los apellidos del estudiante.

        :return: Los apellidos del estudiante.
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value: str):
        """
        Establece los apellidos del estudiante.

        :param value: Los nuevos apellidos del estudiante.
        """
        self.__apellidos = value
<<<<<<< HEAD
=======
        
    def __str__(self) -> str:
        return f"Estudiante: {self.nombre} {self.apellidos}, NIF: {self.nif}, Curso: {self.curso}"    
>>>>>>> 7025416 (FIX #1 Añadiendo metodo str a Estudiante)
