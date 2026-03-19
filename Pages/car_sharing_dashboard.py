import streamlit as st
import pandas as pd 

# Function to load CSV files into dataframes
@st.cache_data
def load_data(): 
    trips = pd.read_csv("datasets/trips.csv") 
    cars = pd.read_csv("datasets/cars.csv") 
    cities = pd.read_csv("datasets/cities.csv") 
    return trips, cars, cities 

trips, cars , cities = load_data()

# Merge trips with cars (joining on car_id) 
trips_merged = trips.merge(cars) 
# Merge with cities for car's city (joining on city_id) 
trips_merged = trips_merged.merge(cities) 
trips_merged = trips_merged.drop(columns=["car_id", "city_id", "customer_id", 
"id"]) 