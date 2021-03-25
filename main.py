import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# inserting data
score_data = pd.read_csv('data1516.csv')
x = score_data[['Home_3rdQ','Away_3rdQ']]
y = score_data.iloc[:,-1]

# train-test-split and scaling data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
scaler = StandardScaler()
train_features = scaler.fit_transform(X_train)
test_features = scaler.transform(X_test)

# initialising model
model = LogisticRegression(max_iter=25000)
model.fit(X_train, y_train)


