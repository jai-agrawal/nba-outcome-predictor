import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


# import numpy as np
# import matplotlib.pyplot as plt

game_data = pd.read_csv('/Users/jai/Downloads/19oddsFinalToday.csv')
x = game_data[['Home_3rdQ','Away_3rdQ']]
y = game_data.iloc[:,-1]
score_data = pd.read_csv('odds1516.csv')
x1 = score_data[['Home_3rdQ','Away_3rdQ']]
y1 = score_data.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
scaler = StandardScaler()
train_features = scaler.fit_transform(X_train)
test_features = scaler.transform(X_test)

model = LogisticRegression(max_iter=25000)
model.fit(X_train, y_train)

# 80% accuracy on most
# print(model.score(X_train, y_train))
# print(model.score(X_test, y_test))
# print(model.score(x1, y1))


x = input('Enter Home Team Score till 3rdQuarter')
y = input('Enter Away Team Score till 3rdQuarter')

if (model.predict([[x,y]]))[0] == 1:
    print('Home Team Wins')
else:
    print('Away Team Wins')


