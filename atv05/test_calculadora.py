import pytest
from calculadora import somar, dividir, subtrair, multiplicar

def test_somar_positivos():
    assert somar(2, 3) == 5
    assert somar(10, 20) == 30

def test_somar_negativos():
    assert somar(-5, -3) == -8

def test_somar_com_zero():
    assert somar(0, 5) == 5
    assert somar(0, 0) == 0

def test_dividir_basico():
    """Testa divisao basica"""
    assert dividir(10, 2) == 5
    assert dividir(20, 4) == 5

def test_dividir_por_zero():
    """Testa excecao divisao por zero"""
    with pytest.raises(ValueError) as excinfo:
        dividir(10, 0)
    assert str(excinfo.value) == "Divisao por zero!"

def test_dividir_zero_por_numero():
    """Testa zero dividido por numero"""
    assert dividir(0, 5) == 0

def test_dividir_negativos():
    assert dividir(-9, 3) == -3
    assert dividir(9, -3) == -3

def test_subtrair_basico():
    assert subtrair(5, 3) == 2
    assert subtrair(-5, -3) == -2
    assert subtrair(0, 5) == -5

def test_multiplicar_basico():
    assert multiplicar(4, 3) == 12
    assert multiplicar(-2, 3) == -6
    assert multiplicar(0, 99) == 0
    assert multiplicar(0.1, 0.2) == pytest.approx(0.02)

class TestSomar:
    """Grupo de testes para somar"""
    def test_positivos(self):
        assert somar(2, 3) == 5

    def test_negativos(self):
        assert somar(-5, -3) == -8

class TestDividir:
    """Grupo de testes para dividir"""

    def test_basico(self):
        assert dividir(10, 2) == 5

    def test_por_zero(self):
        with pytest.raises(ValueError):
            dividir(10, 0)

@pytest.mark.parametrize("a,b,esperado", [
(2, 3, 5),
(10, 20, 30),
(-5, 5, 0),
(0, 0, 0),
(100, 1, 101)
])

def test_somar_parametrizado(a, b, esperado):
    """Testa multiplos casos"""
    assert somar(a, b) == esperado

"""# ERRADO - pode falhar
def test_divisao_errado():
    assert dividir(10, 3) == 3.333333"""

# CORRETO - usa aproximacao
def test_divisao_correto():
    assert dividir(10, 3) == pytest.approx(3.333333)

# Tambem funciona
def test_soma_decimais():
    assert somar(0.1, 0.2) == pytest.approx(0.3)

def valida_nota(nota):
    if nota < 0 or nota > 10:
        raise ValueError("Nota deve ser entre 0 e 10")
    return True

def calcular_media(notas):
    if not notas:
        raise ValueError("Lista de notas vazia")
    return sum(notas) / len(notas) 

def obter_situacao(nota):
    if nota >= 5:
        return "Aprovado"
    elif nota <= 3:
        return "Reprovado"
    else:
        return "Recuperacao"
    
def calcular_estatisticas(notas):
    if not notas:
        raise ValueError("Lista de notas vazia")
    
    for nota in notas:
        valida_nota(nota)
    
    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)
    
    aprovados = 0
    reprovados = 0
    recuperacao = 0
    
    for nota in notas:
        situacao = obter_situacao(nota)
        if situacao == "Aprovado":
            aprovados += 1
        elif situacao == "Reprovado":
            reprovados += 1
        elif situacao == "Recuperacao":
            recuperacao += 1
    
    return {
        "media": media,
        "maior": maior,
        "menor": menor,
        "aprovados": aprovados,
        "reprovados": reprovados,
        "recuperacao": recuperacao
    }

def normalizar_notas(notas):
    if not notas:
        raise ValueError("Lista de notas vazia")
    
    for nota in notas:
        valida_nota(nota)
    
    media = sum(notas) / len(notas)
    
    variancia = sum((nota - media) ** 2 for nota in notas) / len(notas)
    desvio_padrao = variancia ** 0.5
    
    if desvio_padrao == 0:
        return [0.0] * len(notas)
    
    notas_normalizadas = [(nota - media) / desvio_padrao for nota in notas]
    
    return notas_normalizadas

class TestValidarNota:
    def test_nota_valida_inteira(self):
        assert valida_nota(0) == True
        assert valida_nota(5) == True
        assert valida_nota(10) == True

    def test_nota_invalida_negativa(self):
        with pytest.raises(ValueError):
            valida_nota(-1)

    def test_nota_invalida_acima(self):
        with pytest.raises(ValueError):
            valida_nota(11)

def test_calcular_estatisticas():
# ARRANGE - Preparar
    notas = [3, 5, 7, 9]

# ACT - Executar
    resultado = calcular_estatisticas(notas)

# ASSERT - Verificar
    assert resultado["media"] == 6.0
    assert resultado["maior"] == 9
    assert resultado["menor"] == 3
