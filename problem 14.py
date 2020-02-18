#problem 14
#olivia g 19/2/20
#this program will convert seconds to minutes and seconds


SEC_MIN = 60


sec =  int(input("How many seconds? "))

minutes = sec // SEC_MIN
#print(minutes)
extra_sec = sec % SEC_MIN
#print(extra_sec)


print("-------------------")
print("{} seconds is {} minutes and {} seconds".format(sec, minutes, extra_sec))
