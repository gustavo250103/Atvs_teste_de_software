```mermaid
flowchart TD
    A([Inicio]) --> B[i = 0];
    B --> C{i < m?};
    C -->|Nao| H([Fim]);
    C -->|Sim| D[j = 0];
    D --> E{j < n?};
    E -->|Nao| G[i += 1];
    E -->|Sim| F[print(i, j)];
    F --> J[j += 1];
    J --> E;
    G --> C;
```
