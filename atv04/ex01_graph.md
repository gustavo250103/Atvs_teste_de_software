```mermaid
flowchart TD
    A([Inicio]) --> B{n > 0?}
    B -->|Sim| C{n % 2 == 0?}
    C -->|Sim| D[Par positivo]
    C -->|Nao| E[Impar positivo]
    B -->|Nao| F{n < 0?}
    F -->|Sim| G[Negativo]
    F -->|Nao| H[Zero]
```

Complexidade ciclomatica:
- Ha 3 decisoes (n>0, n%2==0, n<0). Logo, M = decisoes + 1 = 3 + 1 = 4.
- Equivalente pela formula M = E - N + 2 (para grafo conexo) => tambem resulta em 4.

Caminhos independentes:
1. A -> B(sim) -> C(sim) -> D   | n>0 e n%2==0  | Saida: "Par positivo"
2. A -> B(sim) -> C(nao) -> E   | n>0 e n%2!=0 | Saida: "Impar positivo"
3. A -> B(nao) -> F(sim) -> G   | n<0          | Saida: "Negativo"
4. A -> B(nao) -> F(nao) -> H   | n==0         | Saida: "Zero"
