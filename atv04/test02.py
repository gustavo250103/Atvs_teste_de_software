import pytest

from .ex02 import classificar


# Mínimo para C0 (comandos) e C1 (ramos):
# - 3 casos cobrem as três saídas e os ramos verdadeiro/falso de ambas decisões.
@pytest.mark.parametrize(
    "entrada, esperado, descricao",
    [
        (150, "Alto", "B=True"),          # cobre decisão x>100 verdadeira
        (75, "Medio", "B=False, D=True"), # cobre x>100 falsa e x>50 verdadeira
        (20, "Baixo", "B=False, D=False") # cobre ambos falsos
    ],
)
def test_classificar(entrada, esperado, descricao):
    assert classificar(entrada) == esperado
