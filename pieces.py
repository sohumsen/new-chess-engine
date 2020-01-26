from utils import algebra_to_cartesian, cartesian_to_algebra
from exceptions import InvalidMoveException
from pos import Pos
import copy

######

# TODO print Fail to replace with Exception. Take Screenshot
# TODO allMoves should return a list of Pos Objects


class Piece:
    def __init__(self, name, posobj, board=None):
        self.name = name or "white_pawna"
        if self.name.find("white") == -1:
            self.color = "black"
        else:
            self.color = "white"

        self.board = board

        self.currpos = posobj #or Pos((4, 4))
        self.newpos = posobj #or Pos((4, 4))
        self.img = None

    def move_piece(self, newPosObj):

        self.newpos = newPosObj

        valid_move = self.validate_move()
        if valid_move == True:  # and no piece there
            self.updateBoardAndPiece()
            return True
        else:
            print("Invalid Move")
            return False
            # raise InvalidMoveException("Invalid Move %s", str(valid_move))

    def updateBoardAndPiece(self):
        """ works for any piece """

        self.board.update(self, self.newpos)
        self.currpos = self.newpos

    def getMovements(self):
        """ returns the old and new positions"""

        return self.currpos, self.newpos


class Pawn(Piece):
    # TODO add a init method that calls the superclass ctor and keeps its own data
    # TODO add how to kill a pawn diagonally
    def __init__(self, name, posobj, board=None):
        super().__init__(name, posobj, board)
        self.points = 1
        if "black" in self.name:
            self.img = "♙"
        else:
            self.img = "♟"

    def move_piece(self, newPosObj):
        self.newpos = newPosObj

        valid_move = False
        # valid_move_dist = {"white": 1, "black": -1}
        # print(i1, i2)
        obj, objname = self.board.piece_from_algebraic_coord(newPosObj.algebraic())

        # Normal Movements
        if self.currpos.x == self.newpos.x:
            if not obj:
                if self.color == "white":

                    if self.currpos.y == 6:
                        if self.currpos.samecolumn(
                            "U", self.newpos, 2
                        ) or self.currpos.samecolumn("U", self.newpos, 1):
                            valid_move = True
                    else:
                        if self.currpos.samecolumn("U", self.newpos, 1):
                            valid_move = True

                elif self.color == "black":
                    if self.currpos.y == 1:
                        if self.currpos.samecolumn(
                            "U", self.newpos, -2
                        ) or self.currpos.samecolumn("U", self.newpos, -1):
                            valid_move = True
                    else:
                        if self.currpos.samecolumn("U", self.newpos, -1):
                            valid_move = True

        # kill another pawn
        else:
            # theres a piece from a diff color
            if obj and self.color != obj.color:
                if self.color == "white" and self.newpos.y + 1 == self.currpos.y:
                    if (self.currpos.x + 1 == self.newpos.x) or (
                        self.currpos.x - 1 == self.newpos.x
                    ):
                        valid_move = True
                elif self.color == "black" and self.newpos.y - 1 == self.currpos.y:
                    if (self.currpos.x + 1 == self.newpos.x) or (
                        self.currpos.x - 1 == self.newpos.x
                    ):
                        valid_move = True

        if valid_move == True:
            # and no piece there
            self.updateBoardAndPiece()
            return True
        else:

            print("FAIL")
            return False

    """         
        def validate_move(self):
        
            pos = copy.deepcopy(self.currpos)
            allmoves = []
            print(pos)
            print(self.currpos)
            for way in pos.knight_moves.keys():
                # lst =
                allmoves.extend(pos.knight_hops(way))

            print(allmoves)
            for tup in allmoves:
                if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                    return True

            return False
        """


# questions


class Knight(Piece):
    def __init__(self, name, posobj, board=None):
        # it used to have Board
        super().__init__(name, posobj, board)
        self.points = 3
        # print(self.name)

        if "black" in name:

            self.img = "♘"
        else:
            self.img = "♞"

    def validate_move(self):

        pos = copy.deepcopy(self.currpos)
        allmoves = []
        print(pos)
        print(self.currpos)
        for way in pos.knight_moves.keys():
            # lst =
            allmoves.extend(pos.knight_hops(way,self))

        print(allmoves)
        for tup in allmoves:
            if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                return True

        return False


class Bishop(Piece):
    def __init__(self, name, posobj, board=None):
        super().__init__(name, posobj, board)
        self.points = 3
        if "black" in self.name:

            self.img = "♗"
        else:
            self.img = "♝"

    def validate_move(self):

        pos = copy.deepcopy(self.currpos)
        print(pos)
        allmoves = []
        # gets all the pathways of the possible moves

        for way in pos.diag_moves.keys():
            allmoves.extend(pos.diag(way, 7, self, self.board))
            print(way, pos, allmoves)

        for tup in allmoves:
            if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                return True

        return False


