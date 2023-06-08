from interpreter import draw
from chessPictures import *

draw(knight.join(knight.negative()).up(knight.join(knight.negative()).verticalMirror()))

