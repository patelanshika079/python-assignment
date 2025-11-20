"""
Ques:- Write a program that converts and prints user given measurement in inches into
1. foot(12 inches)
2. yard(36 inches)
3. centimetres(2.54 inches)
4. meter(39.37 inches) """

inches = float(input("Enter measurement in inches: "))

foot = inches / 12             # 1 foot = 12 inches
yard = inches / 36             # 1 yard = 36 inches
centimetres = inches * 2.54    # 1 inch = 2.54 cm
meters = inches / 39.37        # 1 meter = 39.37 inches

print(f"{inches} inches is equal to:")
print(f"{foot} foot")
print(f"{yard} yard")
print(f"{centimetres} cm")
print(f"{meters} meter")
