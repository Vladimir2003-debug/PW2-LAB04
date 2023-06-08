from interpreter import draw
from chessPictures import *

# Images adicionales
sqRock = square.negative().under(rock) 
sqKnight = square.under(knight)
sqBishop = square.negative().under(bishop) 
sqQueen = square.under(queen)
sqKing = square.negative().under(king) 
sqBishop2 = square.under(bishop)
sqKnight2 = square.negative().under(knight) 
sqRock2 = square.under(rock)

# Esta linea de piezas se ubicaran en la parte inferior 
linePieces = sqRock.join(sqKnight).join(sqBishop).join(sqQueen).join(sqKing).join(sqBishop2).join(sqKnight2).join(sqRock2)
# Una linea de peones
linePawns = square.under(pawn).join(square.negative().under(pawn)).horizontalRepeat(4)
# La tabla que va al medio de la tabla sin piezas
lineTable = square.join(square.negative()).horizontalRepeat(4)
table = lineTable.up(lineTable.negative()).verticalRepeat(2)
# La parte de las negras es el negativo de la parte blanca tanto linea de peones como de piezas
# todo se junta y se muestra
draw(linePieces.negative().img + linePawns.negative().img + table.img + linePawns.img + linePieces.img)