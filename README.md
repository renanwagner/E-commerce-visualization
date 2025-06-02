# E-commerce-visualization

markdown
Copiar
Editar
# 📦 E-commerce Visualization

This project presents an analysis of e-commerce data using two approaches:

- **Static Visualization** with Matplotlib and Seaborn
- **Interactive Dashboard** with Plotly and Dash

It reveals patterns related to product sales by gender, rating distribution, the impact of discounts, number of reviews, and correlations — all in a clear and visual way.

---

## 📁 Project Structure

```bash
ecommerce-visualization/
│
├── ecommerce_estatistica.csv       # E-commerce dataset
├── visualização.py                 # Static visualizations with Matplotlib and Seaborn
├── visualização_interativa.py     # Interactive dashboard with Plotly + Dash
└── README.md                       # This file
📊 Static Visualizations (visualização.py)
Built with Matplotlib and Seaborn, this script generates:

📊 Bar Chart: sales by gender

🥧 Pie Chart: product rating distribution

📈 Histogram: number of reviews

🔵 Scatter Plot: rating vs number of reviews

🌊 Density Plot: price distribution

📉 Regression Plot: discount vs number of reviews

🔥 Heatmap: correlation between reviews and sales volume

⚡ Interactive Dashboard (visualização_interativa.py)
Built with Dash and Plotly, this dashboard allows users to explore:

Interactive bar, pie, histogram, and scatter charts

Price density distribution

Regression line visualization

Correlation heatmap between metrics

<!-- Replace with an actual screenshot -->

▶️ How to Run
Clone the repository:

bash
Copiar
Editar
git clone https://github.com/your-username/ecommerce-visualization.git
cd ecommerce-visualization
Install dependencies:

bash
Copiar
Editar
pip install -r requirements.txt
Run the interactive dashboard:

bash
Copiar
Editar
python visualização_interativa.py
Open your browser and go to: http://127.0.0.1:8050

🛠 Technologies Used
Python

Pandas

Matplotlib

Seaborn

Plotly

Dash

Statsmodels (for OLS regression)

📈 Project Goal
To provide data-driven insights through visual analysis, making it easier to understand customer behavior, product ratings, and the impact of promotional strategies in an e-commerce environment.

