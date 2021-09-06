import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor as rfr

if __name__ == '__main__':

    data = pd.read_csv('data/processed_data.csv')

    categorical_cols = data.select_dtypes(include=['object']).columns

    dummies = pd.get_dummies(data[categorical_cols], drop_first = True)

    data_auto = pd.concat([data, dummies], axis = 1)
    data_auto.drop( categorical_cols, axis = 1, inplace = True)

    X = data_auto.drop(columns=['price'])
    y = data_auto['price']

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    Rfr = rfr(n_estimators = 100, criterion = 'mse',
                              random_state = 1,
                             )

    Rfr.fit(X_train,y_train)

    x_train_pred = Rfr.predict(X_train)
    x_test_pred = Rfr.predict(X_test)

    print('MSE train data: %.3f, MSE test data: %.3f' % 
      (metrics.mean_squared_error(x_train_pred, y_train),
       metrics.mean_squared_error(x_test_pred, y_test)))

    print('R2 train data: %.3f, R2 test data: %.3f' % 
        (metrics.r2_score(y_train,x_train_pred, y_train),
        metrics.r2_score(y_test,x_test_pred, y_test)))