import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

df = pd.read_csv('/data/ecommerce_preparados.csv')
df = df.dropna()

# Statistics calculation
media = df['Desconto'].mean()  # Mean of discounts
mediana = df['Desconto'].median()  # Median of discounts
variancia = df['Desconto'].var()  # Variance of discounts
desvio_padrao = df['Desconto'].std()  # Standard deviation of discounts
moda = df['Desconto'].mode()[0]  # Mode of discounts
minimo = df['Desconto'].min()  # Minimum discount value
quartis = df['Desconto'].quantile([0.25, 0.5, 0.75])  # Discount quartiles
maximo = df['Desconto'].max()  # Maximum discount value

# Displays the first rows of the DataFrame
df.head()

# Correlation between Qtd_Vendidos_Cod and N_Avaliacoes_MinMax
corr_n_avaliacoes = df[['Qtd_Vendidos_Cod', 'N_Avaliacoes_MinMax']].corr()

# Correlation between Qtd_Vendidos_Cod and Nota_MinMax
corr_nota = df[['Qtd_Vendidos_Cod', 'Nota_MinMax']].corr()

# Correlation between Qtd_Vendidos_Cod and Preco_MinMax
corr_preco = df[['Qtd_Vendidos_Cod', 'Preco_MinMax']].corr()

# Displays the results
print("Correlation with number of reviews:\n", corr_n_avaliacoes)
print("Correlation with average rating:\n", corr_nota)
print("Correlation with price:\n", corr_preco)

# Defines the predictor variables and the target variable
X = df[['N_Avaliacoes_MinMax', 'Nota_MinMax', 'Preco_MinMax', 'Desconto_MinMax', 'Temporada_Cod', 'Marca_Freq', 'Material_Freq']]  # Predictor
Y = df['Qtd_Vendidos_Cod']

# Splits the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Creates and trains the Linear Regression model
modelo_lr = LinearRegression()
modelo_lr.fit(x_train, y_train)

# Makes predictions on the test set
y_prev = modelo_lr.predict(x_test)

# Evaluates the model
r2 = r2_score(y_test, y_prev)
print(f'Coefficient of Determination - R²: {r2:.2f}')

rmse = sqrt(mean_squared_error(y_test, y_prev))
print(f"Root Mean Squared Error - RMSE: {rmse:.2f}")

desvio_padrao = df['Qtd_Vendidos_Cod'].std()
print(f"Standard Deviation of Qtd_Vendidos_Cod: {desvio_padrao}")
