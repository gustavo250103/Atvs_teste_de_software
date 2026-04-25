from __future__ import annotations

from .task import Task


class TaskRepository:
    """Coordena a persistencia das tarefas.

    O repositorio conhece a regra de atribuicao de IDs e delega o armazenamento
    para um colaborador externo.
    """

    def __init__(self, storage) -> None:
        self.storage = storage
        # Simula um auto-incremento simples, suficiente para a atividade.
        self._next_id = 1

    def save(self, task: Task) -> Task:
        """Atribui um novo id, persiste a tarefa e devolve o mesmo objeto."""

        task.id = self._next_id
        self._next_id += 1
        self.storage.add(task.id, task)
        return task

    def find_by_id(self, id: int) -> Task | None:
        """Busca uma tarefa especifica delegando a consulta ao storage."""

        return self.storage.get(id)

    def find_all(self) -> list[Task]:
        """Normaliza o retorno do storage para sempre entregar uma lista."""

        tasks = self.storage.get_all()
        if tasks is None:
            return []
        return list(tasks)

    def delete(self, id: int) -> bool:
        """Remove a tarefa pelo id e retorna o resultado da operacao."""

        return self.storage.delete(id)
