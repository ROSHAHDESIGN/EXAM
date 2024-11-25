start = input()
end = input()

start1, start2, start3, start4 = map(int, start)
end1, end2, end3, end4 = map(int, end)

for d1 in range(start1, end1 +1):
    if d1 % 2 == 0:
        continue
    for d2 in range(start2, end2 +1):
        if d2 % 2 == 0:
            continue
        for d3 in range(start3, end3 + 1):
            if d3 % 2 == 0:
                continue
            for d4 in range(start4, end4 +1):
                if d4 % 2 == 0:
                    continue
                print(f"{d1}{d2}{d3}{d4}", end=" ")

