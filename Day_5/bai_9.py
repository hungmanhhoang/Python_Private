import random


def generate_account_auto(num_account):

    account_name = [str(i)
                    for i in range(202160000, 202160000+num_account)]

    accounts = {}

    for i, j in zip(range(num_account), account_name):
        accounts.update(
            {
                f"Account{i+1}": {
                    "Username": j,
                    "Password": random.choice(["CNTT", "KHMT", "KTPM", "HTTT"]) + j
                }
            }
        )
    return accounts


def generate_account_manual(num_account):

    accounts = {}
    for i in range(num_account):

        # Input account_name
        while 1:
            account_name = input("Nhập Username: ")
            if len(account_name) != 10:
                print("Invalid input")
            else:
                break

        # Update account
        accounts.update(
            {
                f"Account{i+1}": {
                    "Username": account_name,
                    "Password": random.choice(["CNTT", "KHMT", "KTPM", "HTTT"]) + account_name
                }
            }
        )
    return accounts


number_accounts = int(input("Nhập số lượng Account: "))

accounts = generate_account_auto(number_accounts)

print('\n\n')
for i, j in accounts.items():
    print(i, ":", j)
print('\n\n')
