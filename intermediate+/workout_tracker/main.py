import requests
import os
import datetime as dt
from workout_tracker import WorkoutTracker

print("Welcome to the Workout Tracker Prgoram!")
print("Firstly, your informations are needed for executing.")
my_tracker = WorkoutTracker()

is_on = True
while is_on:
    print("Options:")
    print("1)Add exercise to sheet.")
    print("2)Show entries of workouts.")
    print("3)Change the sheet url from sheety web.")
    print("4)Change the existing sheet name.")
    print("5)Give physical informations again.")
    print("6)Give accocunt informations again.")
    print("7)Exit.")
    answer = int(input("Please choose an option:"))
    
    if answer == 1:
        my_tracker.add_exercise()
    elif answer == 2:
        my_tracker.get_rows()
    elif answer == 3:
        my_tracker.set_sheet_url()
    elif answer == 4:
        my_tracker.set_sheet_name()
    elif answer == 5:
        my_tracker.set_personal_properties()
    elif answer == 6:
        my_tracker.set_account_infos()
    elif answer == 7:
        is_on = False
        print("See you later!")
    else:
        print("Please enter a valid option.")
        
    

