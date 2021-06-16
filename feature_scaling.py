import pandas as pd
import  numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

class Features:
    def __init__(self, dataset):
        self.data=dataset

    def tasks(self):
        while True:
            print("Tasks")
            print()
            print("1. Perform Normalization(MinMax Scaler)")
            print("2. Perform Standardization(Standard Scaler)")
            print("3. Show the Dataset")
            print()
            val=int(input("What do you want to do? (Press -1 to go back) "))

            if val==1:
                self.normalize()

            elif val==2:
                self.standardize()

            elif val==3:
                self.showDataset()

            elif val==-1:
                break

    def normalize(self):
        while True:
            print("Tasks")
            print()
            print("1. Normalization on one column")
            print("2. Normalization on full dataset")
            print("3. Show dataset")
            print()

            val=int(input("What do you want to do? (Press -1 to go back) "))

            if val==1:
                self.normalizeOne()

            elif val==2:
                self.normalizeAll()

            elif val==3:
                self.showDataset()

            elif val==-1:
                break

    def normalizeOne(self):
        while True:
            print("List of all the columns along with their datatypes")
            print(self.data.dtypes)

            val=input("Enter the column name for which you want to perform normalization(Press -1 to go back): ")
            if val=='-1':
                break
            else:
                if val not in self.data.columns:
                    print("The column you entered is not present")
                    print()
                    continue

                else:
                    scaler = MinMaxScaler()
                    self.data[[val]] = scaler.fit_transform(self.data[[val]])

                    print("Normalization of "+val+ " is done")


    def normalizeAll(self):
        col_list = self.data.select_dtypes(exclude=['object']).columns
        scaler = MinMaxScaler()
        self.data[col_list] = scaler.fit_transform(self.data[col_list])

        print("Normalization of the dataset is done")
            


    def standardize(self):
        while True:
            print("Tasks")
            print()
            print("1. Standardization on one column")
            print("2. Standardization on full dataset")
            print("3. Show dataset")
            print()

            val=int(input("What do you want to do? (Press -1 to go back) "))

            if val==1:
                self.standardizeOne()

            elif val==2:
                self.standardizeAll()

            elif val==3:
                self.showDataset()

            elif val==-1:
                break

    def standardizeOne(self):
        while True:
            print("List of all the columns along with their datatypes")
            print(self.data.dtypes)

            val=input("Enter the column name for which you want to perform standardization(Press -1 to go back): ")
            if val=='-1':
                break
            else:
                if val not in self.data.columns:
                    print("The column you entered is not present")
                    print()
                    continue

                else:
                    scaler = StandardScaler()
                    self.data[[val]] = scaler.fit_transform(self.data[[val]])

                    print("Standardization of "+val+ " is done")

    
    def standardizeAll(self):
        col_list = self.data.select_dtypes(exclude=['object']).columns
        scaler = StandardScaler()
        self.data[col_list] = scaler.fit_transform(self.data[col_list])

        print("Standardization of the dataset is done")



    def showDataset(self):
            rows = int(input("Enter number of rows: "))
            print(self.data.head(rows))