class Vehiculos():
  #Constructor
  def _init__(self, marca, modelo):
      self.marca=marca
      self.modelo=modelo
      self.enmarcha=False
      self.acelera=False
      self.frena=False
      
  def arrancar(self):
    self.enmarcha=True
    
  def acelerar(self):
    self.acelera=True
    
  def frena(self):
    self.frena=True
    
  #es el mensaje que ma a mostrar si quiero saber si el vehiculo indique el estado.
  def estado(self):
      print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Moto(Vehiculos):
  pass

miMoto=Moto("Honda", "CBR")
miMoto.estado()
