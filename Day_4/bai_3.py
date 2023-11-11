import re

def tinh_tong_chuoi(chuoi):
    cac_so = re.findall(r'-?\d+', chuoi)  
    tong = sum(map(int, cac_so))  

    return tong


chuoi_test = "chitu21anh34kdf-234"
ket_qua = tinh_tong_chuoi(chuoi_test)
print("Tổng các số trong chuỗi là:", ket_qua)
