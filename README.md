# Tic-Tac-Toe játék

Ez a Python kód egy egyszerű Tic-Tac-Toe (Amőba) játékot valósít meg, ahol a játékosnak és az ellenfélnek (egyszerű MI) kell váltakozva elhelyeznie a saját karakterét a táblán. A játék célja az, hogy valaki kitöltse a játéktér egy sorát, oszlopát vagy átlóját a saját karakterével.

## Használat

1. Indítsd el a programot, és add meg a játékos és a számítógép karaktereit.
2. Válaszd ki, hogy hova szeretnél lépni, a sor és oszlop számának megadásával (1-től 3-ig).
3. A számítógép elvégzi a saját lépését, majd a program megjeleníti a frissített táblát.
4. A játék addig folytatódik, amíg valaki nyer, vagy a tábla teljesen megtelik.

## Függvények

1. `make_move(board, row_index, column_index, char)`: Meghatározza, hogy a megadott lépés lehetséges-e, és végrehajtja azt.

2. `players_move(board, players_char)`: A játékos lépését kéri be és hajtja végre.

3. `bots_move(board, bots_char, players_char)`: A számítógép lépését végzi el. Először támad, majd védekezik, és ha szükséges, véletlenszerű lépést tesz.

4. `check_winner(board, players_char, bots_char)`: Ellenőrzi, hogy van-e győztes a játékban, vagy döntetlen állapotban van-e.

5. `display_board(board)`: Kirajzolja a játéktáblát a konzolra.

6. `main()`: A játék fő függvénye, ahol inicializálódik a tábla, és a játék menete zajlik.

## Példa használat

```bash
Add meg a karaktered!
-> X
Add meg az ellenfeled karakterét!
-> O
Hova szeretnél lépni? (sor, oszlop)
-> 2,2
