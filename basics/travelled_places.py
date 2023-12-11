#Add countries and cities that travelled

def add_new_country(name, time_visited, cities):
    func_dict = {}
    func_dict["country"] = name
    func_dict["visits"] = time_visited
    func_dict["cities"] = cities
    travel_log_list.append(func_dict)

country = input("Which country have you visited this time: ")
visits = int(input("What is the number of visits now: "))
list_of_cities = input("Can you please type all of the cities been visited: ").split()

travel_log_list = [
    {
        "country" : "France",
        "visits" : 8,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 2,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

add_new_country(name=country, time_visited=visits, cities=list_of_cities)
print(travel_log_list)