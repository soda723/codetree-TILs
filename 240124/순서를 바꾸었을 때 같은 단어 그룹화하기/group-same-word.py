n = int(input())
words = []
for _ in range(n):
    words.append(''.join(sorted(input())))

count = {}
for w in words:
    if w in count: count[w] += 1
    else: count[w] = 1

print(max(count.values()))