from rich import print
from rich.panel import Panel

class Produto:
   def __init__(self, nome="", preco=0.0):
      self.nome = nome
      self.preco = preco
   
   def etiqueta(self):
      precof = f'R${self.preco:,.2f}'
      print(Panel(f'[white]{self.nome.center(30)}\n{'-'*30}\n{precof.center(30, ".")}[/white]', title='Produto', style='green', width=34))


p1 = Produto("Caneta", 2.50)
p2 = Produto("Caderno", 15.00)

p1.etiqueta()
p2.etiqueta()
