import math

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
   
    gcd_value = math.gcd(x, y)
    lcm_value = (x * y) // gcd_value
   
    print(gcd_value, lcm_value)