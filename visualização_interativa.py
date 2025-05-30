import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html
import statsmodels

# Leitura do arquivo CSV para o DataFrame
df = pd.read_csv('ecommerce_estatistica.csv')

# Gráfico de Barras - Vendas por Gênero
genero_counts = df['Gênero'].value_counts().reset_index()
genero_counts.columns = ['Gênero', 'Quantidade']

fig_bar = px.bar(genero_counts,
                 x='Gênero', y='Quantidade',
                 labels={'Gênero': 'Gênero', 'Quantidade': 'Quantidade'},
                 title='Quantidade de Vendas por Gênero (em mil)',
                 color_discrete_sequence=['#90ee90'])

# Gráfico de Pizza - Distribuição por Quantidade Vendida
fig_pie = px.pie(df, names='Qtd_Vendidos', title='Distribuição da Quantidade Vendida')

# Histograma - Número de Avaliações
fig_hist = px.histogram(df, x='N_Avaliações', nbins=100,
                        title='Distribuição do Número de Avaliações',
                        color_discrete_sequence=['green'])

# Gráfico de Dispersão - Nota vs Número de Avaliações
fig_scatter = px.scatter(df, x='Nota', y='N_Avaliações', opacity=0.5,
                         title='Dispersão: Nota vs Número de Avaliações')

# Gráfico de Densidade - Distribuição de Preços
fig_den = px.histogram(df, x='Preço', marginal='rug',
                       nbins=50, histnorm='density',
                       title='Distribuição de Densidade de Preços',
                       color_discrete_sequence=['#86b9ec'])

# Gráfico de Regressão - Avaliações vs Desconto
fig_reg = px.scatter(df, x='Desconto', y='N_Avaliações', trendline='ols',
                     title='Regressão: Número de Avaliações vs Desconto',
                     color_discrete_sequence=['#278765'])

# Mapa de Calor - Correlação
correlation = df[['N_Avaliações', 'Qtd_Vendidos_Cod']].corr()
fig_heatmap = go.Figure(data=go.Heatmap(
    z=correlation.values,
    x=correlation.columns,
    y=correlation.index,
    colorscale='OrRd',
    zmin=-1,
    zmax=1
))
fig_heatmap.update_layout(title='Correlação entre Avaliações e Vendas')

# Criação da aplicação
app = Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard Interativo de E-commerce'),
    dcc.Graph(figure=fig_bar),
    dcc.Graph(figure=fig_pie),
    dcc.Graph(figure=fig_hist),
    dcc.Graph(figure=fig_scatter),
    dcc.Graph(figure=fig_den),
    dcc.Graph(figure=fig_reg),
    dcc.Graph(figure=fig_heatmap)
])

if __name__ == '__main__':
    app.run(debug=True)
