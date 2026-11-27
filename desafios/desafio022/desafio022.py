from rich import print
from rich.panel import Panel
from os import system

class ControleRemoto:
   def __init__(self):
      self.power = False
      self.canal = 1
      self.volume = 2

   def main(self):
      system('clear')
      msg = ''

      if self.canal == 1:
         can = f'[white on yellow]1[/] 2 3 4 5'
      elif self.canal == 2:
         can = f'1 [white on yellow]2[/] 3 4 5'
      elif self.canal == 3:
         can = f'1 2 [white on yellow]3[/] 4 5'
      elif self.canal == 4:
         can = f'1 2 3 [white on yellow]4[/] 5'
      elif self.canal == 5:
         can = f'1 2 3 4 [white on yellow]5[/]'


      if self.volume == 1:
         vol = f'[white on green]  [/white on green][black on white]        [/black on white]'
      elif self.volume == 2:
         vol = f'[white on green]    [/white on green][black on white]      [/black on white]'
      elif self.volume == 3:
         vol = f'[white on green]      [/white on green][black on white]    [/black on white]'
      elif self.volume == 4:
         vol = f'[white on green]        [/white on green][black on white]  [/black on white]'
      elif self.volume == 5:
         vol = f'[white on green]          [/white on green][black on white][/black on white]'


      if self.power == False:
         msg = f'[red]A TV está desligada'
      elif self.power == True:
         msg = f'CANAL = {can}\nVOLUME = {vol}'


      tv = Panel(msg, title='[ TV ]', width=60)
      print(tv)

      comando = input(f'< CH{self.canal} >  - VOL{self.volume} +  ')

      if comando == '<':
         if self.canal == 1:
            self.canal = 5
         else:
            self.canal -= 1
      elif comando == '>':
         if self.canal == 5:
            self.canal = 1
         else:
            self.canal += 1
      
      elif comando == '-':
         if self.volume == 1:
            pass
         else:
            self.volume -= 1
      elif comando == '+':
         if self.volume == 5:
            pass
         else:
            self.volume += 1
      elif comando == '@':
         if self.power == True:
            self.power = False
         elif self.power == False:
            self.power = True
      else:
         print('Comando inválido!')



controle = ControleRemoto()
while True:
   controle.main()
