from board import Board
from utils import algebra_to_cartesian
from pos import Pos

"""
TODO
Annotate everything
finish queen and king 
clean up any errors
do ai stuff
"""
# f=open("pastgames.txt", "w")


def move(color):
    valid_move = False
    while not valid_move:
        print("%s moves now: " % color.upper())
        curr_algebraic_coord = input("Enter the current piece location >")

        next_algebraic_coord = input("Enter the goto location >")

        if curr_algebraic_coord == "end" or next_algebraic_coord == "end":
            break

        pieceObj, _ = board.piece_from_algebraic_coord(curr_algebraic_coord)
        if pieceObj:  # there is a piece there
            if pieceObj.color == color:
                valid_move = pieceObj.move_piece(Pos(next_algebraic_coord))
                if valid_move:
                    f = open("pastgames.txt", "a")
                    f.write(
                        color.upper()
                        + " : "
                        + curr_algebraic_coord
                        + " "
                        + next_algebraic_coord
                        + " \n"
                    )
                    # f.write(" it went in the else")
                    f.close()

                if not valid_move:
                    print(
                        "Invalid move "
                        + curr_algebraic_coord
                        + " cannot move to "
                        + next_algebraic_coord
                    )

            else:
                print("%s moves " % color.upper())
        else:
            print("No object at that place")

        Board.printBoardOnScreen(board)


def move_any_piece():
    import datetime

    # datetime.datetime.now()
    f = open("pastgames.txt", "a")
    f.write(" \n" + str(datetime.datetime.now()) + " \n")
    f.close()
    while True:
        move("white")
        move("black")


def readfile():
    f = open("pastgames.txt", "r")
    print(f.read())
    f.close()


def main_menu():
    valid_choice = False
    while not valid_choice:
        choice = int(
            input("Enter a choice: \n 1) Player v Player \n 2) Review past games \n")
        )
        if choice == 1:
            valid_choice = True

            board.populate_board()
            board.printBoardOnScreen()
            board.printBoardOnPyGame()
            move_any_piece()
        elif choice == 2:
            valid_choice = True
            readfile()
        else:
            print("Enter a valid choice")
    # p v p
    # p vs ai
    # ai vs ai
    # review past games
    # daily puzzle
    pass


if __name__ == "__main__":
    board = Board()
    while True:

        main_menu()
