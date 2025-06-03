import pandas as pd

# Load dataset
df = pd.read_csv('/data/ecommerce.csv')

# Check the number of rows and columns
rows_columns = df.shape
print('Check number of rows and columns: ', rows_columns)

# Check data types
types = df.dtypes
print('Check data types:\n', types)

# Check the number of missing values
nulls = df.isnull().sum()
print('Check missing values:\n', nulls)

# Replace missing values in 'Temporada' and 'Marca' columns with 'Não Definido'
df['Temporada'].fillna('Não Definido', inplace=True)
df['Marca'].fillna('Não Definido', inplace=True)

# Convert 'Marca' column to lowercase
df['Marca'] = df['Marca'].str.lower()

# Convert 'Material' column to lowercase
df['Material'] = df['Material'].str.lower()

# Convert 'Temporada' column to lowercase
df['Temporada'] = df['Temporada'].str.lower()

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove rows with fewer than 8 non-null values
df.dropna(thresh=8, inplace=True)
# The 'thresh' parameter defines the minimum number of non-null values required to retain the row

print(df.columns)

# Calculate the interquartile range (IQR)
q1 = df['N_Avaliacoes'].quantile(0.25)
q3 = df['N_Avaliacoes'].quantile(0.75)
iqr = q3 - q1

# Define the upper limit to identify outliers
upper_limit = q3 + 1.5 * iqr

# Filter products with number of reviews greater than the upper limit
df_avaliados = df[df['N_Avaliacoes'] > upper_limit]

df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# Extract and clean values from the 'Condicao' column
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split('|')[0].strip())

# Use a lambda function to get the fifth word from the string in the 'Condicao' column if it exists; otherwise, return 'Nenhum'
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split('|')[1].strip().split(' ')[0] if '|' in x else 'Nenhum')

# Convert the 'Desconto' column to string
df['Desconto'] = df['Desconto'].astype(str)

# Use a lambda function to remove the '%' symbol from the string in the 'Desconto' column
df['Desconto'] = df['Desconto'].apply(lambda x: x.split('%')[0] if '%' in x else x)