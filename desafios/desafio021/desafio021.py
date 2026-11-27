from rich import print


class Caneta:
   def __init__(self, cor=''):
      self.cor = cor
      self.tampa = True



   def destampar(self):
      self.tampa = False



   def escrever(self, msg=''):
      if self.cor == 'azul':
         if self.tampa == True:
            print(f'A [blue]caneta[/blue] está tampada!')
         elif self.tampa == False:
            print(f'[blue]{msg}[/blue]', end='')
      
      elif self.cor == 'vermelho':
         if self.tampa == True:
            print(f'A [red]caneta[/red] está tampada!')
         elif self.tampa == False:
            print(f'[red]{msg}[/red]', end='')

      elif self.cor == 'verde':
         if self.tampa == True:
            print(f'A [green]caneta[/green] está tampada!')
         elif self.tampa == False:
            print(f'[green]{msg}[/green]', end='')

      else:
         print(f'A cor {self.cor} não é válida!')


   

   def quebrar_linha(self, qtd=0):
      print('\n'*qtd, end='')



   
c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, tudo bem? ')
c1.quebrar_linha(2)
c2.escrever('Olá, Gafanhoto! ')
c3.escrever('Vamos exercitar! ')
