#problem 14
#olivia g 19/2/20
#this program will convert seconds to minutes and seconds


SEC_MIN = 60


sec =  int(input("How many seconds? "))

minutes = sec // 60
print(minutes)
extra_sec = sec % 60
print(extra_sec)
