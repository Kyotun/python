import datetime as dt

time_now = dt.datetime.now()
print(f"Microsecond: {time_now.microsecond}")
print(f"Second: {time_now.second}")
print(f"Hour: {time_now.hour}")
print(f"Day: {time_now.day}")
print(f"Year: {time_now.year}")
print(f"Date: {time_now.date()}")
print(f"Timezone: {time_now.astimezone()}")