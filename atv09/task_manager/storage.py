from __future__ import annotations


class InMemoryStorage:
    """Camada simples de armazenamento em memoria.

    Ela existe para separar persistencia da regra de negocio.
    """

    def __init__(self) -> None:
        # Dicionario privado para simular um banco sem dependencias externas.
        self._data: dict[int, object] = {}

    def add(self, id: int, item: object) -> None:
        """Salva ou sobrescreve um item usando o id como chave."""

        self._data[id] = item

    def get(self, id: int) -> object | None:
        """Retorna um item especifico ou None quando ele nao existe."""

        return self._data.get(id)

    def get_all(self) -> list[object]:
        """Devolve apenas os valores, que sao os objetos persistidos."""

        return list(self._data.values())

    def delete(self, id: int) -> bool:
        """Remove um item e informa se a exclusao realmente aconteceu."""

        if id not in self._data:
            return False
        del self._data[id]
        return True

    def clear(self) -> None:
        """Esvazia todo o armazenamento."""

        self._data.clear()
