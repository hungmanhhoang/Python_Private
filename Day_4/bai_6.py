from itertools import groupby

def nhom_gia_tri_giong_nhau(lst):
    lst.sort()

    grouped_values = [list(group) for key, group in groupby(lst)]

    return grouped_values

my_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
res = nhom_gia_tri_giong_nhau(my_list)

print(res)
