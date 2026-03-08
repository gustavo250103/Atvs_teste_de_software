```mermaid
flowchart TD
    A([Inicio]) --> B[total = 0]
    B --> C{proximo n em numeros?}
    C -->|Nao| J[Abaixo]
    C -->|Sim| D{n > 0 and n % 2 == 0?}
    D -->|Sim| E[total += n]
    D -->|Nao| F{n < 0?}
    F -->|Sim| G[total -= 1]
    F -->|Nao| H[continue]
    E --> I{total > 10?}
    G --> I
    H --> C
    I -->|Sim| K[Acima]
    I -->|Nao| C
```
