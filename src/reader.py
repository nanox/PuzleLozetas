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

from board import Board


def read(filename):
    """ función que lee un tablero de un archivo y retorna objeto Board """

    # Leer archivo
    with open(filename, "r", encoding="utf8") as file:
        data = file.read()

    board = []  # Inicializa el tablero

    # Procesando datos
    data = data.split("\n")
    for i in range(4):
        data[i] = data[i].split(" ")
        for j in range(4):
            curr = data[i][j]
            # Bloque vacío se convierte en 16
            if curr in {"-", "0", "--"}:
                board.append(16)
            else:
                board.append(int(curr))

    # Creación de un objeto Board
    return Board(board, 0)
