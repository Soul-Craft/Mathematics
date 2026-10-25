from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
import pandas as pd

# scikit-learn 1.2 removed load_boston; the California housing set is its documented replacement.
# The first call downloads it (about 400 KB) and caches it in ~/scikit_learn_data.
housing_data = fetch_california_housing(as_frame=True)
x = housing_data['data']
y = housing_data['target']

model = LinearRegression().fit(x, y)

# MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
sample_house = pd.DataFrame([[8.3252, 41.0, 6.98412698, 1.02380952, 322.0, 2.55555556, 37.88, -122.23]],
                            columns=housing_data['feature_names'])

# Median house value, in units of $100,000
prediction = model.predict(sample_house)
print(prediction)
