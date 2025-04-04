import random

days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П’ятниця", "Субота", "Неділя"]
temperatures = {}

for day in days:
    temp = random.randint(-5, 35)
    temperatures[day] = temp

print("Погода на тиждень:\n")
for day, temp in temperatures.items():
    print(f"{day}: {temp}°C")

values = list(temperatures.values())
average_temp = sum(values) / len(values)
max_temp = max(values)
min_temp = min(values)

hottest_days = [day for day, temp in temperatures.items() if temp == max_temp]
coldest_days = [day for day, temp in temperatures.items() if temp == min_temp]

print("\nСтатистика:")
print(f"Середня температура: {average_temp:.1f}°C")
print(f"Найспекотніший день(і): {', '.join(hottest_days)} ({max_temp}°C)")
print(f"Найпрохолодніший день(і): {', '.join(coldest_days)} ({min_temp}°C)")

warm_days = [day for day, temp in temperatures.items() if temp >= average_temp]
cool_days = [day for day, temp in temperatures.items() if temp < average_temp]

print("\nКласифікація:")
print(f"Теплі дні: {', '.join(warm_days)}")
print(f"Прохолодні дні: {', '.join(cool_days)}")
