from rich import print
from rich.panel import Panel

class Churrasco:
   def __init__(self, titulo='', pessoas=0):
      self.titulo = titulo
      self.pessoas = pessoas

   def analisar(self):
      # Consumo padrão: 400g por pessoa
      # Preço médio da carne: R$ 82.40 por kg
      qtd = self.pessoas * 0.4  # em kg
      preco = qtd * 82.40
      precoPessoa = preco / self.pessoas

      print(Panel(f'Analizando [green]{self.titulo}[/green] com [blue]{self.pessoas} convidados[/blue]\nRecomendo [blue]comprar {qtd:.3f}kg[/blue] de carne\nO custo total será de [green]R${preco:.2f}[/green]\nCada pessoa pagará [yellow]R${precoPessoa:.2f}[/yellow] para participar', title=self.titulo, width=60))



c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()
