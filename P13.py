N = int(input())
stones = N
i = 1

while stones > 0:
    stones -= i
    if stones <= 0:
        print("Ramesh")
        break

    stones -= 2 * i
    if stones <= 0:
        print("Suresh")
        break

    i += 1