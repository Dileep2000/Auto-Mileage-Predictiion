import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from catboost import CatBoostRegressor
import warnings
warnings.filterwarnings('ignore')
class MPG_Prediction:
    def predict(test):
        data=pd.read_csv('auto-mpg.data',names=['MPG','Cylinders','Displacement','Horsepower','Weight','Acceleration','Model Year','Origin'],na_values='?',comment='\t',skipinitialspace=True,sep=" ")
        Y=data['MPG']
        data.drop('MPG',axis=True,inplace=True)
        imputer=KNNImputer()
        scaler=StandardScaler()
        data=scaler.fit_transform(data)
        X=data
        X=imputer.fit_transform(X)
        CAT=CatBoostRegressor(depth=7,learning_rate=0.05,n_estimators=300)
        CAT.fit(X,Y)
        test=scaler.transform(test)
        test=imputer.transform(test)
        
        return CAT.predict(test)[0]
