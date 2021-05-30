import sys
import pandas as pd
from data_description import Description
from imputation import Imputation

class preProcessing:
    def __init__(self):
        if(len(sys.argv)!=2 or not(sys.argv[1].endswith(".csv"))):
            print("Number of arguments doesn't meet the given condition.")
            return 
        else:
            print("Welcome to the ML Preprocessing CLI")
        
    def remove_columns(self):
        self.df=pd.read_csv("train.csv")
        #print(self.df.columns)
        for i in self.df.columns:
            print(i, end="  ")
        print() 
        while(True): 
            val=input("Enter the target variable to be removed: ")
            #print(val)
            val1=input("Are you sure?(y/n)")
            if (val1=='y' or val1=='Y'):
                if(val in self.df.columns):
                    self.df.drop(val, axis=1, inplace=True)
                    #print(self.df.columns)
                    print("Done...")
                    break
                else:
                    print("You entered the wrong target variable, which is not present in columns. So please re-enter the target variable")
                    continue
            elif val1!='y' and val1!='n' and val1!='Y' and val1!='N':
                print("Since you have inputted the wrong value, you are exited from the program.")
                sys.exit()

    def tasks(self):
        while True:
            print("Tasks (Preprocessing)")
            print()
            print("1. Data Description" )
            print("2. Handling NULL Values")
            print("3. Encoding Categorical Data")
            print("4. Feature Scaling of the Dataset")
            print("5. Dowload the modified dataset")

            val=int(input("What do you want to do ? (Press -1 to exit) "))
        
            if(val==1):
                obj1=Description(self.df)
                obj1.tasks()

            elif(val==2):
                obj2=Imputation(self.df)
                obj2.tasks()

            elif(val==-1):
                break

        

            
            




obj = preProcessing()
obj.remove_columns()
obj.tasks()
