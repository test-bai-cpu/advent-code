lines = open("input").read().split("\n")
pairs = [(int(lines[i * 18 + 5][6:]), int(lines[i * 18 + 15][6:])) for i in range(14)]
print(pairs)
stack = []
links = {}
for i, (a, b) in enumerate(pairs):
    if a > 0:
        stack.append((i, b))
    else:
        j, bj = stack.pop()
        links[i] = (j, bj + a)
        print(links)

minimize = True
assignments = {}
for i, (j, delta) in links.items():
    print(i, (j, delta))
    assignments[i] = max(1, 1 + delta) if True else min(9, 9 + delta)
    assignments[j] = max(1, 1 - delta) if True else min(9, 9 - delta)
    print(assignments)

print(assignments)
print("".join(str(assignments[x]) for x in range(14)))