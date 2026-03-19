"""
Repositorios para a calculadora.

Mantem compatibilidade com HistoricoRepositorio (ja existente) e adiciona
Repositorio, usado pelos testes desta atividade para persistir operacoes
com operandos/resultado. Comentarios vinculam ao checklist das 5 tarefas.
"""


class HistoricoRepositorio:
    """
    Repositorio legado, mantido para nao quebrar usos anteriores.
    Armazena entradas simples em lista.
    """

    def __init__(self):
        self._registros = []

    def salvar(self, entrada: str) -> None:
        self._registros.append(entrada)

    def listar(self) -> list:
        return self._registros

    def limpar(self) -> None:
        self._registros.clear()

    def total(self) -> int:
        return len(self._registros)


class Repositorio:
    """
    Repositorio especifico da atv06.
    Guarda dicionarios com operacao, operandos e resultado.
    """

    def __init__(self):
        # Estrutura interna: lista de dicionarios.
        self._historico = []

    def salvar_operacao(self, operacao, a, b, resultado):
        """Persiste uma operacao no historico (tarefas 1-3)."""
        self._historico.append({
            "operacao": operacao,
            "operandos": (a, b),
            "resultado": resultado,
        })

    def listar_historico(self):
        """
        Retorna copia defensiva do historico (tarefas 4-5: suporte a testes
        e cobertura sem expor estado mutavel).
        """
        return list(self._historico)
