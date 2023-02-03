# Car-Price-Prediction-and-Visualization-Using-Streamlit

Blog: https://medium.com/@anpuntam/streamlit-powered-used-car-price-prediction-a-hands-on-application-of-machine-learning-55dda1e2e663

cars24_ml_app.py creates a web application that predicts the price of a used car. The user interface is built using the streamlit library and the data is loaded from a CSV file using pandas.

The user can select the car features using drop-down menus and sliders for fuel type, transmission type, engine power, and number of seats. The prediction is triggered by pressing the "Predict Price" button. The result is displayed as text on the user interface.

The code also includes a date input feature where the user can input a date, which is then displayed on the user interface.

A bar chart has been commented out at the end of the code that could be used to visualize data from the CSV file, with the x-axis as fuel type and the y-axis as mileage.

In the code git_setup_colab.py, the user is prompted to enter their Github email, username, password, and token. The code then pulls changes from the remote repository using the user's credentials, stages all changes, commits the changes with a message, checks the URL of the remote repository, and finally pushes the changes to the remote repository.
