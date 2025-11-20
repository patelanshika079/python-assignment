# Ques:- Given three numbers find the maximum of three numbers using the ternary operator.

a = 10
b = 25
c = 17

if a > b and a > c:
    max_num = a
elif b > c:
    max_num = b
else:
    max_num = c

print("Maximum number is:", max_num)
