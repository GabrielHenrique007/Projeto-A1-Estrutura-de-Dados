from produto import Produto
from ordenacao import quick_sort
from busca import busca

# Criando uma lista de produtos
produtos = [
    Produto("iPhone 16", 6999.90, 10, "Smartphones", "Apple", 4.9),
    Produto("Samsung Galaxy S23", 5999.90, 9, "Smartphones", "Samsung", 4.8),
    Produto("Google Pixel 7", 4999.90, 8, "Smartphones", "Google", 4.7),
    Produto("OnePlus 11", 3999.90, 7, "Smartphones", "OnePlus", 4.6),
    Produto("Xiaomi 13", 3499.90, 6, "Smartphones", "Xiaomi", 4.5)
]

# Buscando produtos
termo_busca = "iphone"
resultados_busca = busca(produtos, termo_busca)

# Ordenando resultados por popularidade
resultados_ordenados = quick_sort(resultados_busca, 'popularidade')

print(f"Resultados da busca por '{termo_busca}':")
for produto in resultados_ordenados:
    print(produto)

# Exemplo de busca com filtro por categoria
categoria_filtro = "Smartphones"
resultados_filtrados = busca(produtos, termo_busca, categoria=categoria_filtro)

# Ordenando resultados filtrados por preço
resultados_filtrados_ordenados = quick_sort(resultados_filtrados, 'preco')

print(f"\nResultados da busca por '{termo_busca}' na categoria '{categoria_filtro}':")
for produto in resultados_filtrados_ordenados:
    print(produto)
