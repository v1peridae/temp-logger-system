# Task 1
print("TASK 1 \n")

midday_temps = []
midnight_temps = []

for day in range(1, 31):
  midday_temp = float(input(f"Enter the midday temperature for day {day} >>>"))
  midnight_temp = float(
      input(f"Enter the midnight temperature for day {day}>>>"))
  if midday_temp >= 10 or midday_temp <= 45:
    midday_temps.append(midday_temp)
    midnight_temps.append(midnight_temp)
  else:
    print("Invalid temperature. \n")

# Task 2
print("TASK 2 \n")
midday_avg = sum(midday_temps) / len(midday_temps)
midnight_avg = sum(midnight_temps) / len(midnight_temps)

print("Average temperature at midday is", midday_avg, "°C")
print("Average temperature at midnight is", midnight_avg, "°C \n")

# Task 3
print("TASK 3 \n")
max_midday_temp = max(midday_temps)
min_midnight_temp = min(midnight_temps)
print("The highest temperature recorded in the past 30 days was", max_midday_temp)
print("The lowest temperature recorded in the past 30 days was", min_midnight_temp)
