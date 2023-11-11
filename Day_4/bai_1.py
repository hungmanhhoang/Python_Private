from datetime import datetime

while True:
    string = input()
    d, m , y = list(map(int, string.split('/')))
    if 1 <= d <= 31:
        break
    if 1 <= m <= 12:
        break
    if y >= 1000:
        break

    print("Invalid input")

time = datetime.strptime(string,r"%d/%m/%Y")
last_day_of_the_year = datetime(y, 12, 31)

days_remain = last_day_of_the_year - time

print(days_remain.days)