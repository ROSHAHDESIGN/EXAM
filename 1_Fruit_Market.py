#vhodni danni

strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price * 0.50 #polovinata ot cena
oranges_price = raspberries_price * 0.60 #cena s 40% po niska ot gornata
bananas_price = raspberries_price * 0.20 #cena s 80% po niska ot gornata

total_amount = ((strawberries_price * strawberries_quantity) +
                ( raspberries_price * raspberries_quantity) +
                (oranges_price * oranges_quantity) +
                (bananas_price * bananas_quantity))
print(total_amount)


