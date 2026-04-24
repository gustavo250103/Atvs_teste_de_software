"""Suite de testes de sistema para a API publica DummyJSON."""

import os
import warnings

import jsonschema
import pytest
import requests
import urllib3

# Configuracoes centrais da suite para evitar repeticao nos testes.
BASE_URL = "https://dummyjson.com"
REQUEST_TIMEOUT = 15
VERIFY_SSL = os.getenv("ATV08_VERIFY_SSL", "false").lower() == "true"

# Neste ambiente, a API e acessada por um proxy com certificado proprio.
if not VERIFY_SSL:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)

# Schema minimo do recurso usado para validar a estrutura do JSON retornado.
SCHEMA_PRODUTO = {
    "type": "object",
    "required": ["id", "title", "description", "category", "price"],
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "description": {"type": "string"},
        "category": {"type": "string"},
        "price": {"type": "number"},
        "brand": {"type": "string"},
    },
    "additionalProperties": True,
}

# Mantem a saida do pytest limpa quando o SSL e desativado no laboratorio.
pytestmark = pytest.mark.filterwarnings("ignore:Unverified HTTPS request")


def api_request(session, method, endpoint, **kwargs):
    """Envia requisicoes HTTP com timeout padrao e suporte ao proxy do laboratorio."""
    return session.request(
        method=method,
        url=f"{BASE_URL}{endpoint}",
        timeout=REQUEST_TIMEOUT,
        verify=VERIFY_SSL,
        **kwargs,
    )


@pytest.fixture(scope="session")
def api_session():
    """Cria uma sessao reutilizavel para toda a suite."""
    # Uma sessao reaproveita conexoes e deixa a suite mais simples e consistente.
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    return session


@pytest.fixture(scope="session")
def auth_headers(api_session):
    """Autentica na API e devolve o header Authorization para os testes protegidos."""
    # O token e obtido uma vez e compartilhado entre os testes autenticados.
    response = api_request(
        api_session,
        "POST",
        "/auth/login",
        json={
            "username": "emilys",
            "password": "emilyspass",
            "expiresInMins": 30,
        },
    )

    assert response.status_code == 200
    access_token = response.json()["accessToken"]
    return {"Authorization": f"Bearer {access_token}"}


@pytest.fixture
def novo_produto_payload():
    """Fornece dados validos para criacao de um produto de teste."""
    # Centralizar o payload facilita manutencao e evita duplicacao.
    return {
        "title": "Codex Recruiter Product",
        "description": "Produto criado durante a atividade de testes de API.",
        "price": 99.99,
        "brand": "Codex",
        "category": "beauty",
    }


# Testes de leitura: garantem status code, estrutura e comportamento para casos validos e invalidos.
def test_listar_produtos_retorna_lista_nao_vazia(api_session):
    """Valida que GET /products responde 200 e devolve uma colecao nao vazia."""
    response = api_request(api_session, "GET", "/products")

    assert response.status_code == 200
    body = response.json()
    assert "products" in body
    assert isinstance(body["products"], list)
    assert len(body["products"]) > 0


def test_obter_produto_existente_respeita_schema(api_session):
    """Valida que GET /products/1 responde 200 e segue o schema minimo esperado."""
    response = api_request(api_session, "GET", "/products/1")

    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=SCHEMA_PRODUTO)


def test_obter_produto_inexistente_retorna_404(api_session):
    """Valida que GET em recurso inexistente responde com status 404."""
    response = api_request(api_session, "GET", "/products/999999")

    assert response.status_code == 404


# Teste de criacao: verifica se a API aceita um POST valido e devolve identificador.
def test_criar_produto_retorna_201_e_id(api_session, novo_produto_payload):
    """Valida que POST /products/add cria um recurso e devolve um id."""
    response = api_request(
        api_session,
        "POST",
        "/products/add",
        json=novo_produto_payload,
    )

    assert response.status_code == 201
    body = response.json()
    assert "id" in body
    assert isinstance(body["id"], int)
    assert body["title"] == novo_produto_payload["title"]


# A DummyJSON simula escritas, por isso o update usa um recurso ja existente.
def test_atualizar_produto_com_patch_altera_campo(api_session):
    """Valida que PATCH /products/1 altera o campo enviado na resposta."""
    novo_titulo = "Produto atualizado pela suite"
    response = api_request(
        api_session,
        "PATCH",
        "/products/1",
        json={"title": novo_titulo},
    )

    assert response.status_code == 200
    assert response.json()["title"] == novo_titulo


# O delete tambem e simulado, mas ainda permite validar o contrato HTTP da operacao.
def test_deletar_produto_retorna_status_sucesso(api_session):
    """Valida que DELETE /products/1 responde com status de sucesso."""
    response = api_request(api_session, "DELETE", "/products/1")

    assert response.status_code in (200, 204)
    if response.status_code == 200:
        assert response.json()["isDeleted"] is True


# Teste negativo de validacao: payload incompleto deve ser rejeitado pela API.
def test_login_com_payload_invalido_retorna_4xx(api_session):
    """Valida que enviar dados invalidos ao login retorna erro 4xx."""
    response = api_request(
        api_session,
        "POST",
        "/auth/login",
        json={"username": "emilys"},
    )

    assert 400 <= response.status_code < 500


# Testes de autenticacao: comparam o comportamento do mesmo endpoint com e sem token.
def test_endpoint_autenticado_sem_credencial_retorna_401(api_session):
    """Valida que GET /auth/me sem credencial e bloqueado pela API."""
    response = api_request(api_session, "GET", "/auth/me")

    assert response.status_code == 401


def test_endpoint_autenticado_com_credencial_retorna_usuario(api_session, auth_headers):
    """Valida que GET /auth/me com bearer token responde com sucesso."""
    response = api_request(
        api_session,
        "GET",
        "/auth/me",
        headers=auth_headers,
    )

    assert response.status_code == 200
    body = response.json()
    assert body["username"] == "emilys"
    assert "email" in body


# Teste simples de performance para detectar degradacao grosseira de resposta.
def test_tempo_de_resposta_do_get_fica_abaixo_de_dois_segundos(api_session):
    """Valida que GET /products/1 responde em menos de 2 segundos."""
    response = api_request(api_session, "GET", "/products/1")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2.0
