import math

import pytest
from hypothesis import given, strategies as st

from frete import calcular_frete


# ---------- Classes de Equivalência ----------
@pytest.mark.parametrize(
    "peso,destino,valor,esperado",
    [
        (0.5, "mesma_regiao", 50.0, 10.0),  # classe válida base
        (2.0, "outra_regiao", 50.0, 22.5),  # acréscimo 50%
        (8.0, "internacional", 150.0, 50.0),  # acréscimo 100%
        (3.0, "mesma_regiao", 250.0, 0.0),  # frete grátis
    ],
)
def test_classes_equivalencia_validas(peso, destino, valor, esperado):
    assert calcular_frete(peso, destino, valor) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "peso,destino,valor",
    [
        (0, "mesma_regiao", 50.0),
        (-1, "mesma_regiao", 50.0),
        (21, "outra_regiao", 50.0),
    ],
)
def test_classes_equivalencia_peso_invalido(peso, destino, valor):
    with pytest.raises(ValueError):
        calcular_frete(peso, destino, valor)


# ---------- Valores Limite (fronteiras 1 kg, 5 kg, 20 kg) ----------
@pytest.mark.parametrize(
    "peso,esperado",
    [
        (0.9, 10.0),
        (1.0, 10.0),
        (1.01, 15.0),
    ],
)
def test_valores_limite_fronteira_1kg(peso, esperado):
    assert calcular_frete(peso, "mesma_regiao", 100) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "peso,esperado",
    [
        (4.99, 15.0),
        (5.0, 15.0),
        (5.01, 25.0),
    ],
)
def test_valores_limite_fronteira_5kg(peso, esperado):
    assert calcular_frete(peso, "mesma_regiao", 100) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "peso,espera_erro,esperado",
    [
        (19.99, False, 25.0),
        (20.0, False, 25.0),
        (20.01, True, None),
    ],
)
def test_valores_limite_fronteira_20kg(peso, espera_erro, esperado):
    if espera_erro:
        with pytest.raises(ValueError):
            calcular_frete(peso, "mesma_regiao", 100)
    else:
        assert calcular_frete(peso, "mesma_regiao", 100) == pytest.approx(esperado)


# ---------- Tabela de Decisão (6 combinações principais) ----------
@pytest.mark.parametrize(
    "peso,destino,valor,esperado",
    [
        (1, "mesma_regiao", 50, 10.0),
        (1, "outra_regiao", 50, 15.0),
        (1, "internacional", 50, 20.0),
        (10, "mesma_regiao", 300, 0.0),  # frete grátis
        (10, "outra_regiao", 300, 0.0),  # frete grátis com acréscimo não aplicado
        (10, "internacional", 300, 0.0),  # frete grátis internacional
    ],
)
def test_tabela_decisao(peso, destino, valor, esperado):
    assert calcular_frete(peso, destino, valor) == pytest.approx(esperado)


# ---------- Entradas inválidas adicionais ----------
def test_destino_invalido():
    with pytest.raises(ValueError):
        calcular_frete(2, "marte", 50)


def test_valor_pedido_negativo():
    with pytest.raises(ValueError):
        calcular_frete(2, "mesma_regiao", -10)


# ---------- Propriedades com Hypothesis ----------
valid_destinos = st.sampled_from(["mesma_regiao", "outra_regiao", "internacional"])


@given(
    peso=st.floats(min_value=0.01, max_value=20, allow_nan=False, allow_infinity=False),
    destino=valid_destinos,
    valor=st.floats(min_value=0, max_value=200, allow_nan=False, allow_infinity=False),
)
def test_propriedade_frete_nunca_negativo(peso, destino, valor):
    frete = calcular_frete(peso, destino, valor)
    assert frete >= 0


@given(
    peso=st.floats(min_value=0.01, max_value=20, allow_nan=False, allow_infinity=False),
    destino=valid_destinos,
    valor=st.floats(min_value=200.01, max_value=10000, allow_nan=False, allow_infinity=False),
)
def test_propriedade_frete_gratis_acima_200(peso, destino, valor):
    assert calcular_frete(peso, destino, valor) == 0.0


@given(
    peso=st.floats(min_value=0.01, max_value=20, allow_nan=False, allow_infinity=False),
    valor=st.floats(min_value=0, max_value=200, allow_nan=False, allow_infinity=False),
)
def test_propriedade_outra_regiao_maior_ou_igual(peso, valor):
    mesma = calcular_frete(peso, "mesma_regiao", valor)
    outra = calcular_frete(peso, "outra_regiao", valor)
    assert outra >= mesma
