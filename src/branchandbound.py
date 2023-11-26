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

from queue import PriorityQueue
from time import perf_counter


def branchandbound(board):
    """ La función BranchAndBound acepta el tablero inicial,
    imprime los pasos dados para alcanzar la meta,
    y devuelve el tiempo empleado y el número de nodos generados. """

    # Para formateo jeje, no preocuparse por esto :P
    green = "\033[92m"
    cyan = "\033[96m"
    red = "\033[91m"
    upper = "\033[4m"
    bold = "\033[1m"
    end = "\033[0m"

    timestart = perf_counter()  # Temporizador de inicio

    # Inicializar variables
    nodecount = 0  # Número de nodos generados
    livenodes = PriorityQueue()  # PriorityQueue para nodos activos
    livenodes.put((board.cost(), board))
    curr = board
    checked = {str(curr.blocks): True}  # Diccionario para nodos marcados

    # Iterar a través de livenodes hasta que se alcance el objetivo
    # o se verifiquen todos los nodos
    while (not curr.is_goal()) and (not livenodes.empty()):
        # Tome el nodo con el costo más bajo de livenodes
        curr = livenodes.get()[1]
        # Agregar el nodo actual a los nodos marcados
        checked[str(curr.blocks)] = True

        # Para cada nodo, intercambiar bloques vacíos hacia arriba, abajo,
        # izquierda, derecha y agregue el tablero intercambiado a livenodes
        # si aún no está marcado
        up = curr.move_up()
        if (up is not None) and (str(up.blocks) not in checked):
            livenodes.put((up.cost(), up))
            checked[str(up.blocks)] = True
            nodecount += 1

        down = curr.move_down()
        if (down is not None) and (str(down.blocks) not in checked):
            livenodes.put((down.cost(), down))
            checked[str(down.blocks)] = True
            nodecount += 1

        left = curr.move_left()
        if (left is not None) and (str(left.blocks) not in checked):
            livenodes.put((left.cost(), left))
            checked[str(left.blocks)] = True
            nodecount += 1

        right = curr.move_right()
        if (right is not None) and (str(right.blocks) not in checked):
            livenodes.put((right.cost(), right))
            checked[str(right.blocks)] = True
            nodecount += 1
    # Se alcanza la meta

    timeend = perf_counter()  # Fin del temporizador

    # Resumen de ejecucion
    if curr.steps == 0:
        print(f"{red}{bold}Bueno, el rompecabezas está terminado. >:(\n{end}{end}")
    else:
        print(f"{green}{bold}Completado satisfactoriamente!{end}{end}\n")
        stepstosuccess = []
        currstep = curr

        while currstep.prevstep is not None:
            stepstosuccess.append(currstep)
            currstep = currstep.prevstep

        print(f"{upper}Al principio era así:{end}")
        board.print()

        for i in range(len(stepstosuccess)-1, -1, -1):
            print(f"{upper}Paso #{len(stepstosuccess)-i}:{end}")
            stepstosuccess[i].print()

        print(f"{cyan}Pasos requeridos: {curr.steps}{end}")

    return (timeend-timestart, nodecount)
