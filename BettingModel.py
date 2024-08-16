"""
The betting model is tasked with one very important decison, how much to bet given the current count of cards
"""

import pandas as pd
from sklearn.model_selection import train_test_split

#read in the data
X = pd.read_csv()
y = X.Bet #There will be a column called bet which has the bet placed for the round

# Split up validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,random_state=0)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Function for evaluating model accuracy
def score_dataset(X_train, X_valid, y_train, y_valid, n_estimation):
    model = RandomForestRegressor(n_estimators=n_estimation, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)

# Find an ideal parameter for the model
for n_estimators in range(30,180,10):
    print(str(n_estimators) + score_dataset(X_train,X_valid, y_train, y_valid, n_estimators))

