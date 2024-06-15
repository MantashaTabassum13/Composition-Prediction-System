from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS  # Import CORS from flask_cors
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset for Flask application
df = pd.read_csv("jo.csv")

# Feature Engineering for Flask application
X = pd.get_dummies(df[['Location', 'Enemy']], columns=['Location', 'Enemy'])
y = df['Team_Leader']  # Target variable for Team Leader
p = df['Avenger1']  # Target variable for Avenger1
q = df['Avenger2']  # Target variable for Avenger2
r = df['Avenger3']  # Target variable for Avenger3

# Split the data into training and testing sets for each target variable for Flask application
X_train_y, X_test_y, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_p, X_test_p, p_train, p_test = train_test_split(X, p, test_size=0.2, random_state=42)
X_train_q, X_test_q, q_train, q_test = train_test_split(X, q, test_size=0.2, random_state=42)
X_train_r, X_test_r, r_train, r_test = train_test_split(X, r, test_size=0.2, random_state=42)

# Train a RandomForestClassifier for each target variable for Flask application
model_y = RandomForestClassifier()
model_p = RandomForestClassifier()
model_q = RandomForestClassifier()
model_r = RandomForestClassifier()

model_y.fit(X_train_y, y_train)
model_p.fit(X_train_p, p_train)
model_q.fit(X_train_q, q_train)
model_r.fit(X_train_r, r_train)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dictionary to store danger percentages
danger_percentages = {}

# Flask endpoint for prediction
@app.route('/', methods=['POST'])
def predict():
    # Get data from the request
    data = request.json
    
    # Extract location and enemy from data
    location = data['Location']
    enemy = data['Enemy']
    
    # Prepare input data
    input_data = pd.get_dummies(pd.DataFrame({'Location': [location], 'Enemy': [enemy]}), columns=['Location', 'Enemy'])

    # Ensure that the input data has the same one-hot encoded columns as the training data
    for model, X_train in [(model_y, X_train_y), (model_p, X_train_p), (model_q, X_train_q), (model_r, X_train_r)]:
        missing_cols = set(X_train.columns) - set(input_data.columns)
        for col in missing_cols:
            input_data[col] = 0
        input_data = input_data[X_train.columns]

        # Predict using the corresponding model
        prediction = model.predict(input_data)
        if model == model_y:
            team_leader = prediction[0]
        elif model == model_p:
            avenger1 = prediction[0]
        elif model == model_q:
            avenger2 = prediction[0]
        elif model == model_r:
            avenger3 = prediction[0]

    return jsonify({"Team_Leader": team_leader, "Avenger1": avenger1, "Avenger2": avenger2, "Avenger3": avenger3})

# Flask endpoint for calculating danger
@app.route('/calculate-danger', methods=['POST'])
def calculate_danger():
    data = request.json
    area = data.get('location')

    if not area:
        return jsonify({"error": "Location parameter missing"}), 400

    city_safe = df[df['Location'] == area].shape[0]
    sum_safe = df.shape[0]  # Total number of rows in the dataset
    
    if city_safe == 0:
        return jsonify({"error": "Location not found in dataset"}), 404
    
    danger_percent = sum_safe/city_safe
    
    return jsonify({'danger_percent': danger_percent})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
