import pandas as pd
import  numpy as np
import sys
import os

class Download:
    def __init__(self, dataset):
        self.data=dataset

    def tasks(self):
        while 1:
            val=input("Enter the FILENAME you want ? (Press -1 to go back): ")

            file=val+'.csv'

            b=os.listdir()
            print(b)

            c=0
            for i in b:
                if i==file:
                    c=1
                    print("This file name already exists, Enter another one..")
                    break
            if c==1:
                continue

            else:
                pd.DataFrame(self.data).to_csv(file,index=False)
                print()
                print("We're done.. Hurray!!")
                sys.exit()