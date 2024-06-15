import pandas as pd
from sklearn.model_selection import train_test_split
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

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest classifier
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Prediction function
def predict_battle_outcome(model, battle_details):
    # Convert 'Duration' to string
    battle_details['Duration'] = str(battle_details['Duration'])

    # Prepare input data
    battle_details_encoded = pd.get_dummies(pd.DataFrame([battle_details]), columns=['Team_Leader', 'Avenger1', 'Avenger2', 'Avenger3', 'Location', 'Enemy', 'Weather', 'Time_of_Day'])

    # Add missing columns if any
    missing_cols = set(X_train.columns) - set(battle_details_encoded.columns)
    for c in missing_cols:
        battle_details_encoded[c] = 0

    # Reorder columns to match the training data
    battle_details_encoded = battle_details_encoded[X_train.columns]
    
    # Predict the outcome
    prediction = model.predict(battle_details_encoded)
    
    return "Victory" if prediction[0] == "Victory" else "Defeat"

# Example usage
battle_details = {
    'Team_Leader': 'Captain America (Steve Rogers)',
    'Avenger1': 'Hawkeye (Clint Barton)',
    'Avenger2': 'Ant-Man (Scott Lang)',
    'Avenger3': 'Spider-Man (Peter Parker)',
    'Location': 'Washington D.C.',
    'Enemy': 'Hydra',
    'Weather': 'Overcast',
    'Time_of_Day': 'Afternoon',
    'Duration': 3  # No need for 'hours' suffix
}
outcome = predict_battle_outcome(model, battle_details)
print("Predicted Outcome:", outcome)
