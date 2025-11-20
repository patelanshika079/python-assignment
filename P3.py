"""
Ques:- John is trying to solve the arithmetic series(AP). He wants to find two things in the series
1. He wants to find nth terms in the series
2. He wants to find the sum up to the nth term.   """

a = 2  # first term of the series
d = 2  # common difference
n = 5  # nth term 

nth_term = a + (n - 1) * d
print("Nth term of AP is:", nth_term)

sum_n = (n / 2) * (a + nth_term)
print("Sum of first n terms is:", sum_n)

