# Declaração de classe
class Gafanhoto:
   """
   Essa classe representa um Gafanhoto com atributos de nome e idade, e métodos para celebrar aniversários e exibir uma mensagem de apresentação.

   Para criar um novo Gafanhoto, use:

      variavel = Gafanhoto(nome, idade)
   """
   def __init__(self, nome = "vazio", idade = 0): # Método construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
   def aniversario(self):
        self.idade += 1

   def __str__(self): # Dunder method para representação em string do objeto
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

   def __getstate__(self): # Dunder method para obter o estado do objeto
        return f"Estado: nome = {self.nome}, idade = {self.idade}"

# Declaração de objetos

g1 = Gafanhoto('Maria', 17) # Criação do objeto g1
g1.aniversario() # Chamada do método aniversario do objeto g1

print(g1)
print(g1.__str__()) # Exibe a classe do objeto g1
print(g1.__doc__) # Exibe a documentação da classe g1
print(g1.__dict__) # Exibe o dicionário de atributos do objeto g1
print(g1.__getstate__()) # Exibe o estado do objeto g1

g2 = Gafanhoto('Mauro', 54) # Criação do objeto g2
print(g2)
print(g2.__getstate__()) # Exibe o estado do objeto g2
print(g2.__class__) # Exibe a classe do objeto g2
