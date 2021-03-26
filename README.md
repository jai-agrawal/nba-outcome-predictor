# Predicting the Outcome of an NBA Game with Machine Learning
One may elect for many different options whilst contemplating how to predict the outcome of an NBA game, i.e., who wins the game - Team A or Team B. It's important 
to distinguish these predictions as either being real-time/live or pre-game. One could thus use machine learning techniques such as Logistic Regression on specific
data and labels in order to further predict certain labels (in this case - outcomes of the game) using certain data (in this case - scores from the end of the 3rd 
quarter). 

## Data Used
The data used in this project was previously scraped from stats.nba.com and then formatted for simplicity into a .csv file. More speciifically it conforms to the dates, final, and 3rd-Quarter scores of all matchups that occurred during the 2015-2016 NBA season. 

## Working of the Code
The working of the code is simple. As shown in main.py, the overall flow involves itself with the insertion of the data as a pandas DataFrame, the further splitting 
of said data into data (x) and labels (y). Further, the data is then split into training data and testing data (80-20). Then, the data is scaled using StandardScaler(). Finally, the Logistic Regression Classifier model is initialised and fitted. All of the same have been done using sklearn. 

## Evaluation 
The test data is scored 0.81 approximately using .score(). Prediction of other seasons using the same model yielded scores of around 0.8-0.84. 
