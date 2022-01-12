# main python script for Habit Tracker App
from database import Database
from datetime import datetime
class Main():
    data = Database("Practice.csv")

    def run(self):
        self.welcome()

        self.display_or_create()

    def welcome(self):
        print("Welcome!")
    
    def create_entry(self):
        # get all habits already in database
        habits = self.data.get_habits()
        for v in habits:
            print(v)
        now = datetime.now()
        print(now)

    def display_or_create(self, bool):
        if bool == 1:
            return self.data.display_all()
        
        if bool == 2:
            return self.create_entry()
        
        else:
            i = input("Please choose from the following options\n(1) Display current data\n(2) Create new habit entry")
            return self.display_or_create(i)
    
    
obj = Main()
print(obj.create_entry())