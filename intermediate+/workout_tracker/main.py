from workout_tracker import WorkoutTracker
from tracker_exception import TrackerException

print("Welcome to the Workout Tracker Prgoram!")
print("Firstly, your informations are needed for executing.")

is_on = True
while is_on:
    try:
        my_tracker = WorkoutTracker()
    except ValueError as e:
        print("Error: ", e)
        print("Please be careful by giving the values. Some values should be number rather then character.")
        print("For example -> Age, height, weight, etc.")
    except TrackerException as e:
        print("Error by setting up the personal properties: ", e)
        print("Please try again.")
    else:
        is_on = False

is_on = True
while is_on:
    print("Options:")
    print("1)Add exercise to sheet.")
    print("2)Show entries of workouts.")
    print("3)Change the sheet url from sheety web.")
    print("4)Change the existing sheet name.")
    print("5)Give physical informations again.")
    print("6)Give accocunt informations again.")
    print("7)Change the current weight.")
    print("8)Change the current age.")
    print("9)Change the current gender.")
    print("10)Change the current height.")
    print("11)Exit.")
    try:
        answer = int(input("Please choose an option:"))
        if answer == 1:
            my_tracker.add_exercise()
        elif answer == 2:
            my_tracker.get_rows()
        elif answer == 3:
            sheet_url = input("Please give a valid sheet url: ")
            my_tracker.set_sheet_url(url=sheet_url)
        elif answer == 4:
            sheet_name = input("Please give a valid sheet name: ")
            my_tracker.set_sheet_name(sheet_name=sheet_name)
        elif answer == 5:
            my_tracker.set_personal_properties()
        elif answer == 6:
            my_tracker.set_account_infos()
        elif answer == 7:
            my_tracker.set_weight()
        elif answer == 8:
            my_tracker.set_age()
        elif answer == 9:
            my_tracker.set_gender()
        elif answer == 10:
            my_tracker.set_height()
        elif answer == 11:
            is_on = False
            print("See you later!")
        else:
            print("Please enter a valid option.")
    except ValueError as e:
        print("Error: ", e)
        print("Please be careful by giving the values. Some values should be number rather then character.")
        print("For example -> Option, age, height, weight, etc.")
    except TrackerException as e:
        print("Error, message: ", e)
        
    

