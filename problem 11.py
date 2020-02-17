#problem 11
#olivia g 18/2/20
#this program will split choclate bars between people

#setting constant - how many squares per bar
SQUARE = 7
#getting input - bars and people
bars = int(input("How many chocolate bars do you have? "))
people = int(input("How many people are there to share amongst? "))

#process - calculating how much each person gets and what is left over
whole_bar = bars // people
#print(whole_bar)
extra = bars % people
#print(extra)
extra_squares = extra * SQUARE
#print(extra_squares)
squares_each = extra_squares // people
#print(squares_each)
leftover = extra_squares % people
#print(leftover)

#output - the parts of the calculation that are relevant to what the user wants to know
print("---------------------")
print("Number of chocolate bars: {}".format(bars))
print("Number of people: {}".format(people))
print("Whole choclate  bars each: {}".format(whole_bar))
print("Extra squares each: {}".format(squares_each))
print("Squares left over: {}".format(leftover))
