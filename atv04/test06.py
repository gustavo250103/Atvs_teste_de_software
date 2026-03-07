import pytest

from .ex06 import analisar

# Casos para C0/C1, CC e comportamentos do laço.
# CC da condição (n > 0) and (n % 2 == 0):
# - (True, True): n=2 (par positivo)
# - (True, False): n=3 (ímpar positivo)
# - (False, *) : n=-1 (negativo) ou n=0 (zero)
#
# Comportamento do laço:
# - 0 iterações: []
# - 1 iteração: [2]
# - várias iterações: [6, 6], [3, -1], etc.
#
# Def-uso de total a cobrir:
# - total=0 (def) → usado em total>10 (caso ultrapassa 10 após somas).
# - total += n (def) → usado em total>10 (caso 6,6).
# - total -= 1 (def) → usado em total>10? (aqui sempre mantém <=10 nos testes) e valor final.
@pytest.mark.parametrize(
    "entrada, esperado, descricao",
    [
        ([], "Abaixo", "laço ignorado (0 iterações); total permanece 0"),
        ([2], "Abaixo", "CC (True,True) mas total=2 <=10; 1 iteração"),
        ([6, 6], "Acima", "várias iterações; total=12 aciona if total>10"),
        ([3], "Abaixo", "CC (True,False) segue continue; total não muda"),
        ([-1, -2], "Abaixo", "n>0 False; ramos negativos; total=-2"),
    ],
)
def test_analisar(entrada, esperado, descricao):
    assert analisar(entrada) == esperado
