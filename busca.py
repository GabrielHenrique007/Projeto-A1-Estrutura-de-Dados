def busca(produtos, termo, categoria=None, marca=None):
    resultados = []
    for produto in produtos:
        if termo.lower() in produto.nome.lower():
            if (categoria is None or produto.categoria.lower() == categoria.lower()) and \
               (marca is None or produto.marca.lower() == marca.lower()):
                resultados.append(produto)
    return resultados
