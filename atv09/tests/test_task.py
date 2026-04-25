from datetime import datetime, timedelta

import pytest

from task_manager.task import Priority, Status, Task


@pytest.fixture
def task_valida():
    # Fixture de setup: entrega uma tarefa pronta para varios testes.
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python", Priority.ALTA, prazo)


def test_estado_inicial(task_valida):
    # Teste de estado: confere como o objeto nasce apos a criacao.
    task_valida.validar()

    assert task_valida.id is None
    assert task_valida.titulo == "Estudar"
    assert task_valida.descricao == "Python"
    assert task_valida.prioridade == Priority.ALTA
    assert task_valida.status == Status.PENDENTE


def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Descricao", Priority.BAIXA, prazo)

    # pytest.raises deixa explicito o contrato esperado para entrada invalida.
    with pytest.raises(ValueError):
        task.validar()


def test_prazo_no_passado():
    prazo = datetime.now() - timedelta(days=1)
    task = Task(None, "Estudar", "Descricao", Priority.MEDIA, prazo)

    with pytest.raises(ValueError):
        task.validar()


def test_ciclo_vida_transicao_valida(task_valida):
    # O estado da tarefa deve mudar quando a transicao e permitida.
    task_valida.status = Status.EM_PROGRESSO

    assert task_valida.status == Status.EM_PROGRESSO


def test_ciclo_vida_transicao_invalida(task_valida):
    # Valor fora do enum deve ser rejeitado para proteger o ciclo de vida.
    with pytest.raises(ValueError):
        task_valida.status = "arquivada"
