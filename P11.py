N = int(input())

for _ in range(N):
    SH, SM, EH, EM = map(int, input().split())
   
    minutes = EM - SM
    hours = EH - SH

    if minutes < 0:
        minutes += 60
        hours -= 1

    print(hours, minutes)