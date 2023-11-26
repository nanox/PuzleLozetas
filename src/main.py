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

import sys
from reader import read
from reachablegoal import findm
from reachablegoal import findx
from reachablegoal import sumall
from reachablegoal import reachablegoal
from boardgenerator import random_board
from branchandbound import branchandbound


if __name__ == "__main__":

    print("#####################################\n")
    print("Puzle de las Lozetas (n-puzzle)\n")
    print("#####################################\n")
    
    CYAN = "\033[96m"
    RED = "\033[91m"
    END = "\033[0m"

    # Lea el archivo si se le da, de lo contrario use un tablero aleatorio
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]
        try:
            board = read(FILENAME)
        except FileNotFoundError:
            print("Archivo no encontrado o path incorrecto.")
            sys.exit(1)
    else:
        board = random_board()

    # Tablero inicial de salida
    print("Orden inicial:")
    board.print()

    # Salida kurang(i) de la placa inicial
    time_elapsed, kurang = findm(board)
    print("Puntaje Kurang(i):")
    for key in sorted(kurang):
        print(f"{key}: {kurang[key]}")
    print()

    # Muestra la suma de todos los valores en kurang(i) + x
    sums = sumall(kurang, findx(board))
    print(f"Sigma m(i) + x: {sums}\n")

    # Realiza ramificacion y poda si el tablero se puede resolver;
    # de lo contrario, imprima un mensaje de error
    TIMEELAPSED_BNB = 0
    NODECOUNT = 0
    if not reachablegoal(sums):
        print(f"{RED}No se puede resolver.\n{END}")
    else:
        TIMEELAPSED_BNB, NODECOUNT = branchandbound(board)

    # Tiempo de salida tomado y número de nodos generados
    print(CYAN, end="")
    print(f"Tiempo requerido: {time_elapsed+TIMEELAPSED_BNB:0.4f} segs.")
    print(f"Número de nodos generados: {NODECOUNT}")
    print(END, end="")
