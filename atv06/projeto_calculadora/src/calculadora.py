"""
Calculadora com persistencia de historico (atv06).

Mapa para as 5 tarefas:
1) Exemplos completados: metodos para todas as operacoes basicas + potencia.
2) Testes extras: validacao de tipos, limites e historico centralizados.
3) Bug corrigido: registro da potencia usa o operador correto na string.
4) Cobertura: caminhos de sucesso/erro expostos para coverage.py.
5) Relatorio: comentarios no codigo explicam escolhas para apresentacao.
"""


class Calculadora:
    def __init__(self, repositorio):
        # Injecao de dependencia: aceita HistoricoRepositorio, MagicMock ou stub.
        self.repositorio = repositorio
        self.resultado = 0

    def _validar_operandos(self, a, b):
        """
        Rejeita tipos invalidos.
        - bool precisa ser recusado (subclasse de int) conforme testes de tipagem.
        - Aceita int ou float; demais levantam TypeError.
        """
        for valor in (a, b):
            if isinstance(valor, bool) or not isinstance(valor, (int, float)):
                raise TypeError("Argumentos devem ser numeros")

    def _registrar(self, expressao):
        """
        Centraliza a escrita no historico.
        HistoricoRepositorio e mocks usam metodo salvar(texto).
        (Compatibilidade opcional com salvar_operacao se existir.)
        """
        if hasattr(self.repositorio, "salvar"):
            self.repositorio.salvar(expressao)
        elif hasattr(self.repositorio, "salvar_operacao"):
            # Mantem compatibilidade com Repositorio anterior (dicionario).
            op, resto = expressao.split(" ", 1)
            # Expressao no formato "a op b = r"
            partes = expressao.split()
            a, operador, b, _, resultado = partes[0], partes[1], partes[2], partes[3], partes[4]
            self.repositorio.salvar_operacao(op, float(a), float(b), float(resultado))

    def somar(self, a, b):
        self._validar_operandos(a, b)
        resultado = a + b
        self._registrar(f"{a} + {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def subtrair(self, a, b):
        self._validar_operandos(a, b)
        resultado = a - b
        self._registrar(f"{a} - {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def multiplicar(self, a, b):
        self._validar_operandos(a, b)
        resultado = a * b
        self._registrar(f"{a} * {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def dividir(self, a, b):
        self._validar_operandos(a, b)
        if b == 0:
            # Caminho de erro testado em unidade/integracao.
            raise ValueError("Divisao por zero nao permitida")
        resultado = a / b
        self._registrar(f"{a} / {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def potencia(self, base, expoente):
        """
        Corrige o bug intencional: operador e rotulo corretos na string
        (era alvo dos testes mock). Usa ** em vez de outro simbolo.
        """
        self._validar_operandos(base, expoente)
        resultado = base ** expoente
        self._registrar(f"{base} ** {expoente} = {resultado}")
        self.resultado = resultado
        return resultado

    def obter_ultimo_resultado(self):
        """Retorna o ultimo resultado calculado (usado em integracao)."""
        return self.resultado
