```mermaid
flowchart TD
    A([Inicio]) --> B[i = 0; soma = 0]
    B --> C{i < n?}
    C -->|Sim| D[soma += i]
    D --> E[i += 1]
    E --> C
    C -->|Nao| F[return soma]
```
