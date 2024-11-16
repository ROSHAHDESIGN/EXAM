#vhod
budget = float(input())
number_days = int(input())
price_per_day = float(input())
percentage_addit_costs = int(input()) # /100

#IF нощувките е по-голям от 7, цената за нощувка се намаля с 5%.
if number_days > 7:
    price_per_day = price_per_day - (price_per_day * 0.05)

trip_cost = (price_per_day * number_days) + ((percentage_addit_costs * budget)/100)

if budget >= trip_cost:
    print(f"Ivanovi will be left with {(budget - trip_cost):.2f} leva after vacation.")
else:
    print(f"{(trip_cost - budget):.2f} leva needed.")
    