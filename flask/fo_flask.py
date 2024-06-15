import pandas as pd
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("ok.csv")

# Encoding categorical variables
df_encoded = pd.get_dummies(df, columns=['Team_Leader', 'Avenger1', 'Avenger2', 'Avenger3', 'Location', 'Enemy', 'Weather', 'Time_of_Day'])

# Preprocess the 'Duration' column
df_encoded['Duration'] = df_encoded['Duration'].str.replace(' hours', '').astype(float)

# Splitting into features (X) and target variable (y)
X = df_encoded.drop(['Outcome'], axis=1)
y = df_encoded['Outcome']

# Initialize the Random Forest classifier
model = RandomForestClassifier()

# Train the model
model.fit(X, y)

# Initialize Flask app
app = Flask(__name__)

# Prediction function
def predict_battle_outcome(battle_details):
    # Convert 'Duration' to string
    battle_details['Duration'] = str(battle_details['Duration'])

    # Prepare input data
    battle_details_encoded = pd.get_dummies(pd.DataFrame([battle_details]), columns=['Team_Leader', 'Avenger1', 'Avenger2', 'Avenger3', 'Location', 'Enemy', 'Weather', 'Time_of_Day'])

    # Add missing columns if any
    missing_cols = set(X.columns) - set(battle_details_encoded.columns)
    for c in missing_cols:
        battle_details_encoded[c] = 0

    # Reorder columns to match the training data
    battle_details_encoded = battle_details_encoded[X.columns]
    
    # Predict the outcome
    prediction = model.predict(battle_details_encoded)
    
    return "Victory" if prediction[0] == "Victory" else "Defeat"

# Flask endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    battle_details = request.json
    
    # Perform prediction
    outcome = predict_battle_outcome(battle_details)
    
    # Return the predicted outcome
    return jsonify({"outcome": outcome})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5002)
