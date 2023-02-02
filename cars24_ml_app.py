'''
The code is a web application that predicts the price of a used car. It uses the streamlit library to create the UI and pandas to load a CSV file with the data.

It uses a pre-trained machine learning model (loaded using pickle) to make the prediction based on the input features: fuel type, transmission type, engine power, and number of seats.

The user can select the features using drop-down menus and sliders. The "Predict Price" button is used to trigger the prediction. The result is displayed as text on the UI.

At the end of the code, there is a date input feature where the user can input a date. The date is displayed after the user inputs it.

A bar chart is commented out at the end of the code that could be used to visualize data from the CSV file with the x-axis as fuel type and y-axis as mileage.

'''
# Import necessary libraries
import pandas as pd
import streamlit as st
import datetime
import pickle

# Load the CSV file with the car data
cars_df = pd.read_csv("./cars24-car-price.csv")

# Write the title of the application on the UI
st.write("""
# Cars24 Used Car Price Prediction
""")


# Dictionary to encode categorical variables
encode_dict = {
    "fuel_type": {"Diesel": 1, "Petrol": 2, "CNG": 3, "LPG": 4, "Electric": 5},
    "seller_type": {"Dealer":1,"Individual":2,"Trustmark Dealer":3  },
    "transmission_type": {"Manual":1,"Automatic":2  }
}

# Function to make the prediction using the pre-trained model
def model_pred(fuel_type, transmission_type, engine, seats):

    ## Load the pre-trained model using pickle
    with open("car_pred", "rb") as file:
        reg_model = pickle.load(file)

    # Prepare the input features
    input_features = [[2018.0, 1, 40000, fuel_type, transmission_type, 19.70, engine, 86.30, seats]]
    return reg_model.predict(input_features)

# Create two columns in the UI
col1, col2 = st.columns(2)

# Create a drop-down menu to select the fuel type
fuel_type = col1.selectbox("Select fuel type",
                            ["Diesel", "Petrol", "CNG", "LPG", "Electric"])

# Create a slider to set the engine power
engine = col1.slider("Set the engine power",
                        500, 5000, step=100)

# Create a drop-down menu to select the transmission type
transmission_type = col2.selectbox("Select transmission type",
                                    ['Manual', "Automatic"])

# Create a drop-down menu to select the number of seats
seats = col2.selectbox("No. of Seats",
                        [4,5,6,7])

# Create a button to trigger the prediction
if(st.button("Predict Price")):
  # Encode the categorical variables
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    # Make the prediction
    price = model_pred(fuel_type, transmission_type, engine, seats)
    
     # Display the result on the UI
    st.text("Predicted price of the car: "+ str(price))


# Create a date input field
d = st.date_input("Enter the date", date(2023,01,02))
# Display the input date on the UI
st.write ("Date is:" ,d)

# # Create a bar chart (commented out)
#st.bar_chart(data=cars_df, x= 'fuel_type', y= 'mileage')