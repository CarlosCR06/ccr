# File: Gato.py

"""
Clase Gato.
Este módulo contiene la definición de la clase Gato, que modela el comportamiento básico de un gato.

:author: Roberto Cano Estévez
:date: 2025-04-27
"""

class Gato:
    """
    Clase que modela el comportamiento de un gato.
    """

    def __init__(self, nombre: str):
        """
        Constructor de la clase Gato.

        :param nombre: Nombre del gato.
        """
        self.nombre = nombre

    def maullar(self):
        """
        Método que imprime el sonido característico de un gato.
        """
        print(f"{self.nombre} dice: Miau")

    