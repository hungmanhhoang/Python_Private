def MyMultiple(args):
    '''
    Calculate multiple of numbers
    '''
    result = 1
    for i in args:
        result *= i
    return result

def gcd(a, b):
    '''Caclulate greatest common divisor of a and b'''
    while b != 0:
        a, b = b, a % b
    return a

def simplify(numerator, denominator):
    '''Simplify fraction'''
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def calculate(lst):
    '''Return the result of the calculation of the fractions in the list'''
    numerator = MyMultiple((lst[i][0] for i in range(len(lst))))
    denominator = MyMultiple((lst[i][1] for i in range(len(lst))))
    return simplify(numerator, denominator)

lst = [list(map(int,input().split())) for i in range(int(input()))]

print(*calculate(lst))