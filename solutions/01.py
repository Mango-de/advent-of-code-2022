with open('inputs/01') as f:
    l = [*map(sum, (map(int, x.splitlines()) for x in f.read().split('\n\n')))]

# Part 1

print(max(l))

# Part 2

top = [0] * 3

for s in l:
    for i in range(3):
        if s > top[i]:
            while i > 0:
                top[i] = top[i - 1]
                i -= 1
            top[i] = s
            break

print(sum(top))
