# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("jo.csv")

# Feature Engineering
X = pd.get_dummies(df[['Location', 'Enemy']], columns=['Location', 'Enemy'])
y = df['Team_Leader']  # Target variable for Team Leader
p = df['Avenger1']  # Target variable for Avenger1
q = df['Avenger2']  # Target variable for Avenger2
r = df['Avenger3']  # Target variable for Avenger3

# Split the data into training and testing sets for each target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, p_train, p_test = train_test_split(X, p, test_size=0.2, random_state=42)
X_train, X_test, q_train, q_test = train_test_split(X, q, test_size=0.2, random_state=42)
X_train, X_test, r_train, r_test = train_test_split(X, r, test_size=0.2, random_state=42)

# Train a RandomForestClassifier for each target variable
model_y = RandomForestClassifier()
model_p = RandomForestClassifier()
model_q = RandomForestClassifier()
model_r = RandomForestClassifier()

model_y.fit(X_train, y_train)
model_p.fit(X_train, p_train)
model_q.fit(X_train, q_train)
model_r.fit(X_train, r_train)

# Evaluate the models
y_pred = model_y.predict(X_test)
accuracy_y = accuracy_score(y_test, y_pred)
print("Accuracy for Team Leader:", accuracy_y)

p_pred = model_p.predict(X_test)
accuracy_p = accuracy_score(p_test, p_pred)
print("Accuracy for Avenger1:", accuracy_p)

q_pred = model_q.predict(X_test)
accuracy_q = accuracy_score(q_test, q_pred)
print("Accuracy for Avenger2:", accuracy_q)

r_pred = model_r.predict(X_test)
accuracy_r = accuracy_score(r_test, r_pred)
print("Accuracy for Avenger3:", accuracy_r)

# Make predictions for new location and enemy information
new_location = 'Tokyo'
new_enemy = 'Hydra'

# Ensure that the new data has the same categorical values as the training data
new_data = pd.DataFrame({'Location': [new_location], 'Enemy': [new_enemy]})
X_new_data = pd.get_dummies(new_data, columns=['Location', 'Enemy'])

# Ensure that the new data has the same one-hot encoded columns as the training data
missing_cols = set(X_train.columns) - set(X_new_data.columns)
for col in missing_cols:
    X_new_data[col] = 0

# Reorder the columns to match the order during training
X_new_data = X_new_data[X_train.columns]

# Predict the team leader and avengers for new data
predicted_team_leader = model_y.predict(X_new_data)
predicted_avenger1 = model_p.predict(X_new_data)
predicted_avenger2 = model_q.predict(X_new_data)
predicted_avenger3 = model_r.predict(X_new_data)

print("Predicted Team Leader:", predicted_team_leader[0])
print("Predicted Avenger1:", predicted_avenger1[0])
print("Predicted Avenger2:", predicted_avenger2[0])
print("Predicted Avenger3:", predicted_avenger3[0])
