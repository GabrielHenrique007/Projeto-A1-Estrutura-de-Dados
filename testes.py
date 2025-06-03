import unittest
from produto import Produto
from ordenacao import quick_sort
from busca import busca

class TestEcommerce(unittest.TestCase):
    def setUp(self):
        self.produtos = [
            Produto("iPhone 16", 6999.90, 10, "Smartphones", "Apple", 4.9),
            Produto("Samsung Galaxy S23", 5999.90, 9, "Smartphones", "Samsung", 4.8),
            Produto("Google Pixel 7", 4999.90, 8, "Smartphones", "Google", 4.7)
        ]

    def test_busca(self):
        resultados = busca(self.produtos, "iPhone")
        self.assertEqual(len(resultados), 1)

    def test_busca_com_filtro(self):
        resultados = busca(self.produtos, "iPhone", categoria="Smartphones")
        self.assertEqual(len(resultados), 1)

    def test_ordenacao(self):
        produtos_ordenados = quick_sort(self.produtos, 'preco')
        self.assertEqual(produtos_ordenados[0].nome, "Google Pixel 7")
        self.assertEqual(produtos_ordenados[1].nome, "Samsung Galaxy S23")
        self.assertEqual(produtos_ordenados[2].nome, "iPhone 16")

if __name__ == '__main__':
    unittest.main()
