championLOL = ["Yasuo", "Lee Sin", "Zed", "Master Yi", "Garen",
               "Tryndamere"]
dataLOL = [
    {"price": 6300, "Ulti": "Trăn trối"},
    {"price": 4800, "Ulti": "Nộ Long Cước"},
    {"price": 4800, "Ulti": "Dấu Ấn Tử Thần"},
    {"price": 450, "Ulti": "Chiến Binh Sơn Cước"},
    {"price": 450, "Ulti": "Công Lý Demacia"},
    {"price": 1350, "Ulti": "Từ Chối Tử Thần"}
]


name_champ = input().title()

print('\n\n')
if name_champ in championLOL:
    index = championLOL.index(name_champ)
    data = dataLOL[index]
    get_price = data['price']
    print(get_price)
else:
    print("No champ in the list")
print('\n\n')