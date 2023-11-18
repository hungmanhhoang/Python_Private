def find_largest_subset(input_set, num):
    sorted_set = sorted(input_set, reverse=False)
    largest_subset = set()
    current_sum = 0

    for element in sorted_set:
        if current_sum + element <= num:
            largest_subset.add(element)
            current_sum += element

    return largest_subset

n = int(input())
input_set = set(map(int, input().split()))
num = int(input())

print(find_largest_subset(input_set, num))