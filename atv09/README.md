# atv09 - Sistema Task Manager

## Descricao
Esta atividade implementa um sistema simples de gerenciamento de tarefas em
Python, alinhado ao enunciado da Aula 09. O foco principal e demonstrar:

- testes de estado;
- setup com fixtures do `pytest`;
- isolamento de dependencias com stub e mock;
- interacao entre metodos;
- ciclo de vida do objeto.

O projeto contem a classe `Task`, um armazenamento em memoria
(`InMemoryStorage`), um repositorio (`TaskRepository`) e um `TaskService` como
bonus.

## Estrutura do projeto
```text
atv09/
|-- README.md
|-- pytest.ini
|-- requirements.txt
|-- task_manager/
|   |-- __init__.py
|   |-- repository.py
|   |-- service.py
|   |-- storage.py
|   `-- task.py
`-- tests/
    |-- test_repository.py
    `-- test_task.py
```

## Componentes implementados
### `task_manager/task.py`
- Enum `Priority` com `BAIXA`, `MEDIA` e `ALTA`.
- Enum `Status` com `PENDENTE`, `EM_PROGRESSO` e `CONCLUIDA`.
- Classe `Task` com os atributos:
  - `id`
  - `titulo`
  - `descricao`
  - `prioridade`
  - `prazo`
  - `status` com valor padrao `PENDENTE`
- Metodo `validar()` para garantir:
  - titulo com pelo menos 3 caracteres;
  - prazo diferente de uma data passada.

### `task_manager/storage.py`
Classe `InMemoryStorage` com:
- `add(id, item)`
- `get(id)`
- `get_all()`
- `delete(id)`
- `clear()`

### `task_manager/repository.py`
Classe `TaskRepository` com:
- `save(task)`
- `find_by_id(id)`
- `find_all()`
- `delete(id)`

### `task_manager/service.py` (bonus)
Classe `TaskService` com:
- `criar_tarefa(...)`
- `listar_todas()`
- `atualizar_status(id, status)`

## Testes implementados
### `tests/test_task.py`
Suite de testes unitarios da classe `Task`:

1. verifica estado inicial e status padrao;
2. valida titulo invalido;
3. valida prazo no passado;
4. verifica transicao valida de status;
5. verifica transicao invalida de status.

### `tests/test_repository.py`
Suite de testes de componente da classe `TaskRepository`, com a dependencia
`storage` mockada:

1. `save()` atribui ID;
2. `save()` chama `storage.add()` uma vez;
3. `find_by_id()` usa o retorno configurado no mock (`stub`);
4. sequencia `save()` + `find_by_id()` recupera a mesma tarefa;
5. `find_all()` retorna lista vazia quando o storage esta vazio;
6. `delete()` delega corretamente ao storage.

## Instalacao
Dentro da pasta `atv09`, instale as dependencias com:

```powershell
pip install -r requirements.txt
```

## Como testar
Entre na pasta da atividade:

```powershell
cd C:\Users\51069303\Atvs_teste_de_software\Atvs_teste_de_software_integracao-root\atv09
```

Execute a suite com:

```powershell
pytest -v
```

O projeto inclui um `pytest.ini` que desativa apenas o cache provider para evitar
warnings de permissao neste ambiente Windows.

Cobertura opcional:

```powershell
pytest --cov=task_manager
```

## Relacao com a Aula 09
- `test_task.py` cobre teste unitario, estado e ciclo de vida sem mocks.
- `test_repository.py` cobre teste de componente com dependencia externa
  isolada por mock.
- Fixtures do `pytest` reduzem repeticao e servem como setup para cada teste.
- `return_value` e usado como stub quando so importa o valor devolvido.
- `assert_called_once_with()` valida a interacao com a dependencia mockada.
