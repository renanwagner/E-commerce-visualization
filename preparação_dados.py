import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('/data/ecommerce_tratados.csv')

# Checks the number of unique values in each column
unicos = df.nunique()
print('Unique data analysis:\n', unicos)

# Calculates descriptive statistics for numeric fields
estatisticas = df.describe()
print('Data statistics:\n', estatisticas)

# Creates the "Preço" field using the calculation: Reais + (Centavos / 100)
df['Preco'] = df['Reais'] + (df['Centavos'] / 100)

# Removes the indicated fields and updates the DataFrame
df = df.drop(columns=['Reais', 'Centavos', 'Condicao', 'Condicao_Atual'])

# Cleans column names
df.columns = df.columns.str.strip()
df.columns = df.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
df.columns = df.columns.str.replace(' ', '_')

# Analysis and statistics
unicos = df.nunique()
print('Unique data analysis:\n', unicos)

estatisticas = df.describe()
print('Data statistics:\n', estatisticas)

# Price
df['Preco'] = df['Reais'] + (df['Centavos'] / 100)

# Remove columns
df = df.drop(columns=['Reais', 'Centavos', 'Condicao', 'Condicao_Atual'])

# MinMaxScaler
scaler = MinMaxScaler()
df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])
df['N_Avaliacoes_MinMax'] = scaler.fit_transform(df[['N_Avaliacoes']])
df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])
df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])

# LabelEncoder
le_marca = LabelEncoder()
le_material = LabelEncoder()
df['Marca_Cod'] = le_marca.fit_transform(df['Marca'])
df['Material_Cod'] = le_material.fit_transform(df['Material'])
df['Temporada_Cod'] = le_material.fit_transform(df['Temporada'])

df = pd.read_csv('/data/ecommerce_preparados.csv')

# Qtd_Vendidos_Cod
mapa_vendas = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+1000': 1000,
    '+10mil': 10000,
    '+50mil': 50000
}
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(mapa_vendas)

# Relative frequency of the Brand: based on the total of VALID entries
frequencia_marca = df['Marca'].value_counts(normalize=True)
df['Marca_Freq'] = df['Marca'].map(frequencia_marca)

# Relative frequency of the Material: based on the TOTAL number of DF ROWS
frequencia_material_absoluta = df['Material'].value_counts()
frequencia_material_total_df = frequencia_material_absoluta / len(df)
df['Material_Freq'] = df['Material'].map(frequencia_material_total_df)
