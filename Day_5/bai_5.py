def couple_equal_11(my_set):  
    res = []
    my_set = list(my_set)
    
    for i in range(0, len(my_set)- 1):
        for j in range(i+1, len(my_set)):
            if my_set[i] + my_set[j] == 11:
                res.append((my_set[i], my_set[j]))
                
    return tuple(res)
         
my_set = set(map(int, input().split())) 

if 11 not in my_set:
    my_set.add(11)

for i in my_set:
    print(i)
    
res = couple_equal_11(my_set)
print(res)
print(f"Tổng số cặp phần tử trong my_set có tổng bằng 11 là: {len(res) * 11}")