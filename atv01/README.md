# Calculadora com Testes - Atividade de Teste de Software

Este projeto implementa uma calculadora simples em Python com funções básicas de soma e divisão, acompanhada de uma suíte completa de testes usando pytest.

## Funcionalidades

### Calculadora (`calculadora.py`)
- `somar(a, b)`: Soma dois números
- `subtrair(a, b)`: Subtrai o segundo número do primeiro
- `multiplicar(a, b)`: Multiplica dois números
- `dividir(a, b)`: Divide o primeiro pelo segundo (com tratamento de divisão por zero)

### Utilitários de Notas (`test_calculadora.py`)
- `valida_nota(nota)`: Valida se uma nota está entre 0 e 10
- `calcular_media(notas)`: Calcula a média de uma lista de notas
- `obter_situacao(nota)`: Determina a situação do aluno baseada na nota
- `calcular_estatisticas(notas)`: Calcula estatísticas completas das notas
- `normalizar_notas(notas)`: Normaliza as notas para escores z (padronização estatística)

## Instalação

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como executar os testes

```bash
pytest
```

Ou para execução verbosa:
```bash
pytest -v
```

## Estrutura do Projeto

```
projeto/
├── calculadora.py          # Implementação da calculadora
├── test_calculadora.py     # Testes e utilitários de notas
├── requirements.txt        # Dependências do projeto
└── README.MD              # Este arquivo
```

## Tecnologias Utilizadas

- Python 3.9+
- pytest (testes)
- pytest-cov (cobertura de testes)

## Funcionalidades dos Testes

- Testes unitários para operações básicas
- Testes parametrizados
- Testes de classes
- Testes de validação de notas
- Testes de estatísticas
- Testes de normalização

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request