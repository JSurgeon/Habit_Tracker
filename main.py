# main python script for Habit Tracker App
from database import Database
from datetime import datetime

DAY_OF_WEEK = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

# To Do
# need to add functionality to ADD a new habit
# add functionality to edit entered values before they are written (corresponding placement marked below)
# error checking inputs with try


class Main():
    data = Database("Practice.csv")

    def run(self):
        self.welcome()

        if self.display_or_create() == "created":
            self.display_or_create(bool = 1)

        self.data.write()


    def welcome(self):
        print("Welcome!")
    
    def create_entry(self):
        '''Return True if entry created successfully, False otherwise'''

        # track time/date entry is created
        now = datetime.now()

        # empyt dictionary object to hold all entry items
        dict = {}

        # add time items to dictionary
        dict["Weekday"] = DAY_OF_WEEK[now.weekday()]   # need to implement string conversion of DoW
        dict["Date"] = now.date().__str__()   # should i be using __str__()? without it, dict["Date"] = date.datetime({date})
        
        # get all habits already in database
        habits = self.data.get_habits()
        
        # remind user of date
        print(f'Filling data for {dict["Weekday"]} {dict["Date"]}')
        
        # for each habit
        for v in habits:
            completed = bool(int(input(f'Did you complete "{v}" today? 0 for no, 1 for yes\n')))
            dict[f'{v}'] = completed

        for k, v  in dict.items():
            print(k, v)
    
        ##########################################
        # need to add possibility of editing of entered values here #  
        # (could also possibly add in the habits loop. IE check for edit before moving on to next habit
        ##########################################

        
        

        return self.data.add_entry(dict)

    
    
    def display_or_create(self, bool = None, flag = None):
        # bool == 1, display all data;
        # bool == 2, create new entry;
        # flag represents if the function has previously been called- for use by this method only
        if bool == 1:
            # call Database object's display_all() function
            self.data.display_all()
            return "displayed"
        if bool == 2:
            # call create_entry()
            self.create_entry()
            return "created"

        else:
            # if flag, then we received an invalid response. Tell the user
            if flag: print("\nInvalid character!")

            # grab input from user
            i = int(input("Please choose from the following options\n(1) Display current data\n(2) Create new habit entry\n"))
            return self.display_or_create(bool = i, flag = True)
    
        
    
obj = Main()
obj.run()