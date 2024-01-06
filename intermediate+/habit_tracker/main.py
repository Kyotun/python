from tracker import Tracker
import os


print("Welcome to the tracker program!")
username = input("Please enter your username(press enter if not exist):")
token = input("Please enter your token(press enter if not exist):")
my_tracker = Tracker(username=username, token=token)


is_on = True
while is_on:
    print("Options:")
    print("1)Create an account.")
    print("2)Create a new graph.")
    print("3)Give a new entry for existing graph.")
    print("4)Update an entry of existing graph.")
    print("5)Delete an entry of existing graph.")
    print("6)Get the informations of an entry.")
    print("7)Change the current token.")
    print("8)Change the current username.")
    print("9)Load the graph informations.")
    print("10)Show urls of existing graphs.")
    print("11)Exit.")
    answer = int(input("Please choose an option:"))
    
    if answer == 1:
        username = input("Please enter your username:")
        token = input("Please enter your token:")
        terms = input("Do you agree the usage/service terms of pixela? 'yes' or 'no':").lower()
        if terms == 'no':
            print("Sorry, account cannot be created.")
        else:
            my_tracker.create_user_account(username=username, token=token, terms="yes", minor="yes")
    elif answer == 2:
        graphid = input("Please enter graphid(just lower cases and numbers):")
        graphname = input("Please enter the graphn name(reading graph, gym notebook, etc.):")
        unit = input("Please enter the unit(kilogram, pages, etc.):")
        unit_type = input("Please enter the unit type(float or int):")
        color = input("Please enter the color(shibafu (green), momiji (red), sora (blue), ichou (yellow), "
                      "ajisai (purple) and kuro (black) are supported as color kind):")
        my_tracker.create_new_graph(graphid=graphid, graph_name=graphname, graph_unit=unit, unit_type=unit_type, pixel_color=color)
    elif answer == 3:
        graphid = input("Please enter graphid(just lower cases and numbers):")
        quantity = input("Plese enter the quantitiy:")
        date = input("Please enter the date(in format yyyyMMdd):")
        my_tracker.put_pixel(graphid=graphid, quantity=quantity, date=date)
    elif answer == 4:
        graphid = input("Please enter graphid(just lower cases and numbers):")
        quantity = input("Plese enter the quantitiy:")
        date = input("Please enter the date(in format yyyyMMdd):")
        my_tracker.put_pixel(graphid=graphid, quantity=quantity, date=date)
    elif answer == 5:
        graphid = input("Please enter graphid(just lower cases and numbers):")
        date = input("Please enter the date(in format yyyyMMdd):")
        my_tracker.delete_pixel(graphid=graphid, date=date)
    elif answer == 6:
        graphid = input("Please enter graphid(just lower cases and numbers):")
        date = input("Please enter the date(in format yyyyMMdd):")
        my_tracker.get_pixel(graphid=graphid, date=date)
    elif answer == 7:
        new_token = input("Please enter the new token:")
        my_tracker.set_token(token=token)
    elif answer == 8:
        new_username = input("Please enter the new username:")
        my_tracker.set_username(username=username)
    elif answer == 9:
        my_tracker.load_graphs()
    elif answer == 10:
        print(my_tracker.show_graph_infos())
    elif answer == 11:
        is_on = False
        print("See you later!")
        
        
        
    
