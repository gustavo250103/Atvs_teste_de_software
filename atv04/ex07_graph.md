```mermaid
flowchart TD
    A([Inicio]) --> B[total = preco]
    B --> C{cliente_vip?}
    C -->|Sim| D[desconto = preco * 0.2]
    D --> E[total = preco - desconto]
    C -->|Nao| E
    E --> F{total < 50?}
    F -->|Sim| G[total = 50]
    F -->|Nao| H[return total]
    G --> H
```
