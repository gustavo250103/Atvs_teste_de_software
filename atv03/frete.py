"""Cálculo de frete segundo regras fornecidas na aula 03.

Regime resumido:
- Até 1 kg -> R$10
- 1 a 5 kg -> R$15
- 5 a 20 kg -> R$25
- >20 kg ou peso <= 0 -> erro
- Destino: mesma_regiao (x1), outra_regiao (x1.5), internacional (x2)
- Pedido acima de R$200 -> frete grátis (0.0)
"""

from __future__ import annotations

from typing import Final

_DEST_MULTIPLIERS: Final = {
    "mesma_regiao": 1.0,
    "outra_regiao": 1.5,
    "internacional": 2.0,
}


def _base_por_peso(peso: float) -> float:
    """Retorna o valor base sem acréscimos para o peso informado."""
    if peso <= 0:
        raise ValueError("peso deve ser positivo")
    if peso <= 1:
        return 10.0
    if peso <= 5:
        return 15.0
    if peso <= 20:
        return 25.0
    raise ValueError("peso acima de 20 kg não é aceito")


def calcular_frete(peso: float, destino: str, valor_pedido: float) -> float:
    """Calcula o frete conforme regras.

    Parâmetros
    ----------
    peso : float
        Peso do pacote em kg. Deve ser >0 e <=20.
    destino : str
        Um de: 'mesma_regiao', 'outra_regiao', 'internacional'.
    valor_pedido : float
        Valor total do pedido. Se >200, frete é grátis.

    Retorna
    -------
    float
        Valor do frete. Lança ValueError para entradas inválidas.
    """

    if valor_pedido is None or destino is None:
        raise ValueError("parâmetros obrigatórios faltando")

    if valor_pedido < 0:
        raise ValueError("valor_pedido não pode ser negativo")

    destino_norm = destino.strip().lower()
    if destino_norm not in _DEST_MULTIPLIERS:
        raise ValueError("destino inválido")

    # Valida peso antes de aplicar gratuidades.
    base = _base_por_peso(float(peso))

    # Frete grátis se pedido excede R$200.
    if valor_pedido > 200:
        return 0.0

    return base * _DEST_MULTIPLIERS[destino_norm]


__all__ = ["calcular_frete"]
