import pytest

from .ex01 import verificar


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        (2, "Par positivo"),      # caminho 1
        (3, "Impar positivo"),    # caminho 2
        (-1, "Negativo"),         # caminho 3
        (0, "Zero"),              # caminho 4
    ],
)
def test_verificar(entrada, esperado):
    assert verificar(entrada) == esperado
