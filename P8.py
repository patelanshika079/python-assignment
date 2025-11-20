def last_digit(a, b):
    cycle = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    last = a % 10              # only last digit matters
    seq = cycle[last]          # pick the cycle
    index = (b - 1) % len(seq) # find correct position in cycle
    return seq[index]

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print(last_digit(a, b))
