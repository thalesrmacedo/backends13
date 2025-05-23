# Importa a biblioteca de testes e a função que será testada
import unittest
from media import calcular_media

# Classe com os testes
class TesteDaMedia(unittest.TestCase):
    # Teste com três números
    def test_media_simples(self):
        resultado = calcular_media([10, 20, 30])
        self.assertEqual(resultado, 20)

    # Teste com a lista vazia
    def test_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

# Executa os testes
if __name__ == "__main__":
    unittest.main()
