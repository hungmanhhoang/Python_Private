def flatten(lst):
    flat_list = []
    for element in lst:
        if isinstance(element, list):
            flat_list.extend(element)
        else:
            flat_list.append(element)
    return flat_list

# Example usage:
nested_list = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flattened_list = flatten(nested_list)

print(flattened_list)
