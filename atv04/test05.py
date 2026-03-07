import pytest

from .ex05 import percorrer_matriz


# Cenários pedidos e quantidade esperada de impressões (linha do print):
# 1) Ambos os laços ignorados: m=0, n=5 -> 0 vezes.
# 2) Só o laço j é ignorado: m=3, n=0 -> 0 vezes (externo roda, interno não).
# 3) Um laço 1 vez e outro várias: m=1, n=4 -> 4 vezes (1*4).
# 4) Ambos vários: m=3, n=2 -> 6 vezes (3*2).
@pytest.mark.parametrize(
    "m, n, esperado",
    [
        (0, 5, 0),
        (3, 0, 0),
        (1, 4, 4),
        (3, 2, 6),
    ],
)
def test_percorrer_matriz_contagem(m, n, esperado, capsys):
    percorrer_matriz(m, n)
    capturado = capsys.readouterr().out.strip()
    linhas = 0 if not capturado else len(capturado.splitlines())
    assert linhas == esperado
