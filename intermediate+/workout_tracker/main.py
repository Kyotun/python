from workout_tracker import WorkoutTracker
from tracker_exception import TrackerException

def account_infos():
    app_id = input("Please enter your APP Id from Sheety website.")
    app_key = input("Please enter your APP Id from Sheety website.")
    my_tracker.set_account_infos(app_id=app_id, app_key=app_key)
    
    
def sheet_infos():
    authorization = ""
    if (input("Do your sheet has an authorization token(basic or bearer)? 'y' or 'n': ").lower()) == 'y':
        authorization = input("Please enter your authorization token: ")
    sheet_name = input("Please enter the sheet name: ")
    my_tracker.set_sheet_infos(sheet_name=sheet_name, authorization=authorization)
    
    
def physical_infos():
    gender = input("Please enter your gender('male' or 'female'): ").lower()
    weight = int(input("Please enter your weight(in kg, just numbers): "))
    height = int(input("Please enter your height(in cm, just numbers): "))
    age = int(input("Please enter your age(in year(s), just numbers): "))
    my_tracker.set_personal_properties(gender=gender, age=age, height=height, weight=weight)
    
    
print("Welcome to the Workout Tracker Prgoram!")
print("Firstly, your informations are needed for executing.")
my_tracker = WorkoutTracker()

is_on = True
while is_on:
    try:
        account_infos()
        sheet_infos()
        physical_infos()
    except ValueError as e:
        print("Error: ", e)
        print("Please be careful by giving the values. Some values should be number rather then character.")
        print("For example -> Age, height, weight, etc.")
    except TrackerException as e:
        print("Error: ", e)
        print("Please try again.")
    else:
        is_on = False

is_on = True
while is_on:
    print("Options:")
    print("1)Add exercise to sheet.")
    print("2)Show entries of workouts.")
    print("3)Change the sheet endpoint url from sheety web.")
    print("4)Change the existing sheet name.")
    print("5)Change the exercise endpoint url.")
    print("6)Give physical informations again.")
    print("7)Give accocunt informations again.")
    print("8)Give sheet informations again.")
    print("9)Change the current weight.")
    print("10)Change the current age.")
    print("11)Change the current gender.")
    print("12)Change the current height.")
    print("13)Exit.")
    try:
        answer = int(input("Please choose an option: "))
        if answer == 1:
            my_tracker.add_exercise()
        elif answer == 2:
            my_tracker.get_rows()
        elif answer == 3:
            sheet_url = input("Please give a valid sheet endpoint url: ")
            my_tracker.set_sheet_url(url=sheet_url)
        elif answer == 4:
            sheet_name = input("Please give a valid sheet name: ")
            my_tracker.set_sheet_name(sheet_name=sheet_name)
        elif answer == 5:
            exercise_url = input("Please give a valid exercise endpoint url: ")
            my_tracker.set_exercise_url(url=exercise_url)
        elif answer == 6:
            physical_infos()
        elif answer == 7:
            account_infos()
        elif answer == 8:
            sheet_infos()
        elif answer == 9:
            weight = int(input("Please enter your weight: "))
            my_tracker.set_weight(weight=weight)
        elif answer == 10:
            age = int(input("Please enter your age: "))
            my_tracker.set_age()
        elif answer == 11:
            gender = int(input("Please enter your gender(male or female): "))
            my_tracker.set_gender()
        elif answer == 12:
            height = int(input("Please enter your height: "))
            my_tracker.set_height()
        elif answer == 13:
            is_on = False
            print("See you later!")
        else:
            print("Please enter a valid option.")
    except ValueError as e:
        print("Error: ", e)
        print("Please be careful by giving the values. Some values should be number rather then character.")
        print("For example -> Option, age, height, weight, etc.")
        print("URLs and sheet names should be accurate too.")
    except TrackerException as e:
        print("Error, message: ", e)
        
    

