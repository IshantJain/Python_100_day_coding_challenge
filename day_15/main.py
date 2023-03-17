#Program which greet according to the time

import time

timestamp = time.strftime('%H')
print(timestamp)

time = int(timestamp)
if (time < 12):
  print("Good Morning")
elif (time < 18 and time > 12):
  print("Good Afternoon")
elif (time > 18 and time < 24):
  print("Good night")
else:
  print("Enter valid time")
