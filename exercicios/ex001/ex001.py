# Declaração de classe
class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Declaração de objetos

g1 = Gafanhoto() # Criação do objeto g1
g1.nome = "Maria" # Atribuição de valor ao atributo nome
g1.idade = 17 # Atribuição de valor ao atributo idade
g1.aniversario() # Chamada do método aniversario do objeto g1

print(g1.mensagem()) # Chamada do método mensagem do objeto g1

g2 = Gafanhoto() # Criação do objeto g2
g2.nome = "Mauro" # Atribuição de valor ao atributo nome
g2.idade = 53 # Atribuição de valor ao atributo idade

print(g2.mensagem()) # Chamada do método mensagem do objeto g2
