"""
Exercício 3 – Grafo de fluxo de controle, V(G) e caminhos independentes.

Grafo (Mermaid):
```mermaid
flowchart TD
    A([Início]) --> B{idade >= 18?}
    B -->|Sim| C{membro?}
    C -->|Sim| D[return "Permitido"]
    C -->|Não| E[return "Negado"]
    B -->|Não| E
```

Complexidade ciclomática V(G):
- Há 2 decisões (idade >= 18, membro) ⇒ V(G) = decisões + 1 = 2 + 1 = 3.

Caminhos independentes:
1. A → B(sim) → C(sim) → D   | idade >= 18 e membro=True  | "Permitido"
2. A → B(sim) → C(não) → E   | idade >= 18 e membro=False | "Negado"
3. A → B(não) → E            | idade < 18                 | "Negado"
"""


def acesso(idade: int, membro: bool) -> str:
    """Concede ou nega acesso dependendo da idade e do status de membro."""
    if idade >= 18 and membro:
        return "Permitido"
    return "Negado"
