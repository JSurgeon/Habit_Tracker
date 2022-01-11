# main python script for Habit Tracker App
from database import Database

class Main():
    data = Database()

    def run(self):
        self.welcome()

        self.display_or_create()

    def welcome(self):
        print("Welcome!")
    
    def create_entry():
        # get all habits already in database
        
    def display_or_create(self, bool):
        if bool == 1:
            return self.data.display_all()
        
        if bool == 2:
            return self.create_entry()
        
        else:
            i = input("Please choose from the following options\n(1) Display current data\n(2) Create new habit entry")
            return display_or_create(i)
    
    
