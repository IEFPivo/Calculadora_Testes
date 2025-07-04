import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4

# Função auxiliar para aplicar o mesmo teste a todas as versões da calculadora
def todas_versoes(a, b, op):
    return [
        calculadora(a, b, op),
        calculadora_v2(a, b, op),
        calculadora_v3(a, b, op),
        calculadora_v4(a, b, op)
    ]


class TestCalculadora(unittest.TestCase):

    def test_operacoes_basicas(self):
        # Teste operações básicas de cada operador + - * / % ^ para todas as versões
        for resultado in todas_versoes(2, 3, '+'):
            self.assertEqual(resultado, 5)

        for resultado in todas_versoes(5, 3, '-'):
            self.assertEqual(resultado, 2)

        for resultado in todas_versoes(4, 3, '*'):
            self.assertEqual(resultado, 12)

        for resultado in todas_versoes(6, 3, '/'):
            self.assertEqual(resultado, 2.0)

        for resultado in todas_versoes(10, 3, '%'):
            self.assertEqual(resultado, 1)

        for resultado in todas_versoes(2, 3, '^'):
            self.assertEqual(resultado, 8)

    def test_divisao_por_zero(self):
        # Teste divisão por zero e módulo por zero para todas as versões
        for resultado in todas_versoes(5, 0, '/'):
            self.assertTrue(math.isnan(resultado))

        for resultado in todas_versoes(5, 0, '%'):
            self.assertTrue(math.isnan(resultado))

    def test_operadores_invalidos(self):
        # Teste operador inválido - fazer três testes para todas as versões
        for resultado in todas_versoes(2, 3, '$'):
            self.assertTrue(math.isnan(resultado))

        for resultado in todas_versoes(2, 5, '#'):
            self.assertTrue(math.isnan(resultado))

        for resultado in todas_versoes(0, 2, 'qwe'):
            self.assertTrue(math.isnan(resultado))

    def test_virgula_flutuante(self):
        # Teste números de vírgula flutuante - fazer três testes para todas as versões
        for resultado in todas_versoes(2.5, 1.5, '+'):
            self.assertAlmostEqual(resultado, 4.0)

        for resultado in todas_versoes(4.5, 1.5, '-'):
            self.assertAlmostEqual(resultado, 3.0)

        for resultado in todas_versoes(5.5, 1.5, '*'):
            self.assertAlmostEqual(resultado, 8.25)

    def test_numeros_negativos(self):
        # Teste números negativos - fazer 3 testes para todas as versões
        for resultado in todas_versoes(-2, 3, '*'):
            self.assertEqual(resultado, -6)

        # Teste números negativos com divisão e módulo, testar para todas as versões
        for resultado in todas_versoes(-6, 3, '/'):
            self.assertEqual(resultado, -2.0)

        for resultado in todas_versoes(-7, 3, '%'):
            self.assertEqual(resultado, 2.0)

    def test_exponenciacao_negativos_e_zero(self):
        # Teste números negativos com exponenciação, testar para todas as versões
        for resultado in todas_versoes(-2, 3, '^'):
            self.assertEqual(resultado, -8)

        # Teste números negativos com exponenciação de zero, testar para todas as versões
        for resultado in todas_versoes(0, 3, '^'):
            self.assertEqual(resultado, 0)


if __name__ == '__main__':
    unittest.main()

# Para correr os testes: python -m unittest -v testes_main_alunos.py