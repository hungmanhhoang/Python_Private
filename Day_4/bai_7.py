lst = 'a b c d e f'.split()
so_nhom = 3

res = []
for i in range(so_nhom):
    sub_res = lst[i::so_nhom]
    res.append(sub_res)

print(res)
