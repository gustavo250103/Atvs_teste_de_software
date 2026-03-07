"""
Exercício 2 – Grafo de fluxo de controle, V(G) e caminhos independentes.

Grafo (Mermaid):
```mermaid
flowchart TD
    A([Inicio]) --> B{x > 100?}
    B -->|Sim| C["Alto"]
    B -->|Nao| D{x > 50?}
    D -->|Sim| E["Medio"]
    D -->|Nao| F["Baixo"]
```

Complexidade ciclomática V(G):
- Duas decisões (x>100, x>50), então V(G) = decisões + 1 = 2 + 1 = 3.

Caminhos independentes:
1. A → B(sim) → C           | x > 100        | Saída: "Alto"
2. A → B(não) → D(sim) → E  | 50 < x ≤ 100   | Saída: "Medio"
3. A → B(não) → D(não) → F  | x ≤ 50         | Saída: "Baixo"
"""


def classificar(x: float) -> str:
    """Classifica x em Alto, Medio ou Baixo."""
    if x > 100:
        return "Alto"
    if x > 50:
        return "Medio"
    return "Baixo"
