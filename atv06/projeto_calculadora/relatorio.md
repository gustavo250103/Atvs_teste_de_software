# Relatorio

## Resultados dos testes
- Comando: `python -m unittest discover tests -v` (19/03/2026) -> 23 testes executados, todos aprovados.

## Cobertura de codigo
- Comando: `python -m coverage report -m`.
- Resultado total: 96% (188 statements, 8 nao cobertos).
- Arquivos da aplicacao: `src/calculadora.py` 90%; `src/repositorio.py` 83%; suites de teste 100%.
- Linhas nao cobertas: `src/calculadora.py:37-43` (ramo de compatibilidade com `salvar_operacao` nao exercitado nos testes atuais) e `src/repositorio.py:40,44,55` (classe Repositorio alternativa nao usada na suite).
- Justificativa: trechos nao cobertos pertencem a caminhos de compatibilidade mantidos para nao quebrar implementacoes anteriores, mas fora do fluxo principal.

## Bug encontrado e corrigido
- Defeito: `Calculadora.potencia` registrava a operacao com rotulo/operador incorreto no historico.
- Correcao: registro agora usa o operador `**` correto na string (arquivo `src/calculadora.py`). O teste mock de potencia captura regressao para esse problema.

## Reflexao: Stub vs Mock
- Stub: fornece respostas pre-programadas para isolar a logica sem dependencias externas (ex.: MagicMock usado como stub nos testes de unidade para retornar valores padrao do repositorio).
- Mock: verifica interacoes e argumentos (ex.: MagicMock nos testes de doubles conferindo chamadas a `salvar`, incluindo potencia e contagem de invocacoes).

## Relacao direta com as 5 tarefas solicitadas
1. Exemplos completos: testes antes marcados como "Implemente" foram escritos seguindo os padroes de assert e organizacao.
2. Testes extras por categoria: suites incluem tipagem invalida, limites numericos, valores fora do intervalo e verificacao de saida/historico.
3. Bug localizado com mock: o mock de potencia garante que o operador/rotulo esteja correto; ajuste aplicado no metodo `potencia`.
4. Medicao de cobertura documentada: comandos, porcentagens, linhas faltantes e justificativa registradas acima.
5. Relatorio preenchido: este arquivo consolida resultados, cobertura, bug corrigido e reflexao sobre doubles (stub vs mock).
