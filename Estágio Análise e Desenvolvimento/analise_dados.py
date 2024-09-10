import xml.etree.ElementTree as ET
import pandas as pd


tree = ET.parse('dados.xml')
root = tree.getroot()


dias = []
valores = []


for row in root.findall('row'):
    dia = row.find('dia').text
    valor = row.find('valor').text
    dias.append(int(dia))
    valores.append(float(valor))


df = pd.DataFrame({
    'Dia': dias,
    'Valor': valores
})


print(df)


total_valores = df['Valor'].sum()
print(f"Total dos valores: {total_valores}")

# - Filtrar dias com valor maior que 0
dias_com_valor = df[df['Valor'] > 0]
print(dias_com_valor)
