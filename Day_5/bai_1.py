def sinhVienDangKy2Ban(ban_1:set, ban_2:set)->set:
    students = ban_1 & ban_2
    if students is not None:
        print("Có sinh viên đăng ký học tại cả hai bàn")
        return students
    else:
        print("Không có sinh viên nào đăng ký học tại cả hai bàn")
        return None

def sinhVienDangKy1Ban(ban_1:set, ban_2:set)->set:
    return ban_1 ^ ban_2

def sinhVienDangKyBan1Khong2(ban_1:set, ban_2:set)->set:
    return ban_1 - ban_2

# Nhập 2 bàn 
ban_1 = {input(f"Nhập MSV của bàn 1 thứ {i + 1}: ") for i in range(int(input("Nhập số lượng sinh viên của bàn 1: ")))}
ban_2 = {input(f"Nhập MSV của bàn 2 thứ {i + 1}: ") for i in range(int(input("Nhập số lượng sinh viên của bàn 2: ")))}

# In ra các MSV của 2 bàn
print(f"Sinh viên đăng ký học cả hai bàn là: {sinhVienDangKy2Ban(ban_1, ban_2)}")
print(f"Sinh viên đăng ký học 1 bàn duy nhất là: {sinhVienDangKy1Ban(ban_1, ban_2)}")
print(f"Sinh viên đăng ký bàn 1 không đăng ký bàn 2 là: {sinhVienDangKyBan1Khong2(ban_1, ban_2)}")