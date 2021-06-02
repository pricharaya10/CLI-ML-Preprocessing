from xml.etree.ElementInclude import include
import pandas as pd
import  numpy as np

class Categorical_Encoding:
    def __init__(self, dataset):
        self.data=dataset
        self.col_list=self.data.select_dtypes(include=['object']).columns

    def tasks(self):
        while True:
            print(" Tasks")
            print()
            print("1. Show Categorical Columns")
            print("2. Performing Ordinal Encoding")
            print("3. Performing One Hot Encoding")
            print("4. Performing Dummy Variable Encodings")
            print("5. Show the Dataset")
            print()
            val=int(input("What do you want to do? (Press -1 to go back) "))

            if val==1:
                self.showCol()

            elif val==2:
                self.ordinalEncoding()
        
            elif val==3:
                self.oneHotEncoding()

            elif val==4:
                self.dummyVariableEncoding()

            elif val==5:
                self.showDataset()

            elif val==-1:
                break

    
    def showCol(self):
        print("Columns: ")
        print()
        print("Category     Unique values", end=" ")
        for i in self.col_list:
            print()
            print(i, "  ", self.data[i].nunique())
        print()

    def ordinalEncoding(self):
        while True:
            print("Columns for which you can perform Ordinal Encoding: ")
            for i in self.col_list:
                print(i)
            print()

            col=input("Enter the name of column for which you want to perform Ordinal Encoding (Press -1 to go back): ")

            if col=='-1':
                break
            
            elif col not in self.col_list:
                print(col + " is not present in above list, please consider the above list")

            else:
                col_unique=self.data[col].unique()
                print(col_unique)
                dict_list= {}
                for i in range(len(col_unique)):
                    print("Enter the value for "+ str(col_unique[i]))
                    value=int(input())
                    print()
                    dict_list[col_unique[i]]=value
                self.data[value]=self.data[col].replace(dict_list)
                print(self.data[value].head())
            

    def oneHotEncoding(self):
        while True:
            print("Columns for which you can perform One Hot Encoding: ")
            for i in self.col_list:
                print(i)
            print()

            col=input("Enter the name of column for which you want to perform One Hot Encoding (Press -1 to go back): ")

            if col=='-1':
                break
            
            elif col not in self.col_list:
                print(col + " is not present in above list, please consider the above list")

            else:
                df=pd.get_dummies(self.data[col])
                print(df)
                self.data=pd.concat([self.data,df],axis='columns')
                self.data.drop([col], axis=1, inplace=True)
                print("One Hot Encoding is done")

                print(self.data.head())


    def dummyVariableEncoding(self):
        while True:
            print("Columns for which you can perform Dummy Variable Encoding: ")
            for i in self.data.select_dtypes(include=['object']).columns:
                print(i)
            print()

            col=input("Enter the name of column for which you want to perform Dummy Variable Encoding (Press -1 to go back): ")

            if col=='-1':
                break
            
            elif col not in self.col_list:
                print(col + " is not present in above list, please consider the above list")

            else:
                df=pd.get_dummies(self.data[col])
                print(df)
                self.data=pd.concat([self.data,df],axis='columns')
                self.data.drop([col], axis=1, inplace=True)
                
                while True:
                    for i in df.columns:
                        print(i)
                    column=input("Enter the name of column for removal: ")
                    if column not in df.columns:
                        continue
                    else:
                        self.data.drop([column], axis=1, inplace=True)
                        break
                
                print("Dummy Variable Encoding is done")
                print(self.data.head())



    def showDataset(self):
        rows = int(input("Enter number of rows: "))
        print(self.data.head(rows))   