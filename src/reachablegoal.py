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

from time import perf_counter


def findm(board):
    """ devuelve el número de lozetas que están fuera de lugar """
    timestart = perf_counter()  # Iniciar el temporizador
    board_copy = board.blocks[:]  # Copia la config de los lozetas del tablero
    kurang = {}  # Iniciar el diccionario
    for i in range(16):
        curr = (board_copy[i])
        kurang[curr] = 0
        for j in range(i + 1, 16):
            if curr > (board_copy[j]):
                kurang[curr] += 1
    timeend = perf_counter()  # Detener el temporizador
    return timeend-timestart, kurang


def findx(board):
    """ recibe la matrix (tablero) y retorna el valor para x (0 o 1) """
    idx = board.empty_block()  # encontrar el índice de la lozeta vacía
    return (idx // 4 + idx % 4) % 2  # 0 si es par, 1 si es impar


def sumall(kurang, x_val):
    """ devuelve la suma de todos los valores en m(i) + x """
    sum_kurang = sum(kurang.values())
    return sum_kurang + x_val


def reachablegoal(sum_all):
    """ devuelve True si es par, False en caso contrario """
    return (sum_all) % 2 == 0
