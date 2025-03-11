text = 'i, love, russia,really,hard'
hobbies = text.split(',')

for i in range(0, len(hobbies)):
    hobbies[i] = hobbies[i].capitalize()


result =  ","  .join(hobbies)


print(result)