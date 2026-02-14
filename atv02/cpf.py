"""Funções para validação e formatação de CPF.

Implementa:
- validar_cpf(cpf: str) -> bool
- formatar_cpf(cpf: str) -> str

Algoritmo de validação padrão do CPF brasileiro.
"""
from __future__ import annotations

import re


def _only_digits(cpf: str) -> str:
    return re.sub(r"\D", "", cpf)


def validar_cpf(cpf: str) -> bool:
    """Valida um CPF.

    Regras:
    - Deve conter exatamente 11 dígitos (após remover formatação).
    - Não pode ser uma sequência com todos os dígitos iguais.
    - Os dois dígitos verificadores devem bater com o cálculo padrão.

    Retorna True se válido, False caso contrário.
    """
    if cpf is None:
        return False

    num = _only_digits(cpf)
    if len(num) != 11:
        return False

    # sequências como 00000000000, 11111111111 são inválidas
    if num == num[0] * 11:
        return False

    try:
        digits = [int(c) for c in num]
    except ValueError:
        return False

    # calcula primeiro dígito verificador
    def _calc_verifier(digs: list[int], weights_start: int) -> int:
        s = 0
        w = weights_start
        for d in digs:
            s += d * w
            w -= 1
        r = s % 11
        return 0 if r < 2 else 11 - r

    v1 = _calc_verifier(digits[:9], 10)
    if v1 != digits[9]:
        return False

    v2 = _calc_verifier(digits[:10], 11)
    if v2 != digits[10]:
        return False

    return True


def formatar_cpf(cpf: str) -> str:
    """Recebe um CPF sem formatação e retorna no formato XXX.XXX.XXX-YY.

    Levanta ValueError se o CPF for inválido.
    """
    if cpf is None:
        raise ValueError("CPF inválido")

    num = _only_digits(cpf)
    if len(num) != 11 or not validar_cpf(num):
        raise ValueError("CPF inválido")

    return f"{num[0:3]}.{num[3:6]}.{num[6:9]}-{num[9:11]}"


__all__ = ["validar_cpf", "formatar_cpf"]
