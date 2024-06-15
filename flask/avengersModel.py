import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Load the dataset from CSV file
df = pd.read_csv("data.csv")

# Drop rows with missing target values
df.dropna(subset=['Mission Status'], inplace=True)

# Convert categorical variables to numerical using LabelEncoder
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    if column not in ['Mission ID', 'Enemy Team']:  # Exclude Mission ID and Enemy Team from encoding
        label_encoders[column] = LabelEncoder()
        df[column] = label_encoders[column].fit_transform(df[column])

# Drop the 'Enemy Team' column from the features
X = df.drop(['Mission Status', 'Mission ID', 'Enemy Team'], axis=1)

# Specify the target variable
y = df['Mission Status']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the logistic regression model
model = LogisticRegression()

# Train the logistic regression model
model.fit(X_train, y_train)

# Predict the mission success for each mission in the test set
predictions = model.predict(X_test)

# Print the predicted mission success for each mission
import random

def predict_mission_success(avenger, location_type, strategy):
    # Encode categorical variables
    avenger_encoded = label_encoders['Avenger'].transform([avenger])[0]
    location_type_encoded = label_encoders['Location Type'].transform([location_type])[0]
    strategy_encoded = label_encoders['Strategy'].transform([strategy])[0]

    # Create a feature array for prediction
    feature_array = [[avenger_encoded, location_type_encoded, strategy_encoded]]

    # Predict the success of the mission
    prediction = model.predict(feature_array)

    # Print the predicted mission success
    print(f"Predicted Mission Success: {'Yes' if prediction[0] == 1 else 'No'}")

# Usage example
predict_mission_success('Iron Man (Tony Stark)', 'Urban','Strategic planning')  # Replace with appropriate values
 