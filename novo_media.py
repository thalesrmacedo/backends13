def calcular_media(numeros):
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")
    return sum(numeros) / len(numeros)
