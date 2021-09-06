import pandas as pd

data = pd.read_csv('../data/advertising.csv')

X = data.drop(columns=['Sales'])
y = data['Sales']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=10)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)

from sklearn import metrics
mse = metrics.mean_squared_error(y_test,y_pred)
print(mse)

print()

coeff_df = pd.DataFrame(regressor.coef_,X.columns,columns=['Coefficient'])
print(coeff_df)

print()

import pickle
model_internship = pickle.dump(regressor, open('model/internship.pkl','wb'))
