n = int(input())
array = list(map(int, input().split()))
x = int(input())
res = []
for i in range(x):
    res.append(sum(array[:int(input())+1]))

print()
print(*res, sep='\n')