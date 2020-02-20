#Kim Schalk and Olivia Goodman
#20/02/2020
#Money Change Program

import math
NOTES_COINS = [20, 10, 5, 2, 1, 0.5, 0.2, 0.1]
amount_coins = []

balance = float(input("How much money do you have? $"))
purchase = float(input("What was the cost for the items that you purchased? $"))

change = balance - purchase

print("Purchase: ${:.2f}".format(purchase))
print("Change from ${:.2f}: ${:.2f}".format(balance, change))

for money in NOTES_COINS:
    if change < money:
        amount_coins.append(0)
    else:
        amount = change // money
        change -= money * amount
        amount_coins.append(amount)

print("$20 notes: {:.0f}".format(amount_coins[0]))
print("$10 notes: {:.0f}".format(amount_coins[1]))
print("$5 notes: {:.0f}".format(amount_coins[2]))
print("$2 coins: {:.0f}".format(amount_coins[3]))
print("$1 coins: {:.0f}".format(amount_coins[4]))
print("50c coins: {:.0f}".format(amount_coins[5]))
print("20c coins: {:.0f}".format(amount_coins[6]))
print("10c coins: {:.0f}".format(amount_coins[7]))

