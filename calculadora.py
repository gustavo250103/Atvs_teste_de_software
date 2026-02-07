def somar(a, b):
 """Soma dois numeros."""
 return a + b

def subtrair(a, b):
 """Subtrai o segundo do primeiro."""
 return a - b

def multiplicar(a, b):
 """Multiplica dois numeros."""
 return a * b

def dividir(a, b):
 """Divide o primeiro pelo segundo."""
 if b == 0:
  raise ValueError("Divisao por zero!")
 return a / b