"""
Exercício 6 – Grafo de fluxo de controle, V(G) e caminhos independentes.

Grafo (Mermaid):
```mermaid
flowchart TD
    A([Inicio]) --> B[total = 0]
    B --> C{proximo n em numeros?}
    C -->|Nao| J["Abaixo"]
    C -->|Sim| D{n > 0 and n % 2 == 0?}
    D -->|Sim| E[total += n]
    D -->|Nao| F{n < 0?}
    F -->|Sim| G[total -= 1]
    F -->|Nao| H[continue]
    E --> I{total > 10?}
    G --> I
    H --> C
    I -->|Sim| K["Acima"]
    I -->|Nao| C
```

Complexidade ciclomática V(G):
- Decisões/predicados: (1) laço `for` (há próximo elemento), (2) `n > 0 and n % 2 == 0`,
  (3) `n < 0`, (4) `total > 10`. Logo V(G) = 4 + 1 = 5.

Caminhos independentes (representativos):
1. Sem iterações: A → B → C(não) → J                              | numeros vazio | retorno "Abaixo"
2. Positivo par, não ultrapassa 10: A → B → C(sim) → D(sim) → E → I(não) → C(não) → J | retorno "Abaixo"
3. Positivo par, ultrapassa 10: A → B → C(sim) → D(sim) → E → I(sim) → K              | retorno "Acima"
4. Positivo ímpar (continue): A → B → C(sim) → D(não) → F(não) → H → ... → J          | retorno "Abaixo"
5. Negativo: A → B → C(sim) → D(não) → F(sim) → G → I(não) → ... → J                 | retorno "Abaixo"
"""


def analisar(numeros) -> str:
    """Analisa a lista somando pares positivos, penalizando negativos e limitando por 10."""
    total = 0
    for n in numeros:
        if n > 0 and n % 2 == 0:
            total += n
        elif n < 0:
            total -= 1
        else:
            continue

        if total > 10:
            return "Acima"

    return "Abaixo"
