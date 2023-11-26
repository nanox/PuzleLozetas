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

import random
from board import Board


def random_board():
    """ devuelve un tablero aleatorio de 15 rompecabezas """
    # Inicializa las lozetas
    blocks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    random.shuffle(blocks)  # Barajar las lozetas
    board = Board(blocks, 0)  # Crea el objeto Board
    return board
