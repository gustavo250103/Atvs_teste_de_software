import pytest

from .ex04 import somar_ate


# Cobertura solicitada:
# - Laço ignorado (0 iterações): n=0 -> saída esperada 0.
# - Laço executado uma única vez: n=1 -> soma = 0 -> saída 0.
# - Laço executado várias vezes: n=5 -> 0+1+2+3+4 = 10.
@pytest.mark.parametrize(
    "n, esperado, descricao",
    [
        (0, 0, "laço ignorado (0 iterações)"),
        (1, 0, "laço executa 1 vez (soma só o i=0)"),
        (5, 10, "laço executa várias vezes (0+1+2+3+4)"),
    ],
)
def test_somar_ate(n, esperado, descricao):
    assert somar_ate(n) == esperado
