# Calculadora com Historico e Testes

Projeto da atividade de teste de software (atv06) com:
- Calculadora que registra historico de operacoes em um repositorio.
- Testes de unidade, integracao e doubles (stub/mock).
- Medicao de cobertura com `coverage.py`.

## Como executar

1) Instale dependencias (se necessario):
```
pip install -r requirements.txt
```
2) Rode todos os testes:
```
python -m unittest discover tests -v
```
3) Gere cobertura:
```
python -m coverage run -m unittest discover tests
python -m coverage report -m
python -m coverage html  # abre htmlcov/index.html
```

## Estrutura
- `src/` calculadora e repositorio (historico em memoria).
- `tests/` unidade, integracao e doubles (stub/mock).
- `relatorio.md` resumo da execucao, cobertura e bug corrigido.

## Tarefas atendidas
1. Exemplos completados: todos os testes marcados como "Implemente" foram escritos seguindo o padrao mostrado nas aulas (ver `tests/test_unidade.py`, `tests/test_integracao.py`, `tests/test_doubles.py`).
2. Testes extras: cada categoria (entrada/saida, tipagem, limites, valores fora do intervalo) ganhou ao menos um caso adicional, comentado nos proprios testes.
3. Bug encontrado e corrigido: `Calculadora.potencia` agora registra o operador/rotulo correto no historico; ver comentario no metodo em `src/calculadora.py` e teste mock correspondente.
4. Cobertura medida: 96% total na ultima execucao; detalhes e justificativa das linhas nao cobertas estao em `relatorio.md`.
5. Relatorio preenchido: resultados de testes, cobertura, bug corrigido e reflexao stub vs mock registrados em `relatorio.md`.