class Rook(Piece):
    def __init__(self, name, posobj, board=None):
        super().__init__(name, posobj, board)
        self.points = 5
        if "black" in self.name:

            self.img = "♖"
        else:
            self.img = "♜"

    def validate_move(self):

        pos = copy.deepcopy(self.currpos)
        allmoves = []
        # gets all the pathways of the possible moves

        for way in pos.slide_moves.keys():
            allmoves.extend(pos.slide(way, 7, self))
        print(pos, allmoves)

        for tup in allmoves:

            if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                # the move is legal
                # print(tup)
                # print(pos.y - self.newpos.y)
                # for space in range(self.newpos.y, pos.y):
                #   print("saaaa" + str(space))
                #  coordObj = Pos(str(pos.x) + str(space))
                # if self.board.piece_from_algebraic_coord(coordObj):
                #    print(coordObj)

                return True
                # is there a piece in the way
                # for move in range(pos.x- self.newpos.):
                #   pass
                break
        return False

    def is_piece_in_the_way(self, i1, j1, i2, j2):

        # self.newpos = goto_cartesian_coord
        # i1, j1, i2, j2 = self.getMovements()

        # valid_move = False
        print(self.pos)
        print(self.move.current())
        self.move.left(2)
        print(self.move.diag("left", "up", 2))
        """
        allpos = self.allplaces(i1, j1, i2, j2)
        for p in allpos:
            obj, _ = self.board.piece_from_algebraic_coord([p.x, p.y])
            if obj:
                valid_move = False
                break
            valid_move = True
        """
        """
        if i1 - i2 == j1 - j2:
            print("loop1")

            for z in range(1, (i1 - i2 + 1)):

                obj, _ = self.board.piece_from_algebraic_coord([i1 - z, j1 - z])

                if obj is None:
                    valid_move = True
                    break

        if -i1 + i2 == j1 - j2:
            print("loop2")

            for z in range(0, (abs(i2 - i1) + 1)):

                obj = self.board.piece_from_algebraic_coord([i1 + z, j1 - z])
                print(obj)
                print(i1 + z, j1 - z)
                if type(obj) == str:
                    valid_move = True
                    break
                    # theres nothing there

        print(valid_move)
        """
        # return valid_move


class Queen(Piece):
    def __init__(self, name, posobj, board=None):
        super().__init__(name, posobj, board)
        self.points = 9
        if "black" in self.name:

            self.img = "♕"
        else:
            self.img = "♛"

    def validate_move(self):

        pos = copy.deepcopy(self.currpos)
        allmoves = []
        # gets all the pathways of the possible moves

        for way in pos.slide_moves.keys():
            allmoves.extend(pos.slide(way, 7, self))
            print(way, pos, allmoves)

        for way in pos.diag_moves.keys():
            allmoves.extend(pos.diag(way, 7, self))
            print(way, pos, allmoves)

        for tup in allmoves:
            if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                return True

        return False


class King(Piece):
    def __init__(self, name, posobj, board=None):
        super().__init__(name, posobj, board)
        self.points = 100
        if "black" in self.name:

            self.img = "♔"
        else:
            self.img = "♚"

    def validate_move(self):

        pos = copy.deepcopy(self.currpos)
        print(pos)
        allmoves = []
        castle=[]
        # gets all the pathways of the possible moves

        for way in pos.slide_moves.keys():
            allmoves.extend(pos.slide(way, 1, self))
            print(way, pos, allmoves)

        for way in pos.diag_moves.keys():
            allmoves.extend(pos.diag(way, 1, self))
            print(way, pos, allmoves)
        
        if self.color=="white" and self.currpos.current==[4, 7]:
            obj1,objname1=self.board.piece_from_algebraic_coord("h1")
            obj2,objname2=self.board.piece_from_algebraic_coord("a1")
            if objname1=="white rook h":
                allmoves.extend(pos.diag("R", 3, self))
                    #there is a path

            if objname2=="white rook a":
            # if obj
                allmoves.extend(pos.diag("L", 4, self))

        for tup in allmoves:
            if self.newpos.x == tup[0] and self.newpos.y == tup[1]:
                return True

        return False


def test():
    p = Pawn()


if __name__ == "__main__":

    def f2():
        kn = Knight("ddd", 3, "", algebra_to_cartesian("b8"), None)

        for i in range(0, 7):
            for j in range(0, 7):
                kn.newpos.x = i
                kn.newpos.y = j
                kn.validate_move()

        return

    # f2()
    """

    import timeit

    # t = timeit.Timer(f2)  # outside the try/except
    try:

        print(timeit.timeit(stmt=f2, number=10000))  # or t.repeat(...)

    except Exception as e:
        print(e)
    # class King(Queen) --- perhaps with n=1
    """

