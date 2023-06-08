from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = self.img[::-1]

    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []

    for line in self.img:
      newLine = ""
      for i in line:
        newLine += self._invColor(i)
      negative.append(newLine)
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    joinImg = []

    for line in range(len(self.img)):
      joinImg.append(self.img[line]+p.img[line])

    return Picture(joinImg)

  def up(self, p):
    """Devuelve una nueva figura poniendo la figura p debajo de
       la figura actual """
    upImg = self.img + p.img
    return Picture(upImg)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    underImg = p.img + self.img
    return Picture(underImg)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeat = []
    for line in self.img:
      repeat.append(line*n)
    return Picture(repeat)

  def verticalRepeat(self, n):
    repeat = self.img * n
    return Picture(repeat)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

