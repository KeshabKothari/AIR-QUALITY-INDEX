import pickle
import streamlit as st
import numpy as np

pickle_in = open("randomforest_regression_model.pkl", "rb")
random_forest_regressor = pickle.load(pickle_in)


def welcome():
    return " welcome all "


def predict_AQI(Average_Temperature, Maximum_Temperature, Minimum_Temperature,
                Atm_pressure_at_sea_level, Average_relative_humidity, Average_visibility, Average_wind_speed,
                Maximum_sustained_wind_speed):
    prediction = random_forest_regressor.predict([[Average_Temperature, Maximum_Temperature,
                                                   Minimum_Temperature, Atm_pressure_at_sea_level,
                                                   Average_relative_humidity, Average_visibility, Average_wind_speed,
                                                   Maximum_sustained_wind_speed]])
    print(prediction)
    return prediction


def main():
    html_temp = """
 <div style='background-color:#205454;padding:20px'>
 <h2 style='color:black;text-align:center;'>AQI prediction ML App </h2>
 </div>
 """
    st.markdown(html_temp, unsafe_allow_html=True)
    Average_Temperature = st.number_input("Average_Temperature (Celcius)")
    Maximum_Temperature = st.number_input("Maximum_Temperature (Celcius) ")
    Minimum_Temperature = st.number_input("Minimum_Temperature (Celcius) ")
    Atm_pressure_at_sea_level = st.number_input("Atm_pressure_at_sea_level (hectopascal) ")
    Average_relative_humidity = st.number_input("Average_relative_humidity (Percentage) ")
    Average_visibility = st.number_input("Average_visibility (Km) ")
    Average_wind_speed = st.number_input("Average_wind_speed (Km/h) ")
    Maximum_sustained_wind_speed = st.number_input("Maximum_sustained_wind_speed (Km/h)")

    result = ''
    if st.button('Predict'):
        if ((Average_Temperature != 0.00) and (Maximum_Temperature != 0.00) and (Minimum_Temperature != 0.00) and (
                Atm_pressure_at_sea_level != 0.00) and (Average_wind_speed != 0.00)):
            result = predict_AQI(Average_Temperature, Maximum_Temperature, Minimum_Temperature,
                                 Atm_pressure_at_sea_level, Average_relative_humidity, Average_visibility,
                                 Average_wind_speed, Maximum_sustained_wind_speed)
            if 0 <= result <= 30:
                st.success("The Estimated AQI Good")
                st.success('The value of PM 2.5 is {}'.format(np.round(result, 2)))
            elif 31 <= result <= 60:
                st.success('The value of PM 2.5 is {}'.format(np.round(result, 2)))
                st.success("The Estimated AQI Satisfactory")
            elif 61 <= result <= 90:
                st.success('The value of PM 2.5 is {}'.format(np.round(result, 2)))
                st.success("The Estimated AQI Moderate")
            elif 91 <= result <= 120:
                st.success('The value of PM 2.5 is {}'.format(np.round(result, 2)))
                st.success("The Estimated AQI poor")
            elif 121 <= result <= 250:
                st.success('The value of PM 2.5 is {}'.format(np.round(result, 2)))
                st.success("The Estimated AQI very poor")
            elif result >= 250:
                st.success('The value of PM 2.5 is {}'.format(np.round(result, 2)))
                st.success("The Estimated AQI severe")

    st.text("Built with Streamlit")


if __name__ == '__main__':
    main()
