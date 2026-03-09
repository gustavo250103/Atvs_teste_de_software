# Teste de Software

Repositorio da disciplina de Teste de Software.

Atividades concluidas ate 09/03/2026:
- `atv01`: Calculadora com testes unitarios usando `pytest`.
- `atv02`: Validacao/formatacao de CPF com testes `pytest`.
- `atv03`: Calculo de frete com classes de equivalencia, valores-limite e testes `pytest` + `hypothesis`.
- `atv04`: Sete exercicios sobre grafos de fluxo e complexidade ciclomatica (`ex01` a `ex07`, com arquivos `ex0X_graph.md`), validados por `pytest` (`test01.py` a `test07.py`).

Como rodar os testes (partindo desta pasta):
1) (Opcional) Crie/ative um venv e instale dependencias basicas: `pip install -r atv01/requirements.txt` e, se preciso, `pip install hypothesis`.
2) Rode os testes de cada atividade:
   - `cd atv01` && `pytest -v`
   - `cd atv02` && `pytest -v`
   - `cd atv03` && `pytest -v`
   - `cd atv04` && `pytest -v`

Arquivos de referencia:
- `atv03/Atv03___Simulacao_e_Teste_de_Software.pdf`
- `atv04/ex0X_graph.md` (explicacao dos grafos e caminhos)

Autor: gustavo250103
