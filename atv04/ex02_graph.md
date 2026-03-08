```mermaid
flowchart TD
    A([Inicio]) --> B{x > 100?}
    B -->|Sim| C[Alto]
    B -->|Nao| D{x > 50?}
    D -->|Sim| E[Medio]
    D -->|Nao| F[Baixo]
```

Complexidade ciclomatica:
- Duas decisoes (x>100, x>50), entao V(G) = decisoes + 1 = 2 + 1 = 3.

Caminhos independentes:
1. A -> B(sim) -> C                 | x > 100        | Saida: "Alto"
2. A -> B(nao) -> D(sim) -> E        | 50 < x <= 100   | Saida: "Medio"
3. A -> B(nao) -> D(nao) -> F        | x <= 50         | Saida: "Baixo"
