```mermaid
flowchart TD
    A([Inicio]) --> B{idade >= 18?}
    B -->|Sim| C{membro?}
    C -->|Sim| D[Permitido]
    C -->|Nao| E[Negado]
    B -->|Nao| E
```
