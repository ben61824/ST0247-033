class Bfa():

  """
  Implementacion de fuerza bruta
  (Brutal force algoritmo)
  """

  def __init__(self, conjunto="abc"):
  
    """
    Constructor

    :param conjunto: cadena que se utilizara en la implementacion
    """

    self.__conjunto = conjunto
 
  def subConjuntos(self, s):

    """
    esta funcion genera los posibles
    conjuntos de una cadena

    :param s: cadena a la que se le sacaran los conjuntos
    """

    self.subConjuntosAux("", s)
  
  def subConjuntosAux(self, respuesta, pregunta):  
  
    """
    Funcion recursion que 
    :return: un conjunto posible en cada iteracion
    """

    if len(pregunta) == 0:
      print(respuesta)
    else:
      self.subConjuntosAux(respuesta, pregunta[1:])  
      self.subConjuntosAux(respuesta+pregunta[0], pregunta[1:])  
  
  def permutaciones(self, s):

    """
    Funcion que genera las combinaciones posibles
    sin repetir letras que pueden salir de un conjunto
    """
    self.permutacionesAux("", s)
  
  def permutacionesAux(self, respuesta, pregunta):

    if len(pregunta) == 0:
      print(respuesta)
    
    else:
      for i in range(len(pregunta)):
        self.permutacionesAux(respuesta + pregunta[i], pregunta[0:i] + pregunta[i+1:])
