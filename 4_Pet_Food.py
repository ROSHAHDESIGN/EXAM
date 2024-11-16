#pyrvonachalni danni VHOD
days_quantity = int(input())
food_quantity = float(input())

#pomoshtni promenlivi
biscuits = 0
total_food_eaten_by_dog = 0
total_food_eaten_by_cat = 0

for each_day in range(1,days_quantity +1): #sledvashtite danni SA za den
    food_per_day_eaten_by_dog = int(input())
    food_per_day_eaten_by_cat = int(input())
    if each_day % 3 == 0: #ako e VSEKI treti den im davat biscuits
        biscuits += 0.1 * (food_per_day_eaten_by_cat + food_per_day_eaten_by_dog)
    #FOOR LOOP ZA VSQKA ITERATION
    total_food_eaten_by_dog += food_per_day_eaten_by_dog #UVELICHAVA SE VSEKI DEN
    total_food_eaten_by_cat += food_per_day_eaten_by_cat#UVELICHAVA SE VSEKI DEN

total_food_eaten = total_food_eaten_by_cat + total_food_eaten_by_dog

#% hrana za vsichki dni
total_eaten_food_percentage = (total_food_eaten / food_quantity) * 100
#% hrana izyadena ot kuche i kote
dog_eaten_food_percentage = (total_food_eaten_by_dog/ total_food_eaten) * 100
cat_eaten_food_percentage = (total_food_eaten_by_cat/ total_food_eaten) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_eaten_food_percentage:.2f}% of the food has been eaten.")
print(f"{dog_eaten_food_percentage:.2f}% eaten from the dog.")
print(f"{cat_eaten_food_percentage:.2f}% eaten from the cat.")
