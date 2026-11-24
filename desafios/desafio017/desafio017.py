from rich import print
from rich.panel import Panel

class Produto:
   def __init__(self, nome="", preco=0.0):
      self.nome = nome
      self.preco = preco
   
   def etiqueta(self):
      print(Panel(f'[white]{self.nome:26}\n{'-'*26}\nR${self.preco:23.2f}[/white]', title='Produto', style='green', width=30))


p1 = Produto("Caneta", 2.50)
p2 = Produto("Caderno", 15.00)

p1.etiqueta()
p2.etiqueta()
