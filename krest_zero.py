def con():      # output of the playing field
    for row in sell:
        print(*row)


# creating a field
sell = []
count = 1
count_2 = 1
for i in range(4):
    sell.append(['.'] * 4)
for i in range(4):
    for j in range(4):
        if i == j == 0:
            sell[i][j] = " "
        elif j == 0:
            sell[i][j] = count
            count += 1
        elif i == 0:
            sell[i][j] = count_2
            count_2 += 1


def enter_pl1():    # the first player's move
    a = int(input("Player 1: enter the horizontal value, please (1, 2, 3) "))
    b = int(input("Player 1: enter the vertical value, please (1, 2, 3) "))
    sell[a][b] = 'x'


def enter_pl2():    # the second player's move
    d = int(input("Player 2: enter the horizontal value, please (1, 2, 3) "))
    c = int(input("Player 2: enter the vertical value, please (1, 2, 3) "))
    sell[d][c] = 'o'


con()

enter_pl1(), con()
enter_pl2(), con()

count_w = 0
pl_1 = 0
pl_11 = 0
pl_2 = 0
pl_21 = 0

while count_w <= 2:
    enter_pl1(), con()
    for i in range(1, 4):
        pl_1 = 0
        for j in range(1, 4):
            if sell[i][j] == 'x':
                pl_1 += 1
        if pl_1 == 3:
            break
    for j in range(1, 4):
        pl_11 = 0
        for i in range(1, 4):
            if sell[i][j] == 'x':
                pl_11 += 1
        if pl_11 == 3:
            break

    if pl_1 == 3 or pl_11 == 3:
        print("Won Player1")
        break
    elif sell[1][1] == sell[2][2] == sell[3][3] == "x":
        print("Won Player1")
        break
    elif sell[1][3] == sell[2][2] == sell[3][1] == "x":
        print("Won Player1")
        break

    enter_pl2(), con()
    for i in range(1, 4):
        pl_2 = 0
        for j in range(1, 4):
            if sell[i][j] == 'o':
                pl_2 += 1
        if pl_2 == 3:
            break
    for j in range(1, 4):
        pl_21 = 0
        for i in range(1, 4):
            if sell[i][j] == 'o':
                pl_21 += 1
        if pl_21 == 3:
            break

    if pl_2 == 3 or pl_21 == 3:
        print("Won Player2")
        break
    elif sell[1][1] == sell[2][2] == sell[3][3] == "o":
        print("Won Player2")
        break
    elif sell[1][3] == sell[2][2] == sell[3][1] == "o":
        print("Won Player2")
        break
    count_w += 1
if count_w == 3 and (pl_1 != 3 and pl_11 != 3 and pl_2 != 3 and pl_21 != 3):
    print("Draw")

