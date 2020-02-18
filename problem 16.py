#problem 16
#olivia g 19/2/20
#this program will calculate how many apples the user can buy


CHOC_PRICE = 2.5
APP_PRICE = 0.5


balance = float(input("How much money do you have? $"))
num_choc = int(input("How many chocolate bars do you want to buy? "))

app_money = balance - num_choc * CHOC_PRICE
choc_money = balance = app_money
apples = app_money // APP_PRICE 



print("-------------")
print("Total money: ${:.2f}".format(balance))
print("Money to buy chocolate bars: ${:.2f}".format(choc_money))
print("Chocolate bars bought: {}".format(num_choc))
print("Money to buy apples: ${:.2f}".format(app_money))
print("Apples bought: {:.0f}".format(apples))
