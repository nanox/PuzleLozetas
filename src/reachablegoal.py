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

from time import perf_counter


def findm(board):
    """ Una función que devuelve el número de bloques que están fuera de lugar
    El tablero se representa como una matriz de cadenas
    La función devolverá un diccionario """
    timestart = perf_counter()  # Iniciar el temporizador
    board_copy = board.blocks[:]  # Copia la config de los bloques del tablero
    kurang = {}  # Iniciar el diccionario
    for i in range(16):
        curr = (board_copy[i])
        kurang[curr] = 0
        for j in range(i+1, 16):
            if curr > (board_copy[j]):
                kurang[curr] += 1
    timeend = perf_counter()  # Terminar el temporizador
    return timeend-timestart, kurang


def findx(board):
    """ La función findx recibe una matrix (tablero)
    y devuelve el valor de X (0 o 1) """
    idx = board.empty_block()  # encontrar el índice del bloque vacío
    return (idx//4 + idx % 4) % 2  # 0 si es par, 1 si es impar


def sumall(kurang, x_val):
    """ La función sumall recibe el valor de findkurang y x_val
    y devuelve la suma de todos los valores en kurang + x_val """
    sum_kurang = sum(kurang.values())
    return sum_kurang + x_val


def reachablegoal(sum_all):
    """ La función reachablegoal(sumall) recibe el valor de la suma de todos
    los valores en findkurang + X y devuelve True si es par,
    False en caso contrario """
    return (sum_all) % 2 == 0
