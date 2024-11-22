from flask import Flask, render_template, request
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ETS.ets import forecast_ets

app = Flask(__name__)

# Define paths to data files
DATA_PATHS = {
    'A2': os.path.join(os.path.dirname(__file__), '../dataSet/A2.csv'),
    'A7': os.path.join(os.path.dirname(__file__), '../dataSet/A7.csv'),
    'A9': os.path.join(os.path.dirname(__file__), '../dataSet/A9.csv')
}

@app.route('/', methods=['GET', 'POST'])
def index():
    forecast_results = None
    if request.method == 'POST':
        # Get data from the form
        api_code = request.form['api_code']
        occurrences = int(request.form['occurrences'])
        threshold = 0.01  # Fixed threshold value

        # Ensure the API code is valid
        if api_code in DATA_PATHS:
            data_path = DATA_PATHS[api_code]
            # Call the forecasting function with form data
            forecast_df = forecast_ets(data_path, forecast_steps=100, num_occurrences=occurrences, threshold=threshold)
            # Format the results as a dictionary for display
            forecast_results = forecast_df['Timestamp'].tolist()  # Only pass timestamps
        else:
            forecast_results = "Invalid API Code Selected!"

    return render_template('index.html', forecast_results=forecast_results)

if __name__ == '__main__':
    app.run(debug=True)
