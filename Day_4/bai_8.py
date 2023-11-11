import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def right_input(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Vui lòng nhập một số nguyên dương.")

def play_game():
    highest_point = 0
    winner = None
    highest_round_win = []

    while True:
        n = right_input("Nhập số nguyên dương n: ")
        k = right_input("Nhập số nguyên dương k (0 < k < n): ")
        current_point = 0
        round_win = []

        while n > 0:
            print(f"\nTurn của người chơi (n={n}):")
            choice = right_input(f"Nhập một số từ 1 đến {min(n, k)}: ")

            if choice < 1 or choice > min(n, k):
                print("Người chơi đã phạm luật!")
                current_point += 1
            else:
                n -= choice
                round_win.append(choice)

        print("\nRound kết thúc!")
        print("Người chơi thắng: ", round_win)
        print("Số điểm phạm luật: ", current_point)

        if current_point < highest_point or winner is None:
            highest_point = current_point
            winner = highest_round_win
        elif current_point == highest_point:
            if len(round_win) > len(highest_round_win):
                winner = highest_round_win
            elif len(round_win) == len(highest_round_win):
                print("\nHai người chơi hoà!")
                break
            else:
                winner = round_win

        highest_round_win = round_win
        tiep_tuc = input("Tiếp tục chơi? (YES/NO): ").upper()

        if tiep_tuc != 'YES':
            break
        else:
            clear_screen()

    print("\nTrò chơi kết thúc!")
    print("Người chơi thắng cuộc: ", winner)

if __name__ == "__main__":
    play_game()
