from datetime import datetime, timedelta

import pytest

from task_manager.repository import TaskRepository
from task_manager.task import Priority, Task


@pytest.fixture
def mock_storage(mocker):
    # Dependencia externa isolada por mock para testar so o repositorio.
    return mocker.Mock()


@pytest.fixture
def repo(mock_storage):
    return TaskRepository(mock_storage)


@pytest.fixture
def task():
    # Tarefa de apoio para os testes de componente do repositorio.
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Teste", "Descricao", Priority.BAIXA, prazo)


def test_save_atribui_id(repo, task):
    # Teste de estado: o save precisa alterar o id do objeto.
    resultado = repo.save(task)

    assert resultado.id == 1


def test_save_chama_storage_add(repo, task, mock_storage):
    # Teste de interacao: garante que a colaboracao com o storage aconteceu.
    repo.save(task)

    mock_storage.add.assert_called_once_with(1, task)


def test_find_by_id_usa_storage(repo, task, mock_storage):
    # Stub: interessa apenas o retorno configurado do get.
    mock_storage.get.return_value = task

    resultado = repo.find_by_id(1)

    assert resultado is task
    mock_storage.get.assert_called_once_with(1)


def test_save_seguido_de_find_by_id_recupera_mesma_task(repo, task, mock_storage):
    # Esse dicionario simula um armazenamento simples em memoria.
    armazenadas = {}

    def adicionar(id, item):
        armazenadas[id] = item

    def buscar(id):
        return armazenadas.get(id)

    mock_storage.add.side_effect = adicionar
    mock_storage.get.side_effect = buscar

    # Aqui o foco e a sequencia: salvar primeiro para depois buscar.
    task_salva = repo.save(task)
    resultado = repo.find_by_id(task_salva.id)

    assert resultado is task
    assert resultado.id == 1


def test_find_all_retorna_lista_vazia_quando_storage_sem_itens(repo, mock_storage):
    # Quando nao ha dados, o repositorio deve devolver uma lista vazia.
    mock_storage.get_all.return_value = []

    resultado = repo.find_all()

    assert resultado == []


def test_delete_delega_para_storage(repo, mock_storage):
    # A responsabilidade do repositorio aqui e apenas repassar a operacao.
    mock_storage.delete.return_value = True

    resultado = repo.delete(1)

    assert resultado is True
    mock_storage.delete.assert_called_once_with(1)
