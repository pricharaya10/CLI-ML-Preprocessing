import pandas as pd
import sys

class Description:
    def __init__(self, dataset):
        self.data=dataset
        

    def tasks(self):
        while True:
            print("Tasks (Data Description)")
            print()
            print("1. Describe a specific column")
            print("2. Show properties of each column")
            print("3. Show the dataset")
            print()
            val=int(input("What do you want to do? (Press -1 to go back) "))

            if val==1:
                self.description_column()
        
            elif val==2:
                self.properties()

            elif val==3:
                self.showData()

            elif val==-1:
                break

    def description_column(self):
        print("Columns: ")
        self.data=pd.read_csv("train.csv")
        for i in self.data.columns:
            print(i, end="  ")
        print() 
        while(True):
            value=input("Enter the column for which you want a description :")
            if value in self.data.columns:
                print(self.data[value].describe())
                break
            else:
                print("You entered the wrong target variable, which is not present in columns. So please re-enter the target variable")
                continue

    def properties(self):
        print(self.data.describe())
        print(self.data.info)

    
    def showData(self):
        rows = int(input("Enter number of rows: "))
        print(self.data.head(rows))