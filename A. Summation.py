n = int(input())
num = map(int, input().split())
sum = 0
for i in num:
    sum = sum + i      
print(abs(sum))       