# 1. Definição da função para calcular o saldo e o nível
def calcular_nivel_rankeado(vitorias, derrotas):
    """
    Calcula o saldo de vitórias e determina o nível do herói com base no SALDO de vitórias.

    Parâmetros:
    vitorias (int): Quantidade de vitórias do herói.
    derrotas (int): Quantidade de derrotas do herói.

    Retorna:
    tuple: Uma tupla contendo (saldo_de_vitorias, nivel_do_heroi).
    """
    # Variáveis e Operadores: Cálculo do saldo
    saldo = vitorias - derrotas

    # Estruturas de Decisão: Determinação do nível (AGORA BASEADO NO SALDO)
    nivel = "" # Inicializa a variável nivel
    if saldo < 10:
        nivel = "Ferro"
    elif saldo <= 20: # Implica que 10 <= saldo <= 20
        nivel = "Bronze"
    elif saldo <= 50: # Implica que 21 <= saldo <= 50
        nivel = "Prata"
    elif saldo <= 80: # Implica que 51 <= saldo <= 80
        nivel = "Ouro"
    elif saldo <= 90: # Implica que 81 <= saldo <= 90
        nivel = "Diamante"
    elif saldo <= 100: # Implica que 91 <= saldo <= 100
        nivel = "Lendário"
    else: # Implica que saldo >= 101
        nivel = "Imortal"

    return saldo, nivel # Retorna os dois valores

# --- Início do Programa Principal ---

# Laços de Repetição: Variável para controlar se o usuário quer continuar
deseja_continuar = "sim"

print("--- Calculadora de Nível de Heróis Rankeados ---")

# Laço de repetição principal para permitir múltiplas classificações
while deseja_continuar.lower() == "sim":
    # Variáveis e Laços de Repetição: Coleta e validação de entrada de vitórias
    vitorias = -1 # Valor inicial inválido para entrar no loop
    while vitorias < 0:
        try:
            vitorias_str = input("Digite a quantidade de vitórias do herói: ")
            vitorias = int(vitorias_str)
            if vitorias < 0:
                print("O número de vitórias não pode ser negativo. Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para vitórias.")
            vitorias = -1 # Garante que o loop continue

    # Variáveis e Laços de Repetição: Coleta e validação de entrada de derrotas
    derrotas = -1 # Valor inicial inválido para entrar no loop
    while derrotas < 0:
        try:
            derrotas_str = input("Digite a quantidade de derrotas do herói: ")
            derrotas = int(derrotas_str)
            if derrotas < 0:
                print("O número de derrotas não pode ser negativo. Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para derrotas.")
            derrotas = -1 # Garante que o loop continue

    # Chamada da função e armazenamento dos resultados
    saldo_final, nivel_final = calcular_nivel_rankeado(vitorias, derrotas)

    # Saída: Exibição da mensagem final
    print(f"\nO Herói tem saldo de {saldo_final} vitórias e está no nível {nivel_final}!")

    # Pergunta ao usuário se quer fazer outro cálculo
    deseja_continuar = input("\nDeseja calcular para outro herói? (sim/nao) ").lower()
    print("-" * 30) # Linha divisória para melhor visualização

print("Obrigado por usar a Calculadora de Nível de Heróis Rankeados! Até mais.")