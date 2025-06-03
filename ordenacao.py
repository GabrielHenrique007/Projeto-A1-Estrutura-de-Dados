def quick_sort(produtos, chave):
    if len(produtos) <= 1:
        return produtos
    else:
        pivot = produtos[len(produtos) // 2]
        menores = [x for x in produtos if getattr(x, chave) < getattr(pivot, chave)]
        iguais = [x for x in produtos if getattr(x, chave) == getattr(pivot, chave)]
        maiores = [x for x in produtos if getattr(x, chave) > getattr(pivot, chave)]
        return quick_sort(menores, chave) + iguais + quick_sort(maiores, chave)

def merge_sort(produtos, chave):
    if len(produtos) <= 1:
        return produtos
    mid = len(produtos) // 2
    esquerda = merge_sort(produtos[:mid], chave)
    direita = merge_sort(produtos[mid:], chave)
    return merge(esquerda, direita, chave)

def merge(esquerda, direita, chave):
    resultado = []
    while esquerda and direita:
        if getattr(esquerda[0], chave) < getattr(direita[0], chave):
            resultado.append(esquerda.pop(0))
        else:
            resultado.append(direita.pop(0))
    resultado.extend(esquerda)
    resultado.extend(direita)
    return resultado
