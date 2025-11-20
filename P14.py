"""
Ques:- Davos wants to build a game and he wants to build a staircase in the game.
The staircase must be in the form of

#
##
###
####

Input
The first line is the value of N.

Output:
Number of levels that must be printed """

N = int(input("Enter a number:-"))

for i in range(1, N + 1):
    print("#" * i)
