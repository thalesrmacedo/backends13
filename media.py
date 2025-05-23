# Função para calcular a média de uma lista de números
def calcular_media(numeros):
    # Verifica se a lista está vazia
    if len(numeros) == 0:
        raise ValueError("A lista de números está vazia. Não é possível calcular a média.")
    
    # Calcula a soma dos números
    soma = 0
    for numero in numeros:
        soma += numero
    
    # Calcula a média
    media = soma / len(numeros)
    return media
