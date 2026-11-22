from rich import print
from rich.table import Table

tabela = Table(title='Tabela de preços')

tabela.add_column('Nome', justify='right', style='red')
tabela.add_column('Preço', justify='center', style='blue')
tabela.add_row('Lápis', 'R$1,50')
tabela.add_row('Caneta', '[green]R$2,00[/green]')
tabela.add_row('Caderno', 'R$15,00')
tabela.add_row('Mochila', 'R$120,00')

print(tabela)