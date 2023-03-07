# Weather finding app using streamlit
import streamlit as st
import requests

API_KEY = "8435339acd68b661c22e21b6e08948e7"


def find_weather(city):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    weather_data = requests.get(base_url).json()
    try:
        general = weather_data['weather'][0]['main']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(weather_data['main']['temp'])
        icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City Not Found")
        st.stop()
    return general, temperature, icon

# Here creating user interface
def user_interface():
    st.header("Find the Weather")
    city = st.text_input("Enter the name of the city for which you want to find the weather").lower()
    if st.button("Find Weather"):
        general, temperature, icon = find_weather(city)
        col_1, col_2 = st.columns(2)
        with col_1:
            st.metric(label="Temperature", value=f"{temperature}°C")
        with col_2:
            st.write(general)
            st.image(icon)


if __name__ == '__main__':
    user_interface()