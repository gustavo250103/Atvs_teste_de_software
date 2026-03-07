"""
Exercício 7 – Def/Use, GFC e du-pairs.

Grafo (Mermaid):
```mermaid
flowchart TD
    A([Início]) --> B[total = preco]
    B --> C{cliente_vip?}
    C -->|Sim| D[desconto = preco * 0.2]
    D --> E[total = preco - desconto]
    C -->|Não| E
    E --> F{total < 50?}
    F -->|Sim| G[total = 50]
    F -->|Não| H[return total]
    G --> H
```

Definições e usos:
- preco (parâmetro): def p0; usos em B (total = preco), D (desconto = preco*0.2) e E (total = preco - desconto).
- cliente_vip (parâmetro): def cv0; uso predicado em C.
- total:
  * t1: def em B (total = preco); usos em F (pred total<50) e H (return) quando não sobrescrito.
  * t2: def em E (total = preco - desconto); usos em F (pred) e H.
  * t3: def em G (total = 50); uso em H.
- desconto: d1 def em D; uso em E.

Pares def-uso (du-pairs) relevantes:
- preco: (p0 → B), (p0 → D), (p0 → E)
- cliente_vip: (cv0 → C)
- total: (t1 → F), (t1 → H); (t2 → F), (t2 → H); (t3 → H)
- desconto: (d1 → E)
"""


def desconto(preco: float, cliente_vip: bool) -> float:
    """Calcula total com desconto de 20% para VIP e piso mínimo de 50."""
    total = preco
    if cliente_vip:
        desconto = preco * 0.2
        total = preco - desconto
    if total < 50:
        total = 50
    return total
