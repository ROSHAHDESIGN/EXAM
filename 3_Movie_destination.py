#vhod
budget_movie = float(input())
destination = input()
season = input()
days_quantity = int(input())
discount = 1
movie_day_price = 0
#IF / ELIF
if season == "Winter":
    if destination == "Dubai":
        movie_day_price = 45000
    elif destination == "Sofia":
        movie_day_price = 17000
    elif destination == "London":
        movie_day_price = 24000
elif season == "Summer":
    if destination == "Dubai":
        movie_day_price = 40000
    elif destination == "Sofia":
        movie_day_price = 12500
    elif destination == "London":
        movie_day_price = 20250

#Ако дестинацията е Дубай – 30% отстъпка от крайната цена
if destination == "Dubai":
    discount = 0.7

# Ако дестинацията е София – цената се оскъпява с 25%
if destination == "Sofia":
    discount = 1.25

movie_cost = movie_day_price * days_quantity * discount

if budget_movie >= movie_cost:
    print(f"The budget for the movie is enough! We have {(budget_movie - movie_cost):.2f} leva left!")
else:
    print(f"The director needs {(movie_cost-budget_movie):.2f} leva more!")
