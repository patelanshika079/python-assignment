amount = int(input())
start = int(input())

Money = [100, 50, 20, 10, 5, 2, 1]
idx = Money.index(start)
use_Money = Money[idx:]

for d in use_Money:
    match d:
        case 100:
            notes = amount // 100
        case 50:
            notes = amount // 50
        case 20:
            notes = amount // 20
        case 10:
            notes = amount // 10
        case 5:
            notes = amount // 5
        case 2:
            notes = amount // 2
        case 1:
            notes = amount // 1

    print(f"{d} rupees note: {notes}")
    amount = amount % d
