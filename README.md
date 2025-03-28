# 🌍 Global Temperature Trends Dashboard

This project analyzes and visualizes historical global temperature changes over time, providing insights and future projections.

## 📌 Features

- 📈 Global average temperature trend visualization (1900–2013)
- 🔥 Top 10 countries with highest temperature increase
- 🗺️ Interactive choropleth map of temperature change
- 🔮 Future temperature prediction for 2050 & 2100

---

## 🚀 How to Run

1. Clone the repository:

git clone https://github.com/username/temperature_dashboard.git cd temperature_dashboard


2. Create and activate a virtual environment:

python3 -m venv venv source venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt


4. Run the Streamlit dashboard:

streamlit run dashboard_app.py


5. Choropleth map is also saved as an HTML file:

temperature_map.html


## 📊 Dataset Sources

- [Global Land Temperatures Dataset (Kaggle)](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)
- [Natural Earth Countries GeoJSON](https://www.naturalearthdata.com/)

## 📈 Key Insights

- Global average temperature increased by approximately **+1.2°C** between 1900 and 2013.
- The highest temperature increases were observed in **Russia, Kazakhstan, and Canada**.
- Predicted global average temperature in:
  - **2050:** ~19.8°C
  - **2100:** ~20.5°C

## 🧩 Tech Stack

- Python
- Pandas
- GeoPandas
- Folium
- Plotly
- Scikit-learn
- Streamlit

## 🚧 To-Do List / Future Improvements

This is version 1.0 of the project. For production readiness, the following improvements are planned:

- Code Refactoring & Modularization:
  - Split data preparation, analysis, prediction, and dashboard logic into separate Python modules.
  - Apply Python project structure best practices.
- Configuration & Parameterization:
  - Move file paths and settings to a config file.
- Cloud Deployment:
  - Deploy the dashboard to Google Cloud Platform (GCP) or Streamlit Cloud.
- Advanced Predictive Models:
  - Use ARIMA, LSTM, or other advanced models beyond Linear Regression.
- UI/UX Enhancements:
  - Add country filters, year range selectors, and dynamic interaction options.

## 📄 License

This project is licensed under the MIT License.

## 🙌 Acknowledgements

Thanks to the [Berkeley Earth](http://berkeleyearth.org) initiative for providing open temperature datasets.
