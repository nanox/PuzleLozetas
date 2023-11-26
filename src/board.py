#!/usr/bin/env python

"""
Puzle de las Losetas con Ramificación y Poda
https://en.wikipedia.org/wiki/15_puzzle
https://en.wikipedia.org/wiki/Branch_and_bound
"""
__author__ = "Jose Leonardo Alvarez Lopez"
__contact__ = "joseleonardo.alvarez696@comunidadunir.net"
__copyright__ = "Copyright 2022, UNIR"
__credits__ = ["Fundación Universitaria UNIR Colombia"]
__date__ = "2022/11/28"
__email__ = "jalvarez82@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "jalvarez82"
__status__ = "Devel"
__version__ = "1.0.0"


class Board:
    """ Una clase que representa un tablero de 15 rompecabezas """

    # Atributos:
    # blocks: una matriz de enteros que representan los bloques en el tablero
    # steps: un entero que representa los pasos dados para llegar al tablero
    # prevstep: un objeto que representa el paso anterior dado
    # misplacedblocks: #entero que representa los bloques fuera de lugar

    def __init__(self, blocks, steps):
        self.steps = steps
        self.blocks = blocks
        self.prevstep = None
        self.misplacedblocks = self.count_misplaced()

    def copy(self):
        """ una función que devuelve una copia del tablero y agrega un paso """
        return Board(self.blocks[:], self.steps+1)

    def print(self):
        """ una función que imprime el tablero """
        for i in range(4):
            for j in range(4):
                if self.blocks[i*4+j] < 10:
                    print(f"0{self.blocks[i*4+j]}", end=" ")
                elif self.blocks[i*4+j] == 16:
                    print("--", end=" ")
                else:
                    print(self.blocks[i*4+j], end=" ")
            print()
        print()

    def empty_block(self):
        """ una función que devuelve el índice de bloque vacío en tablero """
        for i in range(16):
            if self.blocks[i] == 16:
                return i

    def swap(self, i, j):
        """ una función que devuelve una copia del tablero con
        bloques intercambiados """
        result = self.copy()
        result.prevstep = self
        temp = result.blocks[i]
        result.blocks[i] = result.blocks[j]
        result.blocks[j] = temp
        result.misplacedblocks = result.count_misplaced()
        return result

    def move_up(self):
        """
        una función que devuelve una copia del tablero con el bloque vacío
        intercambiado con el bloque de arriba """
        if self.empty_block() < 4:
            return None
        else:
            return self.swap(self.empty_block()-4, self.empty_block())

    def move_down(self):
        """ una función que devuelve una copia del tablero con el bloque vacío
        intercambiado con el bloque debajo de él. """
        if self.empty_block() > 11:
            return None
        else:
            down = self.swap(self.empty_block()+4, self.empty_block())
            return down

    def move_left(self):
        """ una función que devuelve una copia del tablero con el bloque vacío
        intercambiado con el bloque a la izquierda. """
        if self.empty_block() % 4 == 0:
            return None
        else:
            left = self.swap(self.empty_block()-1, self.empty_block())
            return left

    def move_right(self):
        """ una función que devuelve una copia del tablero con el bloque vacío
        intercambiado con el bloque a la derecha """
        if self.empty_block() % 4 == 3:
            return None
        else:
            return self.swap(self.empty_block()+1, self.empty_block())

    def count_misplaced(self):
        """ una función que devuelve el número de bloques
        fuera de lugar en el tablero """
        misplaced = 0
        for i in range(16):
            if self.blocks[i] != 16 and self.blocks[i] != i+1:
                misplaced += 1
        return misplaced

    def is_goal(self):
        """ una función que devuelve True si el tablero es un tablero de meta,
        False de lo contrario """
        return self.misplacedblocks == 0

    def cost(self):
        """ una función que devuelve el costo del tablero """
        return self.steps+self.misplacedblocks

    def __lt__(self, other):
        """ una función que devuelve True si el tablero tiene un costo menor
        que el otro tablero, False en caso contrario """
        if self.steps < other.steps:
            return self
        else:
            return other
