class Produto:
    def __init__(self, nome, preco, popularidade, categoria, marca, avaliacao):
        self.nome = nome
        self.preco = preco
        self.popularidade = popularidade
        self.categoria = categoria
        self.marca = marca
        self.avaliacao = avaliacao

    def __repr__(self):
        return f"{self.nome} - R${self.preco:.2f} - Popularidade: {self.popularidade} - Avaliação: {self.avaliacao} - Categoria: {self.categoria} - Marca: {self.marca}"
