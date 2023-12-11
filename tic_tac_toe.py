from random import randint


# Meghatározza hogy a meglépni kívánt lépés lehetséges-e
def make_move(board, row_index, column_index, char):
    if board[row_index][column_index] == "?":
        board[row_index][column_index] = char
        return True
    return False


# A játékos lépését kéri be, és viszi azt végre, True értékkel tér vissza, ha megteheti a lépést, False-al ha nem
def players_move(board, players_char):
    move = input("Hova szeretnél lépni? (sor, oszlop)\n->").replace(",", " ").split()
    if make_move(board, int(move[0]) - 1, int(move[1]) - 1, players_char):
        return True


# Az ellenfél lépését teszi meg, elsősorban megvizsgálja, hogy van-e olyan lépés amivel megnyerheti a játékot.
# Elsőnek a sorokat ellenőrzi, másodjára az oszlopokat majd a bal, jobb átlókat vizsgálja meg.
# Ha nem talál ilyen lehetőséget megvizsgálja, hogy a játékosnak van-e nyerő lépése, majd ha talál megakadályozza.
# Hogyha ilyet se talál, Véletlenszerűen kiválaszt egy helyet, és ha az egy legális mozdulat, megteszi a lépést
def bots_move(board, bots_char, players_char):
    # ---TÁMADÁS---
    # SOR
    for row in range(3):
        if board[row].count(bots_char) == 2:
            for column in range(3):
                if make_move(board, row, column, bots_char):
                    return

    # OSZLOP
    for i, column in enumerate(zip(*board)):
        if column.count(players_char) == 2:
            for row in range(3):
                if column[row] == "?" and make_move(board, row, i, bots_char):
                    return

    # Bal átló
    if [board[x][x] for x in range(3)].count(bots_char) == 2:
        for i in range(3):
            if make_move(board, i, i, bots_char):
                return
    # Jobb átló
    if [board[x][-i] for i, x in enumerate(range(3), start=1)].count(bots_char) == 2:
        for i, x in enumerate(range(3), start=1):
            if make_move(board, x, -i, bots_char):
                return

    # ---VÉDEKEZÉS---
    # SOR
    for row in range(3):
        if board[row].count(players_char) == 2:
            for column in range(3):
                if make_move(board, row, column, bots_char):
                    return

    # OSZLOP

    for i, column in enumerate(zip(*board)):
        if column.count(players_char) == 2:
            for row in range(3):
                if column[row] == "?" and make_move(board, row, i, bots_char):
                    return

    # Bal átló
    if [board[x][x] for x in range(3)].count(players_char) == 2:
        for i in range(3):
            if make_move(board, i, i, bots_char):
                return
    # Jobb átló
    if [board[x][-i] for i, x in enumerate(range(3), start=1)].count(players_char) == 2:
        for i, x in enumerate(range(3), start=1):
            if make_move(board, x, -i, bots_char):
                return

    # Ha nincs esély arra, hogy megnyerje a játékot, vagy védekezzen, véletlenszerűen kezdeményez.
    while True:
        moves = [randint(0, 2), randint(0, 2)]
        if make_move(board, moves[0], moves[1], bots_char):
            return


# Azt vizsgálja, hogy a tábla megadott helyzetében, valami megnyerte-e a játékot / a két fél döntetlen-t játszott.
def check_winner(board, players_char, bots_char):
    # SOR
    for row in board:
        if row.count(row[0]) == 3 and row[0] == players_char:
            return [True, "Nyertél, kitöltöttél egy sort!"]
        elif row.count(row[0]) == 3 and row[0] == bots_char:
            return [True, "Vesztettél, az ellenfeled kitöltött egy sort!"]

    # OSZLOP
    for column in zip(*board):
        if column.count(players_char) == 3:
            return [True, "Nyertél, kitöltöttél egy oszlopot!"]
        if column.count(bots_char) == 3:
            return [True, "Vesztettél, az ellenfeled kitöltött egy oszlopot!"]

    # SRÉG
    if ([board[x][x] for x in range(3)].count(players_char) == 3 or
            [board[x][-i] for i, x in enumerate(range(3), start=1)].count(players_char) == 3):
        return [True, "Nyertél, kitöltöttél egy átlót!"]
    elif ([board[x][x] for x in range(3)].count(bots_char) == 3 or
          [board[x][-i] for i, x in enumerate(range(3), start=1)].count(bots_char) == 3):
        return [True, "Vesztettél, az ellenfeled kitöltött egy átlót!"]

    if sum([row.count("?") for row in board]) == 0:
        return [True, "Döntetlen!"]
    return [False, None]


# Kirajzolja a táblát a konzolra
def display_board(board):
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("-" * 9)


# Fő függvény. Itt zajlik le a játék, és jön létre a pálya
def main():
    board = [["?" for _ in range(3)] for _ in range(3)]

    player_char = input("Add meg a karaktered!\n->")
    bot_char = input("Add meg az ellenfeled karakterét!\n->")
    while player_char == bot_char:
        player_char = input("Add meg a karaktered!\n->")
        bot_char = input("Add meg az ellenfeled karakterét!\n->")

    while True:
        if players_move(board, player_char):
            winner = check_winner(board, player_char, bot_char)
            if winner[0]:
                print(winner[1])
                break

            bots_move(board, bot_char, player_char)
            display_board(board)
            winner = check_winner(board, player_char, bot_char)
            if winner[0]:
                print(winner[1])
                break


if __name__ == '__main__':
    main()
