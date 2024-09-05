"""Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

# Retornando a base de dados de faturamento gerada
import json

faturamento_janeiro = [
    {"dia": 1, "valor": 1500.50},
    {"dia": 2, "valor": 1750.00},
    {"dia": 3, "valor": 1625.75},
    {"dia": 4, "valor": 1830.90},
    {"dia": 5, "valor": 1200.00},
    {"dia": 6, "valor": 1900.50},
    {"dia": 7, "valor": 1450.30},
    {"dia": 8, "valor": 1700.00},
    {"dia": 9, "valor": 1600.40},
    {"dia": 10, "valor": 2100.75},
    {"dia": 11, "valor": 2300.00},
    {"dia": 12, "valor": 1500.50},
    {"dia": 13, "valor": 1800.00},
    {"dia": 14, "valor": 1750.30},
    {"dia": 15, "valor": 1900.75},
    {"dia": 16, "valor": 2050.10},
    {"dia": 17, "valor": 1550.25},
    {"dia": 18, "valor": 2200.50},
    {"dia": 19, "valor": 2400.75},
    {"dia": 20, "valor": 2250.90},
    {"dia": 21, "valor": 1900.50},
    {"dia": 22, "valor": 1800.00},
    {"dia": 23, "valor": 1650.40},
    {"dia": 24, "valor": 2100.75},
    {"dia": 25, "valor": 2350.00},
    {"dia": 26, "valor": 2500.30},
    {"dia": 27, "valor": 2700.40},
    {"dia": 28, "valor": 2450.75},
    {"dia": 29, "valor": 2300.00},
    {"dia": 30, "valor": 2550.50},
    {"dia": 31, "valor": 2750.00}
]

with open ('faturamento_janeiro.json', 'r') as arquivo:
    faturamento_janeiro = json.load(arquivo)

def carregar_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)

def calcular_media_mensal(faturamento):
    valores = [item['valor'] for item in faturamento]
    return sum(valores) / len(valores)

def encontrar_dias_acima_media(faturamento, media_mensal):
    return [item for item in faturamento if item['valor'] > media_mensal]

def encontrar_maior_e_menor_faturamento(faturamento):
    maior = max(faturamento, key=lambda x: x['valor'])
    menor = min(faturamento, key=lambda x: x['valor'])
    return maior, menor

faturamento_janeiro = carregar_faturamento('faturamento_janeiro.json')
media_mensal = calcular_media_mensal(faturamento_janeiro)
dias_acima_media = encontrar_dias_acima_media(faturamento_janeiro, media_mensal)
maior, menor = encontrar_maior_e_menor_faturamento(faturamento_janeiro)

print(f"Média mensal: R$ {media_mensal:.2f}")
print("Dias que superaram a média mensal:")
for dia in dias_acima_media:
    print(f"Dia {dia['dia']}: R$ {dia['valor']:.2f}")

print(f"Dia com maior faturamento: {maior['dia']} (R$ {maior['valor']:.2f})")
print(f"Dia com menor faturamento: {menor['dia']} (R$ {menor['valor']:.2f})")

