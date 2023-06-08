from interpreter import draw
from chessPictures import *

# dibujamos knight junto a su negativo lo pocicinamos encima de su contraparte 
draw(knight.join(knight.negative()).up(knight.negative().join(knight)))
