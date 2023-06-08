from interpreter import draw
from chessPictures import *

line = square.join(square.negative()).horizontalRepeat(4)

draw(line.up(line.negative()).verticalRepeat(2))