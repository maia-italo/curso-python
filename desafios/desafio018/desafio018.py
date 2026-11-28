from rich import print
from rich.panel import Panel

class Churrasco:
   consumo:float = 0.4
   preco_kg:float = 82.4
   
   def __init__(self, titulo='', pessoas=0):
      self.titulo = titulo
      self.pessoas = pessoas

   def analisar(self):
      # Consumo padrão: 400g por pessoa
      # Preço médio da carne: R$ 82.40 por kg
      qtd = self.pessoas * Churrasco.consumo  # em kg
      preco = qtd * Churrasco.preco_kg
      precoPessoa = preco / self.pessoas

      conteudo = f'Analizando [green]{self.titulo}[/green] com [blue]{self.pessoas} convidados[/blue]'
      conteudo += f'\nCada participante comerá {Churrasco.consumo}Kg e cada Kg cuta R${Churrasco.preco_kg}'
      conteudo += f'\nRecomendo [blue]comprar {qtd:.3f}kg[/blue] de carne'
      conteudo += f'\nO custo total será de [green]R${preco:.2f}[/green]'
      conteudo += f'\nCada pessoa pagará [yellow]R${precoPessoa:.2f}[/yellow] para participar'

      print(Panel(conteudo, title=self.titulo, width=66))



c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()
