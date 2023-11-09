# PuzleLozetas
Algoritmo que resuelve el problema del Puzle de las Lozetas aplicando Ramificación y Poda

El puzle de las losetas o rompecabezas de 15 (también llamado Gem Puzzle, Boss Puzzle, Game of Fifteen, Mystic Square y muchos otros) es un rompecabezas deslizante que tiene 15 mosaicos cuadrados numerados del 1 al 15 en un marco de 4 mosaicos de alto y 4 mosaicos de ancho, dejando uno desocupado posición de mosaico. Los mosaicos en la misma fila o columna de la posición abierta se pueden mover deslizándolos horizontal o verticalmente, respectivamente. El objetivo del rompecabezas es colocar las fichas en orden numérico

El programa acepta una configuración inicial de un tablero de 15 rompecabezas y determina si es solucionable o no. Si es solucionable, entonces procede a ejecutar el algoritmo de ramificación y poda para encontrar una solución. 
Se necesita tener instalado Python3 para ejecutar este programa.
El archivo de entrada debe ser en formato plano (txt) que contiene una matriz de 4x4 de la configuración inicial de la placa. Cada elemento/bloque está separado por un espacio, y el bloque vacío puede representarse con '0', '-', '--' o '16'.
Ejemplos de formato correcto:
```
05 01 03 04 		1   2  3  4 		6   5  2  4
09 02 07 08 		0   5  6  8 		9   1  3  8
-- 06 15 11 		9  10  7 11 		10  -  7 15
13 10 14 12 		13 14 15 12 		13 14 12 11
```
