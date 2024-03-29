import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
# Load the dataset
df = pd.read_csv('your_dataset.csv')
X = df[['Road_Conditions', 'Visibility', 'Speed_Limit', 'Num_Vehicles', 'Time_of_Day']]
y = df['Accident_Severity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
# Save the model for future use
joblib.dump(model, 'accident_severity_model.joblib')
accuracy = model.score(X_test, y_test)
print(f'Model Accuracy: {accuracy * 100:.2f}%')
# Example of using the model for prediction
new_data = [[2, 50, 60, 2, 1]]  # Wet road, visibility of 50 meters, speed limit of 60 km/h, 2 vehicles, daytime
predicted_severity = model.predict(new_data)

print(f'Predicted Accident Severity: {predicted_severity[0]:.2f}')