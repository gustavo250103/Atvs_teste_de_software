from __future__ import annotations

from datetime import datetime
from enum import Enum, IntEnum


class Priority(IntEnum):
    """Prioridade numerica facilita comparacoes e futuras ordenacoes."""

    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    """Representa o ciclo de vida basico de uma tarefa."""

    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


class Task:
    """Entidade central do sistema.

    Ela guarda os dados da tarefa e protege duas regras de negocio:
    titulo minimo e prazo nao vencido.
    """

    def __init__(
        self,
        id: int | None,
        titulo: str,
        descricao: str,
        prioridade: Priority,
        prazo: datetime,
        status: Status = Status.PENDENTE,
    ) -> None:
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = self._coerce_prioridade(prioridade)
        self.prazo = prazo
        # O atributo interno evita que o status seja alterado sem passar pela
        # validacao da property.
        self._status = Status.PENDENTE
        self.status = status

    @property
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, value: Status) -> None:
        # O status so pode assumir valores do enum oficial do sistema.
        if not isinstance(value, Status):
            raise ValueError("Status invalido.")
        self._status = value

    def validar(self) -> None:
        """Aplica as regras minimas para uma tarefa ser considerada valida."""

        if not isinstance(self.titulo, str) or len(self.titulo.strip()) < 3:
            raise ValueError("O titulo deve ter pelo menos 3 caracteres.")
        if not isinstance(self.prazo, datetime):
            raise ValueError("O prazo deve ser um datetime valido.")
        # Compara com o momento atual para impedir criacao de tarefas vencidas.
        if self.prazo < datetime.now():
            raise ValueError("O prazo nao pode estar no passado.")

    @staticmethod
    def _coerce_prioridade(value: Priority) -> Priority:
        """Aceita o enum pronto ou um valor numerico compativel."""

        if isinstance(value, Priority):
            return value
        try:
            return Priority(value)
        except (TypeError, ValueError) as exc:
            raise ValueError("Prioridade invalida.") from exc
