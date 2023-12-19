import random

# names = ["Alex", "Beth", "Caroline", "David", "Eleanor", "Freddie"]

# # Create a dictionary with list and dictionary comprehension
# students_scores = {student:random.randint(1,100) for student in names}

# # Create a dictionary that contains the students and their notes as key,value pairs.
# passed_students = {student:value for (student,value) in students_scores.items() if value > 60}
# print(passed_students)

# # An Example to understand dictionary comprehensions
# # Split the sentence into seperate words with split whitespace ' '
# # At the end create a dict contains word:len(word)
# sentence = input("Please write a sentence: ")
# dict_len_words = {word:len(word) for word in sentence.split()}
# print(dict_len_words)

# An Example of creating a dict of celcius that converted from fahrenheit.
# (temp_c * 9/5) + 32 = temp_f
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:((temp* 9/5) + 32) for (day,temp) in weather_c.items()}
print(weather_f)
