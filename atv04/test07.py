import pytest

from .ex07 import desconto


# Objetivos:
# - All-Defs / All-Uses: cada definição tem um uso exercitado.
# - CC na condição composta cliente_vip + total<50, além da condição interna total<50 após cada definição de total.
# - Laço não existe aqui; os cenários variam pelas definições de total.
#
# Casos:
# 1) cliente_vip=False, preco=120 -> total=t1=120; total<50 False; return t1 (cobre t1->F false e t1->H).
# 2) cliente_vip=False, preco=40 -> total=t1=40; total<50 True; total=t3=50; return t3 (cobre t1->F true, t3->H).
# 3) cliente_vip=True, preco=200 -> desconto d1 usado; total=t2=160; total<50 False; return t2 (cobre d1->E, t2->F false, t2->H).
# 4) cliente_vip=True, preco=60 -> desconto d1 usado; total=t2=48; total<50 True; total=t3=50; return t3 (cobre t2->F true, t3->H).
@pytest.mark.parametrize(
    "preco, vip, esperado",
    [
        (120, False, 120.0),
        (40, False, 50.0),
        (200, True, 160.0),
        (60, True, 50.0),
    ],
)
def test_desconto_all_defs_uses(preco, vip, esperado):
    assert desconto(preco, vip) == pytest.approx(esperado)


def test_def_use_cobertura_c1_vs_du():
    """
    Cobertura de ramos (C1) com 2 casos (VIP e não VIP, ambos sem cair em total<50)
    não cobre todos os pares def-uso: faltariam ramos onde total<50 é True (t1->F true, t2->F true, t3->H).
    Os casos 2 e 4 acima são necessários para cobrir esses pares.
    """
    assert True
