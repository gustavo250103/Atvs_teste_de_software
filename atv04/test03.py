import pytest

from .ex03 import acesso


# Cobertura de Condição (CC): todas as combinações das duas condições
# C1 (ramos) requer apenas 2 casos (um True para if, um False),
# mas CC precisa 4 para cobrir todas as combinações (idade>=18 True/False x membro True/False).
@pytest.mark.parametrize(
    "idade, membro, esperado",
    [
        (20, True, "Permitido"),   # idade>=18 True, membro True -> if True
        (20, False, "Negado"),     # idade>=18 True, membro False -> if False
        (17, True, "Negado"),      # idade>=18 False, membro True -> if False
        (17, False, "Negado"),     # idade>=18 False, membro False -> if False
    ],
)
def test_acesso_condicao(idade, membro, esperado):
    assert acesso(idade, membro) == esperado
