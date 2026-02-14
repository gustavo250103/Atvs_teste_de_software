import pytest

from cpf import validar_cpf, formatar_cpf


@pytest.fixture
def cpfs_validos():
    return [
        ("52998224725", "529.982.247-25"),
        ("12345678909", "123.456.789-09"),
        ("529.982.247-25", "529.982.247-25"),
        ("123.456.789-09", "123.456.789-09"),
    ]


@pytest.fixture
def cpfs_invalidos():
    return [
        "11111111111",
        "00000000000",
        "123",
        "12345678900",
    ]


@pytest.mark.parametrize("cpf,expected_fmt", [
    ("52998224725", "529.982.247-25"),
    ("12345678909", "123.456.789-09"),
])
def test_validar_e_formatar_parametrizado(cpf, expected_fmt):
    # Arrange (dados da parametrização)
    # Act
    is_valid = validar_cpf(cpf)
    formatted = formatar_cpf(cpf)
    # Assert
    assert is_valid is True
    assert formatted == expected_fmt


import pytest

from cpf import validar_cpf, formatar_cpf


def _cria_cpf_valido_de_base(base_nove: str) -> str:
    """Gera CPF válido (11 dígitos) a partir de 9 dígitos de entrada."""
    assert len(base_nove) == 9 and base_nove.isdigit()
    digitos = [int(c) for c in base_nove]

    def calcula(digs_list, inicio):
        soma = sum(d * w for d, w in zip(digs_list, range(inicio, 1, -1)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    v1 = calcula(digitos, 10)
    v2 = calcula(digitos + [v1], 11)
    return f"{base_nove}{v1}{v2}"


# Fixtures
@pytest.fixture
def cpfs_validos():
    """Lista com CPF válido padrão e CPF válido contendo zeros."""
    return [
        "52998224725",  # CPF válido padrão
        _cria_cpf_valido_de_base("001002003"),  # CPF válido com zeros
    ]


@pytest.fixture
def cpfs_invalidos():
    """Lista com exemplos de CPFs inválidos por vários motivos."""
    return [
        "12345678900",  # dígitos verificadores errados
        "11111111111",  # todos dígitos iguais
        "123",  # menos de 11
        "123456789012",  # mais de 11
        "123abc45678",  # contém letras
    ]


# Testes solicitados (cada teste tem breve explicação em português)

def test_cpf_valido_padrao(cpfs_validos):
    """CPF válido padrão: valida que o CPF conhecido é considerado válido."""
    cpf_teste = cpfs_validos[0]
    resultado = validar_cpf(cpf_teste)
    assert resultado is True


def test_cpf_valido_com_zeros(cpfs_validos):
    """CPF válido com zeros: valida CPFs com zeros à esquerda/na base."""
    cpf_teste = cpfs_validos[1]
    resultado = validar_cpf(cpf_teste)
    assert resultado is True


def test_cpf_invalido_digitos_verificadores_errados():
    """CPF inválido: dígitos verificadores incorretos devem falhar."""
    cpf_teste = "12345678900"
    resultado = validar_cpf(cpf_teste)
    assert resultado is False


def test_cpf_com_todos_digitos_iguais():
    """CPF com todos os dígitos iguais (ex.: 111.111.111-11) é inválido."""
    cpf_teste = "11111111111"
    resultado = validar_cpf(cpf_teste)
    assert resultado is False


def test_cpf_com_menos_de_11_digitos():
    """CPF com menos de 11 dígitos deve ser inválido."""
    cpf_teste = "123"
    resultado = validar_cpf(cpf_teste)
    assert resultado is False


def test_cpf_com_mais_de_11_digitos():
    """CPF com mais de 11 dígitos deve ser inválido."""
    cpf_teste = "123456789012"
    resultado = validar_cpf(cpf_teste)
    assert resultado is False


def test_cpf_com_letras():
    """CPF contendo letras deve ser tratado como inválido."""
    cpf_teste = "123abc45678"
    resultado = validar_cpf(cpf_teste)
    assert resultado is False


def test_formatacao_cpf_valido(cpfs_validos):
    """Formatação: formata corretamente um CPF válido."""
    cpf_teste = cpfs_validos[0]
    formatado = formatar_cpf(cpf_teste)
    assert formatado == "529.982.247-25"


def test_formatacao_cpf_invalido_levanta_excecao(cpfs_invalidos):
    """Formatação inválida: formatar_cpf deve levantar ValueError para CPF inválido."""
    with pytest.raises(ValueError):
        formatar_cpf(cpfs_invalidos[0])


def test_cpf_none_ou_string_vazia():
    """Entrada None ou string vazia: validar retorna False e formatar levanta ValueError."""
    assert validar_cpf(None) is False
    assert validar_cpf("") is False
    with pytest.raises(ValueError):
        formatar_cpf(None)
    with pytest.raises(ValueError):
        formatar_cpf("")

