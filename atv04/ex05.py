"""
Exercício 5 – Grafo de fluxo de controle, V(G) e caminhos independentes.

Grafo (Mermaid):
```mermaid
flowchart TD
    A([Inicio]) --> B[i = 0]
    B --> C{i < m?}
    C -->|Nao| H([Fim])
    C -->|Sim| D[j = 0]
    D --> E{j < n?}
    E -->|Nao| G[i += 1]
    E -->|Sim| F[print(i, j)]
    F --> J[j += 1]
    J --> E
    G --> C
```

Complexidade ciclomática V(G):
- Duas decisões (i < m, j < n). Portanto V(G) = 2 + 1 = 3.

Caminhos independentes (representando comportamentos distintos):
1. A → B → C(não) → H                    | m <= 0  | laços ignorados
2. A → B → C(sim) → D → E(não) → G → …   | m > 0, n <= 0 | externo roda, interno ignorado
3. A → B → C(sim) → D → E(sim) → F → J → … | m > 0, n > 0 | ambos laços executam
"""


def percorrer_matriz(m: int, n: int) -> None:
    """Percorre matriz m x n imprimindo posições."""
    for i in range(m):
        for j in range(n):
            print(f"Posicao ({i}, {j})")
