📊 Data Analysis and Visualization of Mercado Livre Products
This project presents a complete pipeline for analyzing product data from Mercado Livre. It includes data preparation, cleaning, statistical analysis, and both static and interactive visualizations — all built with Python.

📁 Project Structure
preparação_dados.py
Loads the dataset and performs initial cleaning, such as dropping unnecessary columns and filtering valid entries.

tratamento_dados.py
Handles missing values, renames columns, converts data types, and prepares the dataset for analysis.

matemática_estatística.py
Applies basic statistics (mean, median, mode, standard deviation) to identify trends and patterns in the dataset.

visualização.py
Creates static charts using Matplotlib and Seaborn to explore relationships and distributions in the data.

visualização_interativa.py
Builds interactive charts with Plotly Express to make data exploration more engaging and intuitive.

🎯 Key Objectives
Transform raw data into clean, analysis-ready datasets.

Apply descriptive statistics to uncover patterns and outliers.

Build dashboards and visualizations to communicate insights clearly.

Support decision-making with evidence from real marketplace data.

🧪 Technologies Used
Python 3.10+

pandas, numpy – data manipulation

matplotlib, seaborn – static data visualization

plotly.express – interactive visualizations

▶️ How to Run
Clone the repository

bash
Copiar
Editar
git clone https://github.com/your-user/your-repo.git
cd your-repo
Install the required libraries
(or create a virtual environment first)

bash
Copiar
Editar
pip install -r requirements.txt
Run the scripts in the following order:

preparação_dados.py

tratamento_dados.py

matemática_estatística.py

visualização.py or visualização_interativa.py

📦 Dataset Description
The dataset includes key attributes of fashion products from Mercado Livre:

Product name, brand, gender, season, and material

Ratings and user comments

Sales performance (Qtd_Vendidos – units sold)

💡 Sample Insights
Which product categories have the highest sales volume

Correlation between number of reviews and product ratings

Most frequent brands and materials across genders and seasons

Sales distribution by rating or price

📈 Output Examples
✔️ Pie and bar charts showing sales distribution
✔️ Histograms for ratings and comment counts
✔️ Scatter plots to explore relationships between metrics
✔️ Interactive dashboards using Plotly for filtering and deeper analysis

📄 License
This project is under the MIT License. You are free to use, modify, and share it.



