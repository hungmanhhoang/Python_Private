while True:
    n = int(input())
    lst = list(map(int, input().split()))
    if n != len(lst):
        print("Invalid input")
    else:
        break

odd = sum(filter(lambda x: x% 2 != 0, lst))
even = sum(filter(lambda x: x% 2 == 0, lst))

if odd > even:
    print('odd')
else:
    print('even')