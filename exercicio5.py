"""Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""

def invert_string(s):
    inverted = ""
    for i in range(len(s) - 1, -1, -1):
        inverted += s[i]
    return inverted

# Example usage:
input_string = input("\fInsira uma palavra: ")
print("\fPalavra invertida: ", invert_string(input_string))