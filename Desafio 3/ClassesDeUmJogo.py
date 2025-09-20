# 1. Classes e Objetos: Definição da Classe Heroi
class Heroi:
    # 2. Construtor da classe (__init__)
    # O __init__ é uma função especial que é chamada quando um novo objeto Heroi é criado.
    # self referencia o próprio objeto que está sendo criado.
    def __init__(self, nome, idade, tipo):
        # Variáveis: Propriedades do herói (atributos do objeto)
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    # 3. Funções (Métodos): Definição do método atacar
    def atacar(self):
        # Variáveis: Variável local para armazenar a descrição do ataque
        ataque_descricao = ""

        # Estruturas de Decisão: Define a descrição do ataque com base no tipo do herói
        # self.tipo acessa a propriedade 'tipo' do objeto atual
        if self.tipo == "mago":
            ataque_descricao = "magia"
        elif self.tipo == "guerreiro":
            ataque_descricao = "espada"
        elif self.tipo == "monge":
            ataque_descricao = "artes marciais"
        elif self.tipo == "ninja":
            ataque_descricao = "shuriken"
        else:
            # Caso o tipo seja desconhecido, para garantir que algo seja exibido
            ataque_descricao = "um ataque misterioso"

        # Operadores: Exibir a mensagem final usando f-string para concatenação
        print(f"O {self.tipo} atacou usando {ataque_descricao}")

# --- Início do Programa Principal ---

print("--- Criando nossos Heróis ---")

# Criando Objetos: Instanciando a classe Heroi para criar heróis específicos
heroi_mago = Heroi("Merlin", 1000, "mago")
heroi_guerreiro = Heroi("Conan", 35, "guerreiro")
heroi_monge = Heroi("Li", 45, "monge")
heroi_ninja = Heroi("Hanzo", 28, "ninja")
heroi_paladino = Heroi("Arthur", 50, "paladino")

print("\n--- Heróis atacando individualmente ---")

# Chamando os Métodos: Cada objeto executa seu próprio método atacar
heroi_mago.atacar()
heroi_guerreiro.atacar()
heroi_monge.atacar()
heroi_ninja.atacar()
heroi_paladino.atacar()

# Laços de Repetição
print("\n--- Uma lista de heróis atacando em sequência ---")
lista_de_herois = [heroi_mago, heroi_guerreiro, heroi_monge, heroi_ninja, heroi_paladino]

for heroi_atual in lista_de_herois:
    heroi_atual.atacar()

print("\n--- Fim da aventura! ---")