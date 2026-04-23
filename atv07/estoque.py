"""Implementacao de um estoque simples orientado a TDD.

O objetivo desta classe e manter um cadastro minimo de produtos e quantidades,
aplicando as regras de negocio definidas na atividade.
"""


class Estoque:
    """Representa um estoque simples usando um dicionario interno.

    A chave do dicionario e o nome do produto.
    O valor associado a cada chave e a quantidade disponivel.
    """

    # CICLO 1 - GREEN: estrutura minima para consultar e adicionar produtos.
    def __init__(self):
        # Estrutura central do dominio: nome do produto -> quantidade em estoque.
        self._produtos = {}

    # REFACTOR: centraliza a regra de negocio para quantidades validas.
    def _validar_quantidade_positiva(self, quantidade):
        """Garante que operacoes de entrada e saida usem quantidade positiva."""
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")

    # REFACTOR: concentra a nocao de produtos realmente disponiveis no estoque.
    def _produtos_com_saldo(self):
        """Retorna apenas os produtos cuja quantidade atual e maior que zero."""
        return {nome: quantidade for nome, quantidade in self._produtos.items() if quantidade > 0}

    # CICLO 1 - GREEN: adicionar incrementa a quantidade do produto existente.
    def adicionar_produto(self, nome, quantidade):
        """Adiciona um produto novo ou soma quantidade a um produto ja existente."""
        self._validar_quantidade_positiva(quantidade)
        self._produtos[nome] = self._produtos.get(nome, 0) + quantidade

    # CICLO 2 - GREEN: remover exige saldo suficiente e elimina o item quando zera.
    def remover_produto(self, nome, quantidade):
        """Remove unidades de um produto, sem permitir saldo negativo."""
        self._validar_quantidade_positiva(quantidade)

        if quantidade > self.consultar_quantidade(nome):
            raise ValueError("Quantidade indisponivel para remocao.")

        saldo_restante = self.consultar_quantidade(nome) - quantidade

        if saldo_restante == 0:
            # Ao zerar o saldo, removemos a chave para manter a listagem limpa.
            self._produtos.pop(nome, None)
            return

        self._produtos[nome] = saldo_restante

    # CICLO 1 - GREEN: consultar produto inexistente devolve zero.
    def consultar_quantidade(self, nome):
        """Consulta a quantidade atual de um produto.

        Se o produto ainda nao existir, o retorno e 0.
        """
        return self._produtos.get(nome, 0)

    # CICLO 3 - GREEN: apenas produtos com saldo positivo entram na listagem.
    def listar_produtos(self):
        """Lista somente os produtos que ainda possuem saldo disponivel."""
        return list(self._produtos_com_saldo().keys())

    # CICLO 3 - GREEN: quando nao ha saldo disponivel, o retorno deve ser None.
    def produto_mais_estocado(self):
        """Retorna o nome do produto com maior quantidade em estoque."""
        produtos_com_saldo = self._produtos_com_saldo()
        if not produtos_com_saldo:
            return None

        return max(produtos_com_saldo, key=produtos_com_saldo.get)
