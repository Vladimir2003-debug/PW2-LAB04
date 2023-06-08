from interpreter import draw
from chessPictures import *

# Hacemos casi lo mismo que el Ejercicio 2b pero a la parte de abajo lo giramos
draw(knight.join(knight.negative()).up(knight.join(knight.negative()).verticalMirror()))

