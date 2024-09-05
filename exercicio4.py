"""Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. """

import matplotlib.pyplot as plt

# Defina os valores de faturamento mensal por estado
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcule o valor total mensal
total_mensal = sum(faturamento_mensal.values())

# Crie uma lista com os nomes dos estados
estados = list(faturamento_mensal.keys())

# Crie uma lista com os valores de faturamento mensal por estado
valores = list(faturamento_mensal.values())

# Crie uma lista com os percentuais de representação de cada estado
percentuais = [(valor / total_mensal) * 100 for valor in valores]

# Crie o gráfico de pizza
plt.pie(percentuais, labels=estados, autopct='%1.1f%%')
plt.title('Faturamento Mensal por Estado')
plt.show()