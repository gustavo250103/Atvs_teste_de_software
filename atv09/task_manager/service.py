from __future__ import annotations

from datetime import datetime

from .repository import TaskRepository
from .task import Priority, Status, Task


class TaskService:
    """Camada de servico usada como bonus.

    Ela concentra fluxos de uso mais proximos da aplicacao, deixando o dominio e
    a persistencia separados.
    """

    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def criar_tarefa(
        self,
        titulo: str,
        descricao: str,
        prioridade: Priority,
        prazo: datetime,
    ) -> Task:
        # O servico monta a tarefa, valida e so entao persiste.
        task = Task(None, titulo, descricao, prioridade, prazo)
        task.validar()
        return self.repository.save(task)

    def listar_todas(self) -> list[Task]:
        return self.repository.find_all()

    def atualizar_status(self, id: int, status: Status) -> Task:
        # A atualizacao depende de a tarefa existir primeiro.
        task = self.repository.find_by_id(id)
        if task is None:
            raise ValueError("Tarefa nao encontrada.")
        task.status = status
        return task
