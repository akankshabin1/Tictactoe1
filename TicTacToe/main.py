def sum(a, b, c):
    return a + b + c
def printBG(xPosition, zPosition):
    zero = 'X' if xPosition[0] else ('O' if zPosition[0] else 0)
    one = 'X' if xPosition[1] else ('O' if zPosition[1] else 1)
    two = 'X' if xPosition[2] else ('O' if zPosition[2] else 2)
    three = 'X' if xPosition[3] else ('O' if zPosition[3] else 3)
    four = 'X' if xPosition[4] else ('O' if zPosition[4] else 4)
    five = 'X' if xPosition[5] else ('O' if zPosition[5] else 5)
    six = 'X' if xPosition[6] else ('O' if zPosition[6] else 6)
    seven = 'X' if xPosition[7] else ('O' if zPosition[7] else 7)
    eight = 'X' if xPosition[8] else ('O' if zPosition[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
def checkWinner(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1
if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("   Welcome to Tic Tac Toe   ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    used_values = []  # List to keep track of used values
    while True:
        printBG(xState, zState)
        if turn == 1:
            value = int(input("X's Chance - Please enter a value: "))
            print("\n")
            if value in used_values:
                print("Value already used. Please choose another value.")
                continue
            xState[value] = 1
            used_values.append(value)  # Add the used value to the list
        else:
            value = int(input("O's Chance - Please enter a value: "))
            print("\n")
            if value in used_values:
                print("Value already used. Please choose another value.\n")
                continue
            zState[value] = 1
            used_values.append(value)  # Add the used value to the list
        cwin = checkWinner(xState, zState)
        if cwin != -1:
            print("Match over")
            break
        turn = 1 - turn