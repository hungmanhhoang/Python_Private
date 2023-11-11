while True:
    n = int(input())
    lst = list(map(int, input().split()))
    if n != len(lst):
        print("Invalid input")
    else:
        break

liked_numbers = ['1', '3', '7', '5', '9']
res = list(filter(lambda x: str(x)[-1] in liked_numbers, lst))
print(len(res))
print(res)