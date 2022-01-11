# python file containing database class
import pandas as pd

class Database():
    '''Responsible for reading from csv file and storing entry data'''
    def __init__(self, filename = None):
        
        if filename:
            self.df = pd.read_csv(filename)

        else:
            self.df = pd.DataFrame()

    def return_habits(self):
        return self.df.columns
    def display_all(self):
        print(self.df)

    