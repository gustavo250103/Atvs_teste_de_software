# Guia (atv05) – testes de mutação com mutmut via Docker

## Visão geral
- Código exercitado: `calculadora.py` (somar, subtrair, multiplicar, dividir).
- Testes: `test_calculadora.py` (inclui checagem da mensagem de erro na divisão por zero).
- Configuração: `pyproject.toml` (alvo de mutação e comando de testes).
- Saída/cache do mutmut: pasta `mutants/` (gerada automaticamente; pode ser ignorada/limpa).

## Por que Docker
- O mutmut depende de Linux; o Docker fornece esse ambiente sem precisar de WSL/admin.
- A imagem `mutmut-runner` já vem com Python 3.12 + mutmut + pytest, deixando as execuções seguintes mais rápidas.

## Sequência para rodar tudo (PowerShell)
1) Ir para a raiz do repositório  
   ```
   cd C:\Users\51069303\Atvs_teste_de_software\Atvs_teste_de_software_integracao-root
   ```
2) Construir a imagem (uma vez)  
   ```
   @"
   FROM python:3.12-slim
   RUN pip install --no-cache-dir mutmut pytest
   WORKDIR /workspace
   "@ | docker build -t mutmut-runner -f - .
   ```
3) Entrar na pasta do exercício  
   ```
   cd atv05
   ```
4) Rodar mutação  
   ```
   docker run --rm -v ${PWD}:/workspace -w /workspace mutmut-runner mutmut run
   ```
5) Ver o resumo  
   ```
   docker run --rm -v ${PWD}:/workspace -w /workspace mutmut-runner mutmut results
   ```
6) Se houver sobreviventes, inspecionar um id  
   ```
   docker run --rm -v ${PWD}:/workspace -w /workspace mutmut-runner mutmut show <id>
   ```

## Como funciona
- `-v ${PWD}:/workspace` monta a pasta atual dentro do container.
- `-w /workspace` define o diretório de trabalho para o container.
- O `pyproject.toml` indica que só `calculadora.py` é mutado e que os testes rodam com `python -m pytest -q`.
- A pasta `mutants/` guarda cache/artefatos das execuções; pode ser removida para recomeçar limpo.

## Pontos para destacar ao explicar o projeto
- Uso de mutação para validar a efetividade dos testes: mutantes que alteram a mensagem de erro em `dividir` agora são mortos porque o teste confere o texto do `ValueError`.
- Docker como ambiente Linux portátil para rodar mutmut em máquina Windows corporativa.
- Estrutura simples: código, testes, config do mutmut e cache separado para não poluir o versionamento.
