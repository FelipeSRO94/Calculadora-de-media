# Função para calcular a média e verificar se foi aprovado ou reprovado
def calcular_media():
    # Pedindo ao usuário para inserir as notas
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))

    # Calculando a média
    soma = nota1 + nota2 + nota3 + nota4
    media = soma / 4

    # Verificando se foi aprovado ou reprovado
    if media >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    # Exibindo a média e a situação
    print(f"A média das notas é: {media:.2f}")
    print(f"Situação: {situacao}")

# Chamando a função para calcular a média e verificar a situação
calcular_media()
