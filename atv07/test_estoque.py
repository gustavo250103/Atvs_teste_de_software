"""Suite de testes da atividade 07.

Os comentarios RED, GREEN e REFACTOR foram mantidos para evidenciar a
sequencia usada no desenvolvimento orientado a testes (TDD).
"""

import pytest

from estoque import Estoque


# CICLO 1 - RED: primeiro descrevemos consultar_quantidade e adicionar_produto.
# RED: consultar produto inexistente deve retornar 0.
def test_consultar_produto_inexistente_retorna_zero():
    estoque = Estoque()

    assert estoque.consultar_quantidade("arroz") == 0


# RED: adicionar um produto novo deve registrar a quantidade inicial.
def test_adicionar_produto_novo_registra_quantidade():
    estoque = Estoque()

    estoque.adicionar_produto("arroz", 10)

    assert estoque.consultar_quantidade("arroz") == 10


# RED: adicionar um produto existente deve somar a quantidade, nao sobrescrever.
def test_adicionar_produto_existente_incrementa_quantidade():
    estoque = Estoque()

    estoque.adicionar_produto("arroz", 10)
    estoque.adicionar_produto("arroz", 5)

    assert estoque.consultar_quantidade("arroz") == 15


@pytest.mark.parametrize("quantidade", [0, -3])
# RED: o estoque nao aceita adicionar quantidade zero ou negativa.
def test_adicionar_produto_com_quantidade_invalida_gera_erro(quantidade):
    estoque = Estoque()

    with pytest.raises(ValueError):
        estoque.adicionar_produto("arroz", quantidade)


# CICLO 2 - RED: agora cobrimos remover_produto e suas regras de erro.
# RED: remover deve reduzir apenas a quantidade solicitada quando houver saldo suficiente.
def test_remover_produto_reduz_quantidade_disponivel():
    estoque = Estoque()
    estoque.adicionar_produto("feijao", 10)

    estoque.remover_produto("feijao", 4)

    assert estoque.consultar_quantidade("feijao") == 6


# RED: nao e permitido remover mais unidades do que o disponivel.
def test_remover_produto_maior_que_disponivel_gera_erro():
    estoque = Estoque()
    estoque.adicionar_produto("feijao", 3)

    with pytest.raises(ValueError):
        estoque.remover_produto("feijao", 4)


@pytest.mark.parametrize("quantidade", [0, -2])
# RED: remover com quantidade nao positiva viola a regra de negocio.
def test_remover_produto_com_quantidade_invalida_gera_erro(quantidade):
    estoque = Estoque()
    estoque.adicionar_produto("feijao", 5)

    with pytest.raises(ValueError):
        estoque.remover_produto("feijao", quantidade)


# CICLO 3 - RED: por fim, descrevemos as consultas agregadas do estoque.
# RED: listar_produtos deve mostrar apenas itens com quantidade positiva.
def test_listar_produtos_retorna_apenas_itens_com_saldo_positivo():
    estoque = Estoque()
    estoque.adicionar_produto("arroz", 10)
    estoque.adicionar_produto("feijao", 5)
    estoque.remover_produto("feijao", 5)

    assert estoque.listar_produtos() == ["arroz"]


# RED: estoque vazio deve produzir lista vazia.
def test_listar_produtos_em_estoque_vazio_retorna_lista_vazia():
    estoque = Estoque()

    assert estoque.listar_produtos() == []


# RED: a consulta agregada deve identificar o produto com maior quantidade.
def test_produto_mais_estocado_retorna_nome_com_maior_quantidade():
    estoque = Estoque()
    estoque.adicionar_produto("arroz", 10)
    estoque.adicionar_produto("feijao", 15)
    estoque.adicionar_produto("macarrao", 7)

    assert estoque.produto_mais_estocado() == "feijao"


# RED: nao havendo produtos com saldo positivo, o retorno deve ser None.
def test_produto_mais_estocado_em_estoque_vazio_retorna_none():
    estoque = Estoque()

    assert estoque.produto_mais_estocado() is None


# REFACTOR: a suite final permanece legivel e cobre fluxos normais e de erro
# depois da extracao de regras comuns para metodos auxiliares em estoque.py.
