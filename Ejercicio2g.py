from interpreter import draw
from chessPictures import *


sqRock = square.negative().under(rock) 
sqKnight = square.under(knight)
sqBishop = square.negative().under(bishop) 
sqQueen = square.under(queen)
sqKing = square.negative().under(king) 
sqBishop2 = square.under(bishop)
sqKnight2 = square.negative().under(knight) 
sqRock2 = square.under(rock)

linePieces = sqRock.join(sqKnight).join(sqBishop).join(sqQueen).join(sqKing).join(sqBishop2).join(sqKnight2).join(sqRock2)

linePawns = square.under(pawn).join(square.negative().under(pawn)).horizontalRepeat(4)

lineTable = square.join(square.negative()).horizontalRepeat(4)

table = lineTable.up(lineTable.negative()).verticalRepeat(2)

draw(linePieces.negative().img + linePawns.negative().img + table.img + linePawns.img + linePieces.img)