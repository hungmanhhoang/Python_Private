def MyMultiple(*args):
    '''
    Calculate multiple of numbers
    '''
    result = 1
    for i in args:
        result *= i
    return result

print(MyMultiple(1,2,3,4,5,6,7,8,9,10))
print(MyMultiple(5, 5, 5))