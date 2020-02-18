#problem 13
#olivia g 18/2/20
#this program will sort out netball teams for kids who want to play


TEAM_NUM = 9

kid = int(input("How many children want to play netball? "))

teams = kid // TEAM_NUM
print(teams)
leftover = kid % TEAM_NUM
print(leftover)
