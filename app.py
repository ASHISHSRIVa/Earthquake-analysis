import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# Load data
data = pd.read_csv(r"C:\Users\HP\Downloads\Earthquake analysis\app.py")
data['date_time'] = pd.to_datetime(data['date_time'])

# Streamlit app
st.title("Earthquake Analysis Dashboard")

# Heatmap
st.header("Global Earthquake Heatmap")
m = folium.Map(location=[0, 0], zoom_start=2)
heat_data = [[row['latitude'], row['longitude'], row['magnitude']] for index, row in data.iterrows()]
HeatMap(heat_data).add_to(m)
st_data = st_folium(m, width=700, height=450)

# Yearly Trends
st.header("Yearly Earthquake Trends")
yearly_trend = data.groupby(data['date_time'].dt.year).size()
st.bar_chart(yearly_trend)

# Model Prediction
st.header("Predict CDI or MMI")
mag = st.slider("Select Magnitude:", min_value=0.0, max_value=10.0, step=0.1)
depth = st.slider("Select Depth (km):", min_value=0.0, max_value=700.0, step=1.0)
if st.button("Predict"):
    # Example prediction logic
    # Ensure you have a model loaded here, e.g., a trained machine learning model
    # For now, just a placeholder:
    prediction = mag * depth  # This is a dummy logic; replace it with actual prediction model
    st.write(f"Predicted CDI/MMI: {prediction:.2f}")

# Geospatial Risk Maps: Highlighting high-seismicity and tsunami-prone zones
st.header("Geospatial Risk Maps: High-Seismicity and Tsunami-Prone Zones")

# Create a folium map for risk zones
risk_map = folium.Map(location=[20, 30], zoom_start=2)

# High Seismicity Zones (example points, you can replace this with real data)
seismicity_zones = [
    {"name": "Zone 1", "coords": [38.2975, 142.3722]},  # Example: Japan (near Tohoku)
    {"name": "Zone 2", "coords": [-33.8688, 151.2093]},  # Example: Australia
    {"name": "Zone 3", "coords": [19.4326, -99.1332]},  # Example: Mexico City
]

for zone in seismicity_zones:
    folium.Marker(
        location=zone["coords"],
        popup=f"High Seismicity Zone: {zone['name']}",
        icon=folium.Icon(color='red')
    ).add_to(risk_map)

# Tsunami-Prone Zones (example points, you can replace this with real data)
tsunami_zones = [
    {"name": "Tsunami Risk Zone 1", "coords": [0, 100]},  # Example: Pacific Ocean
    {"name": "Tsunami Risk Zone 2", "coords": [-10, 120]},  # Example: Indian Ocean
]

for zone in tsunami_zones:
    folium.Marker(
        location=zone["coords"],
        popup=f"Tsunami Risk Zone: {zone['name']}",
        icon=folium.Icon(color='blue')
    ).add_to(risk_map)

# Display the map with high seismicity and tsunami-prone zones
st_data_risk = st_folium(risk_map, width=700, height=450)
