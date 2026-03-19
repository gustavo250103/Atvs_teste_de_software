"""
Testes de UNIDADE (entrada/saida, tipagem, limites, fora do intervalo, mensagens).
Mapa para as 5 tarefas: exemplos completos, casos extras por categoria,
bug da potencia exercitado, caminhos para coverage e notas para relatorio.
"""

from unittest.mock import MagicMock
import unittest
from src.calculadora import Calculadora

class TestEntradaSaida(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()  # Stub do repositório
        self.calc = Calculadora(self.repo)

    def test_soma_retorna_valor_correto(self):
        resultado = self.calc.somar(5, 3)
        self.assertEqual(resultado, 8)

    def test_soma_atualiza_ultimo_resultado(self):
        self.calc.somar(5, 3)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)

    def test_subtrair_retorna_valor_correto(self):
        resultado = self.calc.subtrair(10, 5)
        self.assertEqual(resultado, 5)

    def test_multiplicar_retorna_valor_correto(self):
        resultado = self.calc.multiplicar(4, 3)
        self.assertEqual(resultado, 12)

    def test_dividir_retorna_valor_correto(self):
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5.0)

    def test_potencia_retorna_valor_correto(self):
        resultado = self.calc.potencia(2, 3)
        self.assertEqual(resultado, 8)

class TestTipagem(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()  # Stub do repositório
        self.calc = Calculadora(self.repo)

    def test_tipagem_string_rejeitada(self):
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)

    def test_tipagem_none_rejeitado(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)

    def test_tipagem_bool_rejeitado(self):
        with self.assertRaises(TypeError):
            self.calc.somar(True, 3)

class TestLimite(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()  # Stub do repositório
        self.calc = Calculadora(self.repo)

    def test_limite_zero(self):
        self.assertEqual(self.calc.somar(0, 5), 5)

    def test_limite_float_pequeno(self):
        self.assertAlmostEqual(self.calc.multiplicar(-1e-10, 2), -2e-10)

    def test_limite_float_grande(self):
        import sys
        grande = sys.float_info.max / 2
        resultado = self.calc.somar(grande, grande)
        self.assertFalse(resultado == float('inf'))  # Não deve transbordar

class TestValoresForaDoIntervalo(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()  # Stub do repositório
        self.calc = Calculadora(self.repo)

    def test_divisao_por_zero_levanta_excecao(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

class TestMensagensDeErro(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()  # Stub do repositório
        self.calc = Calculadora(self.repo)

    def test_mensagem_divisao_por_zero(self):
        with self.assertRaisesRegex(ValueError, "Divisao por zero"):
            self.calc.dividir(5, 0)

    def test_mensagem_tipo_invalido(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser numeros"):
            self.calc.somar("x", 1)
