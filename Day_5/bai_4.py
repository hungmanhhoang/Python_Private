A = [input(f"Nhập chuỗi {i+1}: ") for i in range(int(input("Nhập số lượng chuỗi: ")))]

B = tuple(A)
print(B)

num_string_number = tuple(filter(lambda x:  x.isnumeric(), A))    
print(f"Số lượng phần tử trong b có dạng số là: {len(num_string_number)}")
