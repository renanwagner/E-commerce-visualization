import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head(20).to_string())
print(df.columns)
print(df.dtypes)



# Gráfico de Barras
plt.figure(figsize=(10, 6))
df['Gênero'].value_counts().plot(kind='bar', color='#90ee90')
plt.title('Quantidade de vendas por gênero (em mil)')
plt.xlabel('Gênero')
plt.ylabel('Qtd_Vendidos')
plt.xticks(rotation=0)
plt.show()

# Gráfico de Pizza - Distribuição por Quantidade Vendida
x = df['Qtd_Vendidos'].value_counts().index
y = df['Qtd_Vendidos'].value_counts().values

plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição por Quantidade de Vendas')
plt.show()

# Gráfico Histograma
plt.figure(figsize=(10, 6))
plt.hist(df['N_Avaliações'], bins=100, color='green', alpha=0.8)
plt.title('Histograma - Distribuição do Número de Avaliações')
plt.xlabel('N_Avaliações')
plt.xticks(ticks=range(0, int(df['N_Avaliações'].max())+100, 1000))
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Gráfico de Dispersão
plt.hexbin(df['Nota'], df['N_Avaliações'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Nota')
plt.ylabel('Número de Avaliações')
plt.title('Dispersão entre Nota e Número de Avaliações')
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='#86b9ec')
plt.title('Densidade de Preços')
plt.xlabel('Preço')
plt.show()

# Gráfico de Regressão
sns.regplot(x='Desconto', y='N_Avaliações', data=df, color='#278765',
            scatter_kws={'alpha': 0.5, 'color': '#3fc289'})
plt.title('Regressão de N_Avaliações por Desconto')
plt.xlabel('Desconto')
plt.ylabel('N_Avaliações')
plt.show()

# Gráfico Mapa de Calor
correlacoes = df[['N_Avaliações', 'Qtd_Vendidos_Cod']].corr()
plt.figure(figsize=(6, 4))
sns.heatmap(correlacoes, annot=True, cmap='OrRd', fmt=".2f")
plt.title('Correlação entre Número de Avaliações e Quantidade de Vendas')
plt.show()

