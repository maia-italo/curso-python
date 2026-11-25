from rich import print



class Livro:
   def __init__(self, titulo='', pag=0):
      self.titulo = titulo
      self.pag = pag
      self.atual = 1
      print(f':book: Você acabou de abrir o livro [red]"{self.titulo}"[/red] que tem [green]{self.pag} páginas[/green] no total. Você está na [yellow]página {self.atual}[/yellow]')

   def avancar_paginas(self, qtd=0):
      self.count = 0
      for i in range(qtd):
         
         if self.atual < self.pag:
            self.atual += 1
            print(f'Pág [white]{self.atual}[/white] ▶ ', end='')
            self.count += 1
      print(f'Você avançou [white]{self.count}[/white] páginas e agora está na [yellow]página {self.atual}[/yellow]')
      if self.atual == self.pag:
         print(f':closed_book: [red]Você chegou ao final do livro "{self.titulo}"[/red]')



l1 = Livro('10 Coisas que Aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)
