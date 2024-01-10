from workout_tracker import WorkoutTracker
from tracker_exception import TrackerException

def account_infos():
    """Asks user to APP ID and APP Key from website Sheety.
    """
    app_id = input("Please enter your APP ID from Sheety website: ")
    app_key = input("Please enter your APP Key from Sheety website: ")
    my_tracker.set_account_infos(app_id=app_id, app_key=app_key)
    
    
def sheet_infos():
    """Asks user to the sheet information to save the datas of the tracked exercise/workout.
    """
    authorization = ""
    if (input("Do your sheet has an authorization token(basic or bearer)? 'y' or 'n': ").lower()) == 'y':
        authorization = input("Please enter your authorization token: ")
    sheet_endpoint_url = input("Please give the URL of the sheet endpoint: ")
    sheet_name = input("Please enter the sheet name: ")
    my_tracker.set_sheet_infos(sheet_name=sheet_name, sheet_endpoint=sheet_endpoint_url, authorization=authorization)
    
    
def physical_infos():
    """Asks user to his/her physical informations to set the infos for the tracker.
    """
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
    print("3)Change the sheet endpoint URL from website Sheety.")
    print("4)Change the existing sheet name.")
    print("5)Change the exercise endpoint URL from website Nutritionix.")
    print("6)Change the current weight.")
    print("7)Change the current age.")
    print("8)Change the current gender.")
    print("9)Change the current height.")
    print("10)Show the current sheet endpoint URL from website Sheety.")
    print("11)Show the current sheet name.")
    print("12)Show the exercise endpoint URL from website Nutritionix")
    print("13)Show the current weight.")
    print("14)Show the current age.")
    print("15)Show the current gender.")
    print("16)Show the current height.")
    print("17)Show calories burned(estimated) for given exercise(s).")
    print("18)Give physical informations again.")
    print("19)Give exercise endpoint informations again.")
    print("20)Give sheet endpoint informations again.")
    print("21)Exit.")
    try:
        answer = int(input("Please choose an option: "))
        if answer == 1:
            exercise = input("Which exercise(s) did you do?:")
            my_tracker.add_exercise(exercise=exercise)
        elif answer == 2:
            my_tracker.get_rows()
        elif answer == 3:
            sheet_url = input("Please give a valid sheet endpoint url: ")
            my_tracker.set_sheet_url(sheet_url=sheet_url)
        elif answer == 4:
            sheet_name = input("Please give a valid sheet name: ")
            my_tracker.set_sheet_name(sheet_name=sheet_name)
        elif answer == 5:
            exercise_url = input("Please give a valid exercise endpoint url: ")
            my_tracker.set_exercise_url(exercise_url==exercise_url)
        elif answer == 6:
            weight = int(input("Please enter your weight: "))
            my_tracker.set_weight(weight=weight)
        elif answer == 7:
            age = int(input("Please enter your age: "))
            my_tracker.set_age(age=age)
        elif answer == 8:
            gender = int(input("Please enter your gender(male or female): "))
            my_tracker.set_gender(gender=gender)
        elif answer == 9:
            height = int(input("Please enter your height: "))
            my_tracker.set_height(height=height)
        elif answer == 10:
            print(f"Current sheet URL: {my_tracker.get_sheet_url()}")
        elif answer == 11:
            print(f"Current sheet name: {my_tracker.get_sheet_name()}")
        elif answer == 12:
            print(f"Current exercise URL: {my_tracker.get_exercise_url()}")
        elif answer == 13:
            print(f"Current weight: {my_tracker.get_weight()} kg.")
        elif answer == 14:
            print(f"Current age: {my_tracker.get_age()} years old.")
        elif answer == 15:
            print(f"Current gender: {my_tracker.get_gender()}.")
        elif answer == 16:
            print(f"Current height: {my_tracker.get_height()} cm.")
        elif answer == 17:
            exercise = input("For which exercise(s) estimated calories would you wanna see(please describe the exercise(s)): ")
            my_tracker.get_calories(exercise=exercise)
        elif answer == 18:
            physical_infos()
        elif answer == 19:
            account_infos()
        elif answer == 20:
            sheet_infos()
        elif answer == 21:
            is_on = False
            print("See you later!")
        else:
            print("Please enter a valid option.")
    except KeyError as e:
        print("Error: ", e)
        print("Possible situations:")
        print("Unvalid ID or/and Key, that's why response is not optimal.")
        print("There can be an auth token. Please check that again.")
        print("Sheet names aren't matching.")
    except ValueError as e:
        print("Error: ", e)
        print("Please be careful by giving the values. Some values should be number rather then character.")
        print("For example -> Option, age, height, weight, etc.")
        print("URLs and sheet names should be accurate too.")
    except TrackerException as e:
        print("Error, message: ", e)
        
    

