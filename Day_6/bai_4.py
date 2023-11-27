import math

def get_points(filename):
    '''Get points from file'''
    with open(filename, 'r') as f:
        data = f.read().split()
        pointA = (float(data[1]), float(data[2]))
        pointB = (float(data[4]), float(data[5]))
    return pointA, pointB

def calculate_distance(point1, point2):
    '''Calculate distance between two points'''
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def output(pointA, pointB, filename='output.txt'):
    '''Output to file'''
    distance = calculate_distance(pointA, pointB)
    with open(filename, 'w') as f:
        f.write(f"A({pointA[0]}, {pointA[1]}) B({pointB[0]}, {pointB[1]}) AB = {round(distance, 2)}")

pointA, pointB = get_points('input.txt')
output(pointA, pointB)
