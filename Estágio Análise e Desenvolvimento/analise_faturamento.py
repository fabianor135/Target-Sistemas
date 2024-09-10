import json


with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

# Filtra os valores de faturamento maiores que 0
faturamentos_validos = [item['valor']
                        for item in faturamento if item['valor'] > 0.0]

# Calcula o menor e o maior valor de faturamento
menor_faturamento = min(faturamentos_validos)
maior_faturamento = max(faturamentos_validos)

# Calcula a média de faturamento
media_faturamento = sum(faturamentos_validos) / len(faturamentos_validos)

# Conta o número de dias com faturamento acima da média
dias_acima_da_media = len(
    [item['valor'] for item in faturamento if item['valor'] > media_faturamento])


print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Média de faturamento (excluindo dias 0.0): R$ {media_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
