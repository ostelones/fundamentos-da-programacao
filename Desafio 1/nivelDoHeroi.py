# Inicia a variável para controlar se o usuário quer continuar
deseja_continuar = "sim"

# Laço de repetição principal para permitir múltiplas classificações
while deseja_continuar.lower() == "sim":
    # 1. Coletar o nome do herói
    nome_do_heroi = input("Bem-vindo ao Classificador de Nível de Heróis!\n\nDigite o nome do herói: ")

    # Validação de nome (opcional, mas boa prática)
    if not nome_do_heroi or nome_do_heroi.strip() == "": # .strip() remove espaços em branco antes/depois
        print("O nome do herói não pode ser vazio. Por favor, tente novamente.")
        deseja_continuar = input("Deseja classificar outro herói? (sim/nao) ").lower()
        print("-" * 30) # Linha divisória para melhor visualização
        continue # Volta para o início do loop principal

    # 2. Coletar e validar a XP do herói usando um laço interno
    experiencia_do_heroi = None # Inicializa como None para o loop de validação
    while experiencia_do_heroi is None: # Loop para garantir uma entrada de XP válida
        xp_input = input(f"Olá, {nome_do_heroi}!\n\nDigite a quantidade de experiência (XP) do herói: ")

        try:
            experiencia_do_heroi = int(xp_input) # Tenta converter para inteiro
            if experiencia_do_heroi < 0:
                print("Entrada inválida! A XP não pode ser negativa. Por favor, digite um número positivo.")
                experiencia_do_heroi = None # Reseta para continuar o loop
        except ValueError:
            # Captura o erro se a conversão para int falhar (ex: usuário digitou texto)
            print("Entrada inválida! Por favor, digite um número de XP válido.")
            experiencia_do_heroi = None # Reseta para continuar o loop

    # 3. Estruturas de Decisão para classificar o nível
    nivel_do_heroi = "" # Inicializa a variável do nível
    if experiencia_do_heroi < 1000:
        nivel_do_heroi = "Ferro"
    elif experiencia_do_heroi <= 2000: # Já sabemos que é >= 1000
        nivel_do_heroi = "Bronze"
    elif experiencia_do_heroi <= 5000: # Já sabemos que é >= 2001
        nivel_do_heroi = "Prata"
    elif experiencia_do_heroi <= 7000: # Já sabemos que é >= 5001
        nivel_do_heroi = "Ouro"
    elif experiencia_do_heroi <= 8000: # Já sabemos que é >= 7001
        nivel_do_heroi = "Platina"
    elif experiencia_do_heroi <= 9000: # Já sabemos que é >= 8001
        nivel_do_heroi = "Ascendente"
    elif experiencia_do_heroi <= 10000: # Já sabemos que é >= 9001
        nivel_do_heroi = "Imortal"
    else: # Se não se encaixou em nenhum dos anteriores, é >= 10001
        nivel_do_heroi = "Radiante"

    # 4. Apresentar o resultado
    # Usamos f-strings (formatted string literals) que são uma forma elegante de incluir variáveis em strings no Python.
    print(f"\nO Herói de nome {nome_do_heroi} está no nível de {nivel_do_heroi}")

    # Pergunta ao usuário se quer classificar outro herói
    deseja_continuar = input("\nDeseja classificar outro herói? (sim/nao) ").lower()
    print("-" * 30) # Linha divisória para melhor visualização

print("Obrigado por usar o Classificador de Nível de Heróis! Até mais.")
