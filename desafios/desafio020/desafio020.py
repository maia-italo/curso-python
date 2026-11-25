from rich import print
from rich.panel import Panel


class Gamer:
   def __init__(self, nome='', nick=''):
      self.nome = nome
      self.nick = nick
   
   def add_favoritos(self, jogo=''):
      self.jogos = []
      self.jogos.append(jogo)

   def ficha(self):
      self.lista = self.jogos.sort()
      self.ficha = Panel(f'Nome real: [background = blue][black]{self.nome}[/black]\nJogos favoritos:\n{self.lista}', title=f'Jogador <{self.nick}>', width=60)
      print(self.ficha)



j1 = Gamer('Fabricio da Silva', 'detonator2025')
j1.add_favoritos('Mario Bros.')
j1.add_favoritos('Sonic')
j1.add_favoritos('God of War')
j1.add_favoritos('Fortnite')
j1.ficha()

j2 = Gamer('Olívia Souza', 'peach_raivosa')
j2.add_favoritos('Mario Bros.')
j2.add_favoritos('Call of Duty')
j2.ficha()
