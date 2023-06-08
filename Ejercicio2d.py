from interpreter import draw
from chessPictures import *

# Juntamos un cuadrado con su negativo y lo repetimos 4 veces
draw(square.join(square.negative()).horizontalRepeat(4))