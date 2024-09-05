
"""Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

def fibonacci_sequencia(limit):
    fib_seq = [0, 1]
    while fib_seq[-1] < limit:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def check_fibonacci(number):
    fib_seq = fibonacci_sequencia(num1)
    if number in fib_seq:
        return f"\f O número {num1} pertence à sequência de Fibonacci."
    else:
        return f"\f O número {num1} não pertence à sequência de Fibonacci."

num1 = int(input("\f Insira um número inteiro qualquer: "))

resultado = check_fibonacci(num1)
print(resultado)