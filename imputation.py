import pandas as pd
import  numpy as np

class Imputation:
    def __init__(self, dataset):
        self.data=dataset

    def tasks(self):
        while True:
            print("Imputation Tasks")
            print()
            print("1. Show number of Null Values")
            print("2. Remove columns")
            print("3. Remove rows")
            print("4. Fill Null Values (with mean)")
            print("5. Fill Null Values (with median)")
            print("6. Fill Null Values (with mode)")
            print("7. Show the Dataset")
            print()
            val=int(input("What do you want to do? (Press -1 to go back) "))

            if val==1:
                self.showNull()
        
            elif val==2:
                self.removeColumns()

            elif val==3:
                self.removeRows()

            elif val==4:
                self.null_mean()
            
            elif val==5:
                self.null_median()
            
            elif val==6:
                self.null_mode()

            elif val==7:
                self.showDataset()

            elif val==-1:
                break

    def showNull(self):
        print(self.data.isnull().sum())

    def removeColumns(self):
        while True:
            print("The list of columns: ")
            for i in self.data.columns:
                print(i, end="  ")
            print()

            while True:
                col=input("Enter the column you want to remove: ")
                if col in self.data.columns:
                    self.data.drop(col,axis=1,inplace=True)
                    print("Column "+col+" is removed from the dataset.")
                    break
                else:
                    print("You entered the wrong value of column, which is not present in columns. So please re-enter the column name.")
                    continue
            
            val=int(input("If you want to remove more press 1 else 0"))
            print()
            if val==1:
                continue
            elif val==0:
                break
    
    def removeRows(self):
        print("Shape of dataset before deleting: ", self.data.shape)
        self.data.dropna(inplace=True)
        print("Shape of dataset after deleting: ", self.data.shape)

    def null_mean(self):
        while True:
            print("The list of columns: ")
            for i in self.data.columns:
                print(i, end="  ")
            print()
            while True:
                col=input("Enter the column you want to be filled with mean: ")
                if col in self.data.columns:
                    if self.data.dtypes[col]==np.object:
                        print(col+" doesnt't have numeric values so can't be filled with mean")
                        break
                    self.data[col].replace(np.nan, self.data[col].mean(),inplace=True)
                    print("Column's Null values "+col+" are filled with mean of the "+col)
                    break
                else:
                    print("You entered the wrong value of column, which is not present in columns. So please re-enter the column name.")
                    continue 
            val=int(input("If you want to remove more press 1 else 0: "))
            print()
            if val==1:
                continue
            elif val==0:
                break    
        
        
    def null_median(self):
        while True:
            print("The list of columns: ")
            for i in self.data.columns:
                print(i, end="  ")
            print()
            while True:
                col=input("Enter the column you want to be filled with median: ")
                if col in self.data.columns:
                    if self.data.dtypes[col]==np.object:
                        print(col+" doesnt't have numeric values so can't be filled with median")
                        break
                    self.data[col].replace(np.nan, self.data[col].median(), inplace=True)
                    print("Column's Null values "+col+" are filled with median of the "+col)
                    break
                else:
                    print("You entered the wrong value of column, which is not present in columns. So please re-enter the column name.")
                    continue 

            val=int(input("If you want to remove more press 1 else 0: "))
            print()
            if val==1:
                continue
            elif val==0:
                break  

    def null_mode(self):
        while True:
            print("The list of columns: ")
            for i in self.data.columns:
                print(i, end="  ")
            print()
            while True:
                col=input("Enter the column you want to be filled with mode: ")
                if col in self.data.columns:
                    self.data[col].replace(np.nan, self.data[col].mode()[0], inplace=True)
                    print("Column's Null values "+col+" are filled with mode of the "+col)
                    break
                else:
                    print("You entered the wrong value of column, which is not present in columns. So please re-enter the column name.")
                    continue    

            val=int(input("If you want to remove more press 1 else 0: "))
            print()
            if val==1:
                continue
            elif val==0:
                break  

    def showDataset(self):
        rows = int(input("Enter number of rows: "))
        print(self.data.head(rows))