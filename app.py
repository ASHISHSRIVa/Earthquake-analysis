import pandas as pd
import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# Load and preprocess dataset
data = pd.read_csv(r"C:\Users\HP\Downloads\earthquake_1995-2023.csv")
data['date_time'] = pd.to_datetime(data['date_time'])
data['year'] = data['date_time'].dt.year

# Streamlit app setup
st.title("Earthquake Analysis Dashboard (1995-2023)")

# Global Heatmap
st.header("Global Earthquake Heatmap")
m = folium.Map(location=[0, 0], zoom_start=2)
heat_data = [[row['latitude'], row['longitude'], row['magnitude']] for index, row in data.iterrows()]
HeatMap(heat_data).add_to(m)
st_data = st_folium(m, width=700, height=450)

# Yearly Trends
st.header("Yearly Earthquake Trends")
yearly_trend = data.groupby(data['year']).size()
st.bar_chart(yearly_trend)

# Alert Level Distribution
st.header("Alert Level Analysis")
alert_counts = data['alert'].value_counts()
st.bar_chart(alert_counts)

# Predictive Model
st.header("Predict Community Determined Intensity (CDI) or Modified Mercalli Intensity (MMI)")
st.subheader("Input Parameters")
mag = st.slider("Magnitude:", min_value=0.0, max_value=10.0, step=0.1, value=5.0)
depth = st.slider("Depth (km):", min_value=0.0, max_value=700.0, step=1.0, value=10.0)
if st.button("Predict"):
    # Placeholder for a prediction model
    st.write(f"Predicted CDI/MMI: {mag * 1.2 - depth * 0.02:.2f} (Example formula)")
