# atv08 - Suite de Testes para API REST

## API escolhida
- **DummyJSON**
- Documentacao oficial: https://dummyjson.com/docs

## Justificativa da escolha
Escolhi a DummyJSON porque ela combina tres pontos que deixam o projeto mais
forte para portfolio:

1. possui endpoints documentados de CRUD para recursos como `products`;
2. possui autenticacao real por bearer token em `/auth/login` e `/auth/me`;
3. responde com status codes coerentes para a maior parte dos cenarios da
   atividade, o que permite montar uma suite objetiva e demonstravel.

Ela tambem e uma API conhecida no ecossistema frontend/backend, o que ajuda a
deixar o projeto facil de entender por recrutadores.

## Observacao importante sobre a API
Os endpoints de escrita da DummyJSON sao simulados. Isso significa que:

- `POST /products/add` retorna `201` e um novo objeto com `id`;
- `PATCH`, `PUT` e `DELETE` retornam o recurso modificado/deletado na resposta;
- a alteracao nao fica persistida no servidor.

Por isso, a suite cria produto em um teste especifico de `CREATE` e usa o
produto existente `id=1` para os testes de `UPDATE` e `DELETE`.

## Estrutura da pasta
```text
atv08/
|-- README.md
|-- requirements.txt
`-- test_api.py
```

## Dependencias
O arquivo `requirements.txt` contem exatamente:

```text
requests
pytest
jsonschema
```

## Instalacao
### Linux / Mac
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Execucao
Rodar a suite com saida detalhada:

```powershell
pytest test_api.py -v
```

Gerar um relatorio simples em arquivo:

```powershell
pytest test_api.py -v > resultado.txt
```

## Sobre SSL no ambiente
No ambiente em que esta atividade foi montada havia um proxy com certificado
proprio. Por isso, a suite deixa a verificacao SSL desativada por padrao para
garantir execucao estavel contra a API publica.

Se o seu ambiente confia normalmente nos certificados HTTPS, voce pode ativar a
verificacao exportando a variavel abaixo antes de rodar os testes:

### Linux / Mac
```bash
export ATV08_VERIFY_SSL=true
```

### Windows PowerShell
```powershell
$env:ATV08_VERIFY_SSL = "true"
```

## Testes implementados
1. `GET /products` retorna `200` e uma lista de produtos nao vazia.
2. `GET /products/1` retorna `200` e o JSON e validado com `jsonschema`.
3. `GET /products/999999` retorna `404`.
4. `POST /products/add` retorna `201` e devolve `id` no corpo.
5. `PATCH /products/1` retorna `200` e mostra o campo atualizado.
6. `DELETE /products/1` retorna status de sucesso (`200`).
7. `POST /auth/login` com payload invalido retorna erro `4xx`.
8. `GET /auth/me` sem credencial retorna `401`.
9. `GET /auth/me` com bearer token valido retorna `200`.
10. `GET /products/1` responde em menos de `2.0` segundos.

## Fixtures usadas
- `api_session`: reaproveita uma sessao HTTP para toda a suite.
- `auth_headers`: autentica uma vez e fornece o header `Authorization`.
- `novo_produto_payload`: centraliza o payload usado no teste de criacao.
