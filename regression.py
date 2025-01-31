

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


df = pd.read_csv('product_pricing_dataset (1).csv')

df.head()

df.shape

df.isnull().sum()

# Visualize Price vs Units Sold
sns.scatterplot(x="Price", y="Units_Sold", hue="Product_Category", data=df)
plt.title("Price vs Units Sold")
plt.show()

# Feature Selection
X = df[["Price", "Competitor_Price", "Customer_Rating", "Demand_Elasticity"]]
y = df["Units_Sold"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predictions and Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

import joblib

# Save the model
joblib.dump(model, "pricing_model.pkl")
print("Model saved as 'pricing_model.pkl'.")
