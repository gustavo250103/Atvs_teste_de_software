"""
Exercício 4 – Grafo de fluxo de controle, V(G) e caminhos independentes.

Grafo (Mermaid):
```mermaid
flowchart TD
    A([Inicio]) --> B[i=0; soma=0]
    B --> C{i < n?}
    C -->|Sim| D[soma += i]
    D --> E[i += 1]
    E --> C
    C -->|Nao| F[return soma]
```

Complexidade ciclomática V(G):
- Há 1 decisão (i < n). Portanto V(G) = decisões + 1 = 1 + 1 = 2.

Caminhos independentes:
1. A → B → C(não) → F        | n <= 0 (laço ignorado)
2. A → B → C(sim) → D → E → C(não) → F | n > 0 (laço executa ≥1 vez)
"""


def somar_ate(n: int) -> int:
    """Soma os inteiros de 0 até n-1."""
    soma = 0
    for i in range(n):
        soma += i
    return soma
