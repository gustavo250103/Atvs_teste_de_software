 # atv04 – Grafos, complexidade ciclomática e testes

## O que tem aqui
- Exercícios `ex01.py` a `ex07.py`: funções simples usadas para ilustrar grafos de fluxo de controle, complexidade ciclomática e pares def-use.
- Arquivos `ex0X_graph.md`: cada um traz o grafo em Mermaid, o cálculo da complexidade ciclomática (V(G)) e os caminhos independentes.
- Testes `test01.py` a `test07.py`: validam os caminhos principais de cada exercício.
- `__init__.py`: deixa a pasta tratada como pacote para que os testes importem via `from .ex01 import ...`.

## Resumo dos exercícios
- **ex01.py** (`verificar`): classifica um número como par/ímpar positivo, negativo ou zero. Grafo com 3 decisões (V(G)=4). Coberto por `test01.py`.
- **ex02.py** (`classificar`): rotula um valor em Alto/Médio/Baixo baseado em limites >100 e >50. V(G)=3. Teste em `test02.py`.
- **ex03.py** (`acesso`): concede/nega acesso por idade e status de membro. V(G)=3. Teste em `test03.py`.
- **ex04.py** (`somar_ate`): soma de 0 até n-1; laço simples com V(G)=2. Teste em `test04.py`.
- **ex05.py** (`percorrer_matriz`): laço duplo m x n imprimindo posições; V(G)=3. Teste em `test05.py`.
- **ex06.py** (`analisar`): percorre lista, soma pares positivos, penaliza negativos, e interrompe se total passa de 10; V(G)=5. Teste em `test06.py`.
- **ex07.py** (`desconto`): aplica desconto VIP de 20% e piso mínimo 50; inclui pares def-use. Teste em `test07.py`.

## Como rodar os testes
Estando na raiz do repositório:
```powershell
cd atv04
python -m pytest -q
```
Ou, para um exercício específico (exemplo ex06):
```powershell
python -m pytest -q test06.py
```

## Como ler os grafos
Cada `ex0X_graph.md` contém:
- Diagrama Mermaid do fluxo de controle.
- Cálculo da complexidade ciclomática.
- Lista de caminhos independentes (base para os casos de teste).

Esses arquivos ajudam a justificar a cobertura dos testes e a ligação entre teoria (grafos/V(G)) e prática (asserts).***
