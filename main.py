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

        # track time/date entry is created
        now = datetime.now()

        # empyt dictionary object to hold all entry items
        dict = {}

        # add time items to dictionary
        dict["Day of Week"] = now.weekday()   # need to implement string conversion of DoW
        dict["Date"] = now.date().__str__()   # should i be using __str__()? without it, dict["Date"] = date.datetime({date})
        
        # get all habits already in database
        habits = self.data.get_habits()
        
        # for each habit
        for v in habits:
            completed = bool(int(input(f'Did you complete "{v}" today? 0 for no, 1 for yes\n')))
            dict[f'{v}'] = completed

        for k, v  in dict.items():
            print(k, v)
        self.data.add_entry(dict)

        ##########################################
        # need to add editing possibilities here #  (could also possibly add in the habits loop. IE check for edit before moving on to next habit
        ##########################################

        return self.display_or_create(bool = 1)


    def display_or_create(self, bool = None):
        # bool == 1, display all data;
        # bool == 2, create new entry;
        if bool == 1:
            return self.data.display_all()
        
        if bool == 2:
            return self.create_entry()
        
        else:
            i = int(input("Please choose from the following options\n(1) Display current data\n(2) Create new habit entry\n"))
            return self.display_or_create(bool = i)
    
    
obj = Main()
obj.run()