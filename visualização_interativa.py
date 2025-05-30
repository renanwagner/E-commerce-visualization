import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html
import statsmodels

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head(20).to_string())
print(df.columns)
print(df.dtypes)

# Bar Chart - Sales by Gender
genero_counts = df['Gênero'].value_counts().reset_index()
genero_counts.columns = ['Gênero', 'Quantidade']

fig_bar = px.bar(genero_counts,
                 x='Gênero', y='Quantidade',
                 labels={'Gênero': 'Gênero', 'Quantidade': 'Quantidade'},
                 title='Sales Quantity by Gender (in thousands)',
                 color_discrete_sequence=['#90ee90'])

# Pie Chart - Distribution by Sales Amount
fig_pie = px.pie(df, names='Qtd_Vendidos', title='Sales Amount Distribution')

# Histogram - Number of Reviews
fig_hist = px.histogram(df, x='N_Avaliações', nbins=100,
                        title='Distribution of Number of Reviews',
                        color_discrete_sequence=['green'])

# Scatter Plot - Rating vs. Number of Reviews
fig_scatter = px.scatter(df, x='Nota', y='N_Avaliações', opacity=0.5,
                         title='Scatter Plot of Rating vs Number of Reviews')

# Density Plot - Price Distribution
fig_den = px.histogram(df, x='Preço', marginal='rug',
                       nbins=50, histnorm='density',
                       title='Price Density Distribution',
                       color_discrete_sequence=['#86b9ec'])

# Regression Plot - Reviews vs. Discount
fig_reg = px.scatter(df, x='Desconto', y='N_Avaliações', trendline='ols',
                     title='Regression: Number of Reviews vs Discount',
                     color_discrete_sequence=['#278765'])

# Heatmap - Correlation
correlation = df[['N_Avaliações', 'Qtd_Vendidos_Cod']].corr()
fig_heatmap = go.Figure(data=go.Heatmap(
    z=correlation.values,
    x=correlation.columns,
    y=correlation.index,
    colorscale='OrRd',
    zmin=-1,
    zmax=1
))
fig_heatmap.update_layout(title='Correlation between Reviews and Sales')

# App creation
app = Dash(__name__)

app.layout = html.Div([
    html.H1('Interactive E-commerce Dashboard'),
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