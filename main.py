import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
import pickle

# Reading credit Card Fraud dataset
df = pd.read_csv("creditcard.csv")
#Checking the fist 10 records
df.head(10)

df.info()

df.isnull().sum() #Checking the null values

df['Class'].value_counts()
# Distribution of class
legit = df[df.Class == 0]
fraud = df[df.Class != 0]

fraud.Amount.describe()
#Undersampling the dataset
legit_sample = legit.sample(n=492)


new_df = pd.concat([legit_sample, fraud], axis=0)

# Feature Selection
X = new_df.drop(columns = "Class", axis = 1)
Y = new_df["Class"]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2, stratify = Y , random_state =2)


mutual_info = mutual_info_classif(X_train, Y_train)
mutual_info

mutual_info = pd.Series(mutual_info)
mutual_info.index = X_train.columns
mutual_info.sort_values(ascending = False)

# Plotting the feature based on their importance
mutual_info.sort_values(ascending = False).plot.bar(figsize=(20, 8))


#Here we will be selecting top 20 features
sel_five_cols= SelectKBest(mutual_info_classif, k=21)
sel_five_cols.fit(X_train,Y_train)
X_train.columns[sel_five_cols.get_support()]

#Dropping unwanated features
X_train.drop(['V13','V15','V19','V20','V22','V23','V24','V25','V26'], axis=1 , inplace= True)

#Model training
model = LogisticRegression()
model.fit(X_train,Y_train)

#Model Evaluation
X_train_pred = model.predict(X_train)
train_data_accuracy = accuracy_score(X_train_pred, Y_train)

#Removing the unwanted features from the test set
X_test.drop(['V13','V15','V19','V20','V22','V23','V24','V25','V26'], axis=1, inplace= True)

#Model testing
X_test_pred = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_pred, Y_test)

#Saving the model in the form of pickle file
with open('Credit_Card_pickle','wb') as f:
    pickle.dump(model,f)
