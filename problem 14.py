#problem 14
#olivia g 19/2/20
#this program will convert seconds to minutes and seconds

#constant - seconds in a minute
SEC_MIN = 60

#getting input - seconds
sec =  int(input("How many seconds? "))

#process - converting it to minutes and seconds
minutes = sec // SEC_MIN
extra_sec = sec % SEC_MIN

#output - formatted
print("-------------------")
print("{} seconds is {} minutes and {} seconds".format(sec, minutes, extra_sec))
