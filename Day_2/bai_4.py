#%% Trả về số lượng các bits cần thiết để biểu diễn số a ở dạng nhị phân, không bao gồm phần dấu và các số 0 ở đầu.
a= 100032
binary_number = bin(a)[2:]
print(len(binary_number))


#%% Kiểm tra danh sách các thuộc tính và phương thức hiện tại của một biến có kiểu dữ liệu là number.
number = 543
attributes_and_methods = dir(number)

# In danh sách thuộc tính và phương thức
for item in attributes_and_methods:
    print(item)
