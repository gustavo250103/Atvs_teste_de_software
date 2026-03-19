"""
Test doubles (stub e mock) demonstrando diferencas praticas.
Ligacao com tarefas: exemplos completos (1), extras de interacao (2),
detecao do bug de potencia via mock (3), caminhos de cobertura (4)
e notas explicativas para o relatorio (5).
"""

from unittest.mock import MagicMock
import unittest
from src.calculadora import Calculadora
from src.repositorio import HistoricoRepositorio

class TestComStub(unittest.TestCase):
    def setUp(self):
        self.stub_repo = MagicMock()
        self.calc = Calculadora(self.stub_repo)

    def test_soma_stub_repositorio(self):
        resultado = self.calc.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_stub_repositorio_nao_precisa_estar_pronto(self):
        self.stub_repo.total.return_value = 0
        resultado = self.calc.multiplicar(3, 7)
        self.assertEqual(resultado, 21)

class TestComMock(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.calc = Calculadora(self.mock_repo)

    def test_mock_salvar_chamado_apos_soma(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once()

    def test_mock_salvar_chamado_com_argumento_correto(self):
        self.calc.somar(4, 6)
        self.mock_repo.salvar.assert_called_once_with("4 + 6 = 10")

    def test_mock_salvar_nao_chamado_em_excecao(self):
        with self.assertRaises(TypeError):
            self.calc.somar("x", 1)
        self.mock_repo.salvar.assert_not_called()
