"""
Exercício 1 – Grafo de fluxo de controle, complexidade ciclomática e caminhos independentes.

Grafo (Mermaid):
```mermaid
flowchart TD
    A([Início]) --> B{n > 0?}
    B -->|Sim| C{n % 2 == 0?}
    C -->|Sim| D[return "Par positivo"]
    C -->|Não| E[return "Impar positivo"]
    B -->|Não| F{n < 0?}
    F -->|Sim| G[return "Negativo"]
    F -->|Não| H[return "Zero"]
```

Complexidade ciclomática:
- Há 3 decisões (n>0, n%2==0, n<0). Logo, M = decisões + 1 = 3 + 1 = 4.
- Equivalente pela fórmula M = E - N + 2 (para grafo conexo) => também resulta em 4.

Caminhos independentes:
1. A → B(sim) → C(sim) → D   | n>0 e n%2==0  | Saída: "Par positivo"
2. A → B(sim) → C(não) → E   | n>0 e n%2!=0 | Saída: "Impar positivo"
3. A → B(não) → F(sim) → G   | n<0          | Saída: "Negativo"
4. A → B(não) → F(não) → H   | n==0         | Saída: "Zero"
"""


def verificar(n: int) -> str:
    """Classifica um número como par/ímpar positivo, negativo ou zero."""
    if n > 0:
        if n % 2 == 0:
            return "Par positivo"
        else:
            return "Impar positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"
