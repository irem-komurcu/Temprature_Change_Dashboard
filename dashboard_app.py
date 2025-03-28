import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from sklearn.linear_model import LinearRegression
import numpy as np

# Başlık
st.title("🌍 Global Temperature Trends Dashboard")

# Veri yükleme
@st.cache_data
def load_data():
    df = pd.read_csv('data/GlobalLandTemperaturesByCountry.csv')
    df['dt'] = pd.to_datetime(df['dt'])
    df = df.dropna(subset=['AverageTemperature', 'Country'])
    df['year'] = df['dt'].dt.year
    return df

df = load_data()

# Global yıllık ortalama
global_trend = df.groupby('year')['AverageTemperature'].mean().reset_index()

# Ülke bazlı sıcaklık değişimi
country_yearly = df.groupby(['Country', 'year'])['AverageTemperature'].mean().reset_index()
start = country_yearly[country_yearly['year'] == 1900]
end = country_yearly[country_yearly['year'] == 2013]
merged = pd.merge(end, start, on='Country', suffixes=('_2013', '_1900'))
merged['temp_change'] = merged['AverageTemperature_2013'] - merged['AverageTemperature_1900']
top_warming = merged.sort_values('temp_change', ascending=False).head(10)

# Geo veri
geojson_path = 'data/countries.geojson'
world = gpd.read_file(geojson_path)
merged_geo = world.merge(merged, how='left', left_on='ADMIN', right_on='Country')

# ️ Sidebar filtre
st.sidebar.header("Filters")
year_range = st.sidebar.slider('Year Range', 1900, 2013, (1900, 2013))

#  Global Trend Grafik
st.subheader("🌡️ Global Average Temperature Over Time")
filtered = global_trend[(global_trend['year'] >= year_range[0]) & (global_trend['year'] <= year_range[1])]
fig = px.line(filtered, x='year', y='AverageTemperature',
              labels={'AverageTemperature': 'Avg Temp (°C)'})
st.plotly_chart(fig)

#  En Çok Isınan Ülkeler
st.subheader("🔥 Top 10 Countries with Highest Warming (1900–2013)")
fig2 = px.bar(top_warming, x='Country', y='temp_change',
              labels={'temp_change': 'Temp Increase (°C)'})
st.plotly_chart(fig2)

#  Folium Harita
st.subheader("🗺️ Global Temperature Change Map")
m = folium.Map(location=[10, 0], zoom_start=2)

folium.Choropleth(
    geo_data=merged_geo.to_json(),
    name='choropleth',
    data=merged_geo,
    columns=['ADMIN', 'temp_change'],
    key_on='feature.properties.ADMIN',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Temperature Change (°C) from 1900 to 2013'
).add_to(m)

m.save("temperature_map.html")

st_folium(m, width=700, height=500)

# Prediction için model oluştur
X = global_trend['year'].values.reshape(-1, 1)
y = global_trend['AverageTemperature'].values
model = LinearRegression()
model.fit(X, y)

# 2050 ve 2100 için tahmin
future_years = np.array([2050, 2100]).reshape(-1, 1)
future_temps = model.predict(future_years)

# Prediction grafiği
st.subheader("🔮 Future Temperature Prediction")
fig3 = px.scatter(global_trend, x='year', y='AverageTemperature', 
                  title='Global Avg Temperature + Future Projection')
fig3.add_scatter(x=[2050, 2100], y=future_temps, 
                 mode='markers+text', 
                 marker=dict(color='red', size=10),
                 text=[f"{future_temps[0]:.2f}°C", f"{future_temps[1]:.2f}°C"],
                 textposition='top center')
st.plotly_chart(fig3)

# Insight metni
st.markdown(f"""
### 📌 Insights on Future Prediction

If the current trend continues:
- **2050 Predicted Avg Temp:** {future_temps[0]:.2f}°C
- **2100 Predicted Avg Temp:** {future_temps[1]:.2f}°C

This projection shows that the global average temperature may increase by approximately **{future_temps[1] - global_trend['AverageTemperature'].iloc[-1]:.2f}°C** by 2100.
""")
