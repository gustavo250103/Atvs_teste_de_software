# Teste de Software

Repositorio principal das atividades da disciplina de Teste de Software.

## Visao geral das atividades
- `atv01`: calculadora simples com testes unitarios em `pytest`.
- `atv02`: validacao e formatacao de CPF com testes em `pytest`.
- `atv03`: calculo de frete com classes de equivalencia, valores-limite e
  testes com `pytest` e `hypothesis`.
- `atv04`: sete exercicios sobre grafos de fluxo e complexidade ciclomatica,
  acompanhados de testes automatizados e arquivos explicativos dos grafos.
- `atv05`: testes de mutacao com `mutmut` usando Docker.
- `atv06`: projeto de calculadora com historico de operacoes, testes de
  unidade, integracao, doubles e cobertura.
- `atv07`: classe `Estoque` implementada com TDD, incluindo comentarios
  `RED`, `GREEN` e `REFACTOR` e mais de 10 testes.

## Estrutura do repositorio
```text
Atvs_teste_de_software_integracao-root/
|-- atv01/
|-- atv02/
|-- atv03/
|-- atv04/
|-- atv05/
|-- atv06/
|-- atv07/
`-- README.md
```

## Como rodar as atividades
Os comandos abaixo partem desta pasta.

### atv01
```powershell
cd .\atv01
python -m pytest -v
```

### atv02
```powershell
cd .\atv02
python -m pytest -v
```

### atv03
Se necessario, instale `hypothesis` antes da execucao.

```powershell
cd .\atv03
python -m pytest -v
```

### atv04
```powershell
cd .\atv04
python -m pytest -v
```

### atv05
Esta atividade possui um fluxo proprio com Docker e `mutmut`.
Consulte:

- [atv05/README.md](atv05/README.md)

### atv06
```powershell
cd .\atv06\projeto_calculadora
python -m unittest discover tests -v
```

Para gerar cobertura:

```powershell
python -m coverage run -m unittest discover tests
python -m coverage report -m
```

### atv07
Para ver cada teste individualmente com `PASSED` ou `FAILED`:

```powershell
cd .\atv07
python -m pytest -v
```

Para um resumo rapido:

```powershell
python -m pytest -q
```

## Dependencias e ferramentas
- `pytest`: usado em `atv01`, `atv02`, `atv03`, `atv04` e `atv07`.
- `hypothesis`: usado na `atv03`.
- `unittest` e `coverage`: usados na `atv06`.
- Docker + `mutmut`: usados na `atv05`.

## Arquivos de referencia
- [atv03/Atv03___Simulacao_e_Teste_de_Software.pdf](atv03/Atv03___Simulacao_e_Teste_de_Software.pdf)
- [atv04/README.md](atv04/README.md)
- [atv05/README.md](atv05/README.md)
- [atv06/projeto_calculadora/README.md](atv06/projeto_calculadora/README.md)
- [atv06/projeto_calculadora/relatorio.md](atv06/projeto_calculadora/relatorio.md)
- [atv07/README.md](atv07/README.md)

Autor: gustavo250103
