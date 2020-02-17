#problem 11
#olivia g 18/2/20
#this program will split choclate bars between people


SQUARE = 7

bars = int(input("How many chocolate bars do you have? "))
people = int(input("How many people are there to share amongst? "))

whole_bar = bars // people
print(whole_bar)

extra = bars % people
print(extra)

extra_squares = extra * SQUARE
print(extra_squares)

squares_each = extra_squares // people
print(squares_each)

leftover = extra_squares % people
print(leftover)
