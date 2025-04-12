# Create a list of ages
ages = [90,25,15,75,98,22,14,10,5,6,7,9,10,15,25]
# print(ages)
age_old = [age for age in ages if age>18] # tested 
# print(age_old)
#calculate average age use sum() and len()
average = sum(ages)/len(ages)
print("Average ", average)
#Add your age, then print updated list
ages.append(34)
print("Updated ages: ", ages)

#Loop Through data
#print each age above 25
older_ages = []
print("Ages above 25: ")
for age in ages:
    if age>25:
        older_ages.append(age)
print("New list is: ", older_ages)

#count people eligible to vote (>=18)

count = 0
for age in ages:
    if age>=18:
        count += 1

print("Total voters above 18 are: ", count)


# Buggy code - fix it!
cities = ["New York", "London", "Tokyo"]
for city in cities:
    print("City:", city)