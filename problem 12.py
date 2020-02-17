#problem 12
#olivia g 18/2/20
#this program will calculate the number of buses needed and how many kids on average can fit per bus
import math

cap = int(input("How many passengers can each bus take? "))
kid = int(input("How many chidlren are going on the trip? "))


bus = math.ceil(kid / cap)
avg_kid = kid / bus


print("--------------------")
print("Capacity: {} passengers".format(cap))
print("Number of children: {}".format(kid))
print("Buses needed: {}".format(bus))
print("Average children per bus: {:.2f}".format(avg_kid))
