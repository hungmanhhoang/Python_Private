def Tranposition(matrix):
    '''
    Transposition of a matrix
    '''
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

# *Tranposition(matrix) is a way to unpack the list of lists then use sep='\n' to print each list in a new line    
print(*Tranposition(matrix), sep='\n')