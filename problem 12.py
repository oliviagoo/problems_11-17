#problem 12
#olivia g 18/2/20
#this program will calculate the number of buses needed and how many kids on average can fit per bus
import math

cap = int(input("How many passengers can each bus take? "))
kid = int(input("How many chidlren are going on the trip? "))


bus_float = kid / cap
print(bus_float)

bus_int = math.ceil(bus_float)
print(bus_int)

avg_kid = kid / bus_int
print(avg_kid)
