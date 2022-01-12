# python file containing database class
import pandas as pd

class Database():
    '''Responsible for reading from csv file and storing entry data'''
    def __init__(self, filename = None):
        self.file = filename
        if self.file:
            self.df = pd.read_csv(self.file)

        else:
            self.df = pd.DataFrame()

    def get_habits(self):
        return self.df.columns[2:]

    def display_all(self):
        '''Displays Database object's DataFrame'''
        
        # print df
        print(self.df.to_string())
        return True

    def add_entry(self, entry):
        # appends entry to dataframe. Returns True if successful, False otherwise
        if type(entry) != dict: 
            return False
        
        self.df = self.df.append(entry, ignore_index = True)
        return True

    def write(self):
        '''Writes the DataFrame to a csv'''
        self.df.to_csv(self.file)