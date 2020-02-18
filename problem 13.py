#problem 13
#olivia g 18/2/20
#this program will sort out netball teams for kids who want to play

#setting constant - how many kids per team
TEAM_NUM = 9

#getting input - how many children
kid = int(input("How many children want to play netball? "))

#process - calculating how many kids get in a team and how many teams are needed
teams = kid // TEAM_NUM
leftover = kid % TEAM_NUM

#output - the variables in context
print("------------------")
print("Number of children: {}".format(kid))
print("Number of teams: {}".format(teams))
print("Number of children left over: {}".format(leftover))
