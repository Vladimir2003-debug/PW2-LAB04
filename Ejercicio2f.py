from interpreter import draw
from chessPictures import *

# Dibujamos una linea de cuadrados
line = square.join(square.negative()).horizontalRepeat(4)
# Luego lo ponemos encima de su negativo y lo repetimos 2 veces
draw(line.up(line.negative()).verticalRepeat(2))