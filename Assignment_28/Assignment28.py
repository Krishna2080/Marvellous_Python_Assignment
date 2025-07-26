import pandas as pd
import numpy as np
from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import countplot
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def winepredictor(datapath):

    df=pd.read_csv(datapath)
    print("Dataset Loaded Succesfully :",df.head())

    print("Dimension of dataset :",df.shape)

    df.dropna(inplace=True)

    x=df.drop(columns=['Class'])
    y=df['Class']

    scaler=StandardScaler()
    x_scale=scaler.fit_transform(x)

    x_train, x_test,y_train, y_test=train_test_split(x_scale,y,test_size=0.2,random_state=42)
    
    model=KNeighborsClassifier()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)

    accuracy=accuracy_score(y_test,y_pred)
    print(accuracy)


def main():
    
    winepredictor("WinePredictor.csv")

      
if __name__=="__main__":
    main()