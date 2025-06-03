# 🚀 Projeto de Algoritmos de Busca e Ordenação

## Sobre o Projeto
Este projeto tem como objetivo aplicar algoritmos de busca e ordenação em diferentes contextos, otimizando a recuperação e organização de informações.

## Exemplos Práticos de Uso

### Exemplo 1: Buscar e ordenar produtos por popularidade
No arquivo main.py, realizamos uma busca pelo termo "iphone" na lista de produtos e ordenamos os resultados pela popularidade, exibindo os mais populares primeiro.

```python
from produto import Produto
from ordenacao import quick_sort
from busca import busca

produtos = [
    Produto("iPhone 16", 6999.90, 10, "Smartphones", "Apple", 4.9),
    Produto("Samsung Galaxy S23", 5999.90, 9, "Smartphones", "Samsung", 4.8),
    Produto("Google Pixel 7", 4999.90, 8, "Smartphones", "Google", 4.7),
    Produto("OnePlus 11", 3999.90, 7, "Smartphones", "OnePlus", 4.6),
    Produto("Xiaomi 13", 3499.90, 6, "Smartphones", "Xiaomi", 4.5)
]

termo_busca = "iphone"
resultados_busca = busca(produtos, termo_busca)

# Ordenar por popularidade (maior para menor)
resultados_ordenados = quick_sort(resultados_busca, 'popularidade')

print(f"Resultados da busca por '{termo_busca}':")
for produto in resultados_ordenados:
    print(produto) 
```

### Exemplo 2: Buscar produtos em uma categoria específica e ordenar por preço
Podemos também buscar produtos filtrando pela categoria "Smartphones" e ordenar os resultados pelo preço, exibindo do mais barato para o mais caro.

```python
categoria_filtro = "Smartphones"
resultados_filtrados = busca(produtos, termo_busca, categoria=categoria_filtro)

# Ordenar por preço (menor para maior)
resultados_filtrados_ordenados = quick_sort(resultados_filtrados, 'preco')

print(f"\nResultados da busca por '{termo_busca}' na categoria '{categoria_filtro}':")
for produto in resultados_filtrados_ordenados:
    print(produto)
```

### Exemplo 3: Testar funcionalidades com testes automatizados
Para garantir que as funções de busca e ordenação funcionam corretamente, execute os testes no arquivo testes.py com o seguinte comando no terminal:

```python
python testes.py
```

Isso irá rodar os testes automáticos para validar as buscas e ordenações no nosso conjunto de produtos.

### Esses exemplos mostram como integrar os módulos para criar um sistema simples de busca e ordenação para um catálogo de produtos em e-commerce.

### Tecnologias Utilizadas:

1. Python 3
2. Algoritmos de Ordenação: Quick Sort, Merge Sort
3. Algoritmo de Busca linear com filtros

### Como Executar:

1. Clone o projeto.
2. Execute main.py para ver os exemplos de busca e ordenação.
3. Execute testes.py para rodar os testes automatizados.
