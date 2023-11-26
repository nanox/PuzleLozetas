#!/usr/bin/env python

"""
Algoritmo de Puzle de las Losetas con Ramificación y Poda
https://en.wikipedia.org/wiki/15_puzzle
https://en.wikipedia.org/wiki/Branch_and_bound
"""
__author__ = "Jose Leonardo Alvarez Lopez"
__contact__ = "joseleonardo.alvarez696@comunidadunir.net"
__copyright__ = "Copyright 2023, UNIR"
__credits__ = ["Fundación Universitaria UNIR Colombia"]
__date__ = "2023/11/20"
__email__ = "jalvarez82@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "nanox"
__status__ = "alpha"
__version__ = "1.0.0"


class Board:
    """ Una clase que representa un tablero de 15 lozetas """

    # Atributos:
    # blocks: matriz de enteros que representa las lozetas en el tablero
    # steps: entero que representa los pasos dados para llegar a la solución
    # prevstep: objeto que representa el paso anterior dado
    # misplacedblocks: entero que representa el num lozetas fuera de lugar

    def __init__(self, blocks, steps):
        self.steps = steps
        self.blocks = blocks
        self.prevstep = None
        self.misplacedblocks = self.count_misplaced()

    def copy(self):
        """ devuelve una copia del tablero y agrega un paso """
        return Board(self.blocks[:], self.steps + 1)

    def print(self):
        """ imprime el tablero """
        for i in range(4):
            for j in range(4):
                if self.blocks[i * 4 + j] < 10:
                    print(f"0{self.blocks[i*4+j]}", end=" ")
                elif self.blocks[i * 4 + j] == 16:
                    print("--", end=" ")
                else:
                    print(self.blocks[i * 4 + j], end=" ")
            print()
        print()

    def empty_block(self):
        """ devuelve el índice de lozeta vacía en el tablero """
        for i in range(16):
            if self.blocks[i] == 16:
                return i
        return 0

    def swap(self, i, j):
        """ devuelve una copia del tablero con las lozetas intercambiadas """
        result = self.copy()
        result.prevstep = self
        temp = result.blocks[i]
        result.blocks[i] = result.blocks[j]
        result.blocks[j] = temp
        result.misplacedblocks = result.count_misplaced()
        return result

    def move_up(self):
        """
        devuelve una copia del tablero con la lozeta vacía
        intercambiado con la lozeta de arriba """
        if self.empty_block() < 4:
            return None
        else:
            return self.swap(self.empty_block() - 4, self.empty_block())

    def move_down(self):
        """ devuelve una copia del tablero con la lozeta vacío
        intercambiado con la lozeta debajo de esta. """
        if self.empty_block() > 11:
            return None
        else:
            down = self.swap(self.empty_block() + 4, self.empty_block())
            return down

    def move_left(self):
        """ devuelve una copia del tablero con la lozeta vacío
        intercambiado con la lozeta a la izquierda. """
        if self.empty_block() % 4 == 0:
            return None
        else:
            left = self.swap(self.empty_block() - 1, self.empty_block())
            return left

    def move_right(self):
        """ devuelve una copia del tablero con la lozeta vacío
        intercambiado con la lozeta a la derecha """
        if self.empty_block() % 4 == 3:
            return None
        else:
            return self.swap(self.empty_block() + 1, self.empty_block())

    def count_misplaced(self):
        """ devuelve el número de lozetas
        fuera de lugar en el tablero """
        misplaced = 0
        for i in range(16):
            if self.blocks[i] != 16 and self.blocks[i] != i + 1:
                misplaced += 1
        return misplaced

    def is_goal(self):
        """ devuelve True si la configuracion objetiva se alcanzó,
        False de lo contrario """
        return self.misplacedblocks == 0

    def cost(self):
        """ devuelve el costo del tablero """
        return self.steps + self.misplacedblocks

    def __lt__(self, other):
        """ devuelve True si el tablero tiene un costo menor
        que el otro tablero, False en caso contrario """
        if self.steps < other.steps:
            cost = self
        else:
            cost = other
        return cost
