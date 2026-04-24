# atv07 - Estoque com TDD

## Objetivo
Esta atividade implementa a classe `Estoque` em Python seguindo a metodologia
TDD (Test-Driven Development). A ideia central foi escrever os testes primeiro,
ver a falha acontecer (`RED`), implementar o minimo necessario para passar
(`GREEN`) e, por fim, melhorar o codigo sem alterar o comportamento
(`REFACTOR`).

## Enunciado resumido
Implementar as seguintes operacoes:

1. `adicionar_produto(nome, quantidade)`
2. `remover_produto(nome, quantidade)`
3. `consultar_quantidade(nome)`
4. `listar_produtos()`
5. `produto_mais_estocado()`

## Regras de negocio
- Nao e permitido adicionar ou remover quantidade menor ou igual a zero.
- Nao e permitido remover mais unidades do que o disponivel.
- Adicionar um produto ja existente incrementa a quantidade, e nao substitui.
- `consultar_quantidade(nome)` retorna `0` para produto inexistente.
- `listar_produtos()` retorna apenas produtos com quantidade maior que zero.
- `produto_mais_estocado()` retorna `None` quando o estoque esta vazio.

## Requisitos atendidos
- `estoque.py` contem a classe `Estoque`.
- `test_estoque.py` contem a suite de testes automatizados.
- A atividade possui mais de 10 testes.
- Os comentarios `RED`, `GREEN` e `REFACTOR` aparecem no codigo para evidenciar
  os ciclos do TDD.
- Ao final, todos os testes passam.

## Estrutura da pasta
```text
atv07/
|-- README.md
|-- estoque.py
|-- test_estoque.py
`-- pytest.ini
```

### Papel de cada arquivo
- `estoque.py`: implementacao da classe `Estoque`.
- `test_estoque.py`: testes automatizados com `pytest`.
- `pytest.ini`: configuracao do `pytest` para uma execucao previsivel neste
  ambiente.
- `README.md`: documentacao da atividade.

## Como o codigo foi organizado
O estoque foi modelado com um dicionario Python simples:

- chave: nome do produto;
- valor: quantidade disponivel.

Essa escolha deixa a implementacao facil de explicar:

- consultar quantidade e um acesso direto ao dicionario;
- adicionar produto soma a quantidade atual com a nova entrada;
- remover produto valida o saldo antes de atualizar;
- listar produtos considera apenas itens com saldo positivo;
- produto mais estocado usa a maior quantidade entre os itens disponiveis.

Na etapa de refatoracao, duas regras repetidas foram extraidas para metodos
auxiliares:

- `_validar_quantidade_positiva()`: evita duplicacao na validacao das entradas.
- `_produtos_com_saldo()`: concentra a regra de quais produtos devem ser
  considerados nas consultas agregadas.

## Evidencia do TDD
O projeto deixa o ciclo de TDD visivel nos comentarios do codigo:

- `RED`: aparece em `test_estoque.py`, onde cada comportamento e descrito antes
  da implementacao.
- `GREEN`: aparece em `estoque.py`, marcando a implementacao minima para fazer
  os testes passarem.
- `REFACTOR`: aparece quando a validacao e a filtragem de produtos foram
  extraidas para metodos auxiliares.

## Requisitos para executar
- Python 3 instalado.
- `pytest` instalado no ambiente.

Se precisar instalar o `pytest`:

```powershell
python -m pip install pytest
```

## Como rodar os testes
Entre na pasta da atividade:

```powershell
cd C:\Users\51069303\Atvs_teste_de_software\Atvs_teste_de_software_integracao-root\atv07
```

### Rodar a suite completa
Mostra apenas o resumo final:

```powershell
python -m pytest -q
```

### Ver cada teste individualmente
Mostra item por item com `PASSED` ou `FAILED`:

```powershell
python -m pytest -v
```

Se quiser uma saida ainda mais detalhada:

```powershell
python -m pytest -vv -rA
```

## Exemplo de saida esperada
Executando `python -m pytest -v`, a saida deve ficar semelhante a esta:

```text
test_estoque.py::test_consultar_produto_inexistente_retorna_zero PASSED
test_estoque.py::test_adicionar_produto_novo_registra_quantidade PASSED
test_estoque.py::test_adicionar_produto_existente_incrementa_quantidade PASSED
test_estoque.py::test_adicionar_produto_com_quantidade_invalida_gera_erro[0] PASSED
test_estoque.py::test_adicionar_produto_com_quantidade_invalida_gera_erro[-3] PASSED
test_estoque.py::test_remover_produto_reduz_quantidade_disponivel PASSED
test_estoque.py::test_remover_produto_maior_que_disponivel_gera_erro PASSED
test_estoque.py::test_remover_produto_com_quantidade_invalida_gera_erro[0] PASSED
test_estoque.py::test_remover_produto_com_quantidade_invalida_gera_erro[-2] PASSED
test_estoque.py::test_listar_produtos_retorna_apenas_itens_com_saldo_positivo PASSED
test_estoque.py::test_listar_produtos_em_estoque_vazio_retorna_lista_vazia PASSED
test_estoque.py::test_produto_mais_estocado_retorna_nome_com_maior_quantidade PASSED
test_estoque.py::test_produto_mais_estocado_em_estoque_vazio_retorna_none PASSED
```
  