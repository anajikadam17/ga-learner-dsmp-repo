# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here

df = pd.read_csv(path)
print(df.head())
X = df.drop(['list_price'], axis = 1) 
y = df.iloc[:,2]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 6)
# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here 
cols = X_train.columns
fig ,axes = plt.subplots(nrows = 3 , ncols = 3)
for i in range(0,3):
    for j in range(0,3):
        col = cols[i*3+j]
        axes[i,j].scatter(X_train[col],y_train)
        plt.show()


# code ends here



# --------------
# Code starts here


corr = X_train.corr()
print(corr)


X_train = X_train.drop(['play_star_rating', 'val_star_rating'], axis = 1) 
X_test = X_test.drop(['play_star_rating', 'val_star_rating'], axis = 1) 
# Code ends here


# --------------

#Task 1 -  Data loading and splitting
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df=pd.read_csv(path)
df.head(5)
X=df[['ages','num_reviews','piece_count','play_star_rating','review_difficulty','star_rating','theme_name','val_star_rating','country']]
y=df['list_price']
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size = 0.3, random_state = 6)
# code ends here
#Task 2 - Predictor Check!
import matplotlib.pyplot as plt
# code starts here
cols=X_train.columns
fig,axes=plt.subplots(nrows=3, ncols=3)
for i in range(0,3):
   for j in range(0,3):
       col=cols[i*3+j]
       axes[i,j].scatter(X_train[col],y_train)
       plt.show()
# code ends here
#Task 3 - Reduce feature redundancies!
# Code starts here
corr=X_train.corr()
print(corr)
X_train.drop(columns=['play_star_rating','val_star_rating'],inplace=True)
X_test.drop(columns=['play_star_rating','val_star_rating'],inplace=True)
# Code ends here
#Task 4 - Is my price prediction ok?
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Code starts here
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
print(mse)
r2=r2_score(y_test,y_pred)
print(r2)
# Code ends here


# --------------
# Code ends here
residual= y_test - y_pred
residual.plot(kind = 'hist')
plt.show()


