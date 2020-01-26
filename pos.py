from utils import algebra_to_cartesian, cartesian_to_algebra

# from board import Board

# TODO always return only pos objecte from this class
# Import the str to "a1(0|7)"


class Pos:
    knight_moves = {
        "LU": "self._lu(2,1)  ",
        "LD": "self._ld(2,1)",
        "RU": "self._ru(2,1)",
        "RD": "self._rd(2,1)",
        "UL": "self._lu(1,2)",
        "UR": "self._ru(1,2)",
        "DL": "self._ld(1,2)",
        "DR": "self._rd(1,2)",
    }

    diag_moves = {
        "LU": "self._lu(1,1)  ",
        "LD": "self._ld(1,1)",
        "RU": "self._ru(1,1)",
        "RD": "self._rd(1,1)",
    }
    slide_moves = {
        "L": "self.left(1)  ",
        "R": "self.right(1)",
        "U": "self.up(1)",
        "D": "self.down(1)",
    }

    def __init__(self, coord):
        if isinstance(coord, tuple) or isinstance(coord, list):
            self.x = coord[0]
            self.y = coord[1]
            self.actualx = coord[0]
            self.actualy = coord[1]
        elif isinstance(coord, str):
            # TODO check that its a valid str
            self.x, self.y = algebra_to_cartesian(coord)
            self.actualx = self.x
            self.actualy = self.y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __str__(self):
        return (
            str(self.x)
            + ","
            + str(self.y)
            + " "
            + "".join(cartesian_to_algebra((self.x, self.y)))
        )

    def algebraic(self):
        return cartesian_to_algebra((self.actualx, self.actualy))

    def algebraic_newpos(self):
        return cartesian_to_algebra((self.x, self.y))

    def cartesian(self):
        return (self.actualx, self.actualy)

    # TODO if p makes u go out of the board , reject
    def current(self):
        return [self.x, self.y]

    def left(self, num_moves, returnPath=False):
        if 0 <= (self.x - num_moves) <= 7:
            self.x -= num_moves
        else:
            return False

    def right(self, num_moves, returnPath=False):
        if 0 <= self.x + num_moves <= 7:
            # its valid
            self.x += num_moves
        else:
            return False

    def up(self, num_moves, returnPath=False):
        if 0 <= self.y - num_moves <= 7:
            # its valid
            self.y -= num_moves
        else:
            return False

    def down(self, num_moves, returnPath=False):
        if 0 <= self.y + num_moves <= 7:
            self.y += num_moves
        else:
            return False

    #  return None
    def _lu(self, num_moves1, num_moves2):
        # TODO only allow atomic manipulation
        if (0 <= (self.y - num_moves1) <= 7) and 0 <= self.x + -num_moves2 <= 7:
            self.y -= num_moves1
            self.x -= num_moves2
        else:
            return False

    def _ld(self, num_moves1, num_moves2):
        # self.left(num_moves1)
        # self.down(num_moves2)
        if (0 <= (self.y + num_moves1) <= 7) and 0 <= self.x - num_moves2 <= 7:
            self.y += num_moves1
            self.x -= num_moves2
        else:
            return False

    def _ru(self, num_moves1, num_moves2):
        # self.right(num_moves1)
        # self.up(num_moves2)
        if (0 <= (self.y - num_moves1) <= 7) and 0 <= self.x + num_moves2 <= 7:
            self.y -= num_moves1
            self.x += num_moves2
        else:
            return False

    def _rd(self, num_moves1, num_moves2):
        # self.right(num_moves1)
        # self.down(num_moves2)
        if (0 <= (self.y + num_moves1) <= 7) and 0 <= self.x + num_moves2 <= 7:
            self.y += num_moves1
            self.x += num_moves2
        else:
            return False

    def diag(self, way, num_moves, piece=None, returnPath=True):
        list_of_moves = []
        for i in range(0, num_moves):
            # can i do self.way1
            # self.diag(way, 1, returnPath = False)
            prex, prey = self.x, self.y
            eval(self.diag_moves.get(way))

            if piece:

                otherpiece, otherpiecename = piece.board.piece_from_algebraic_coord(
                    self.algebraic_newpos()
                )
                if otherpiece:
                    if otherpiece.color != piece.color:
                        list_of_moves.append([self.x, self.y])
                        break
                    else:
                        break
                    # if otherpiece.color == piece.color:
                    #   break
                    # elif otherpiece

            if prex == self.x and prey == self.y:
                break

            if returnPath:
                list_of_moves.append([self.x, self.y])
        self.x = self.actualx
        self.y = self.actualy
        return list_of_moves

    def knight_hops(self, way, piece=None):
        list_of_moves = []
        prex, prey = self.x, self.y

        eval(self.knight_moves.get(way))
        if prex == self.x and prey == self.y:
            return list_of_moves
        else:
            if piece:
                otherpiece, otherpiecename = piece.board.piece_from_algebraic_coord(
                    self.algebraic_newpos()
                )
                # if otherpiece == None:
                #   list_of_moves.append([self.x, self.y])
                # elif not otherpiece.color == piece.color:
                #   list_of_moves.append([self.x, self.y])

                if otherpiece:
                    if otherpiece.color != piece.color:
                        list_of_moves.append([self.x, self.y])

                else:
                    list_of_moves.append([self.x, self.y])

        self.x = self.actualx
        self.y = self.actualy
        return list_of_moves

    def slide(self, way, num_moves, piece=None, returnPath=True):
        list_of_legal_moves = []
        for i in range(0, num_moves):
            prex, prey = self.x, self.y
            eval(self.slide_moves.get(way))

            if piece:
                obj, objname = piece.board.piece_from_algebraic_coord(
                    self.algebraic_newpos()
                )
                if obj:
                    if obj.color != piece.color:
                        list_of_legal_moves.append([self.x, self.y])
                        break
                    else:
                        break

            # is_piece_in_the_way(list_of_legal_moves)
            if prex == self.x and prey == self.y:
                break
            if returnPath:

                list_of_legal_moves.append([self.x, self.y])
        self.x = self.actualx
        self.y = self.actualy
        return list_of_legal_moves

    """
        def is_piece_in_the_way(self, list_of_moves):

            for tup in list_of_moves:
                val = self.board.piece_from_algebraic_coord(tup)
                # there is a pice there
                if val == True:
                    list_of_moves.remove(tup)
            print(list_of_moves)

            # if tup==board.piece_from_algebraic_coord():

            # pass
    """

    def samecolumn(self, way, newpos, num_moves):
        if (self.y - newpos.y) == num_moves:
            return True
        else:
            return False

    def samerow(self, way, newpos, num_moves=None):
        if self.y == newpos.y:
            return True
        else:
            return False

    def commit(self):
        self.actualx = self.x
        self.actualp = self.y


def test():

    posbr = Pos([7, 7])  # Bottom Right
    postl = Pos([0, 0])  # Top Left
    posbl = Pos([7, 0])  # Bottom Left
    postr = Pos([0, 7])  # Top Right

    print("Left Slide", postl.slide("L", 3))
    pos = Pos([7, 7])  # Bottom Right
    print("Right Slide", postl.slide("R", 3))
    pos = Pos([7, 7])  # Bottom Right
    print("Up Slide", postl.slide("U", 3))
    pos = Pos([7, 7])  # Bottom Right
    print("Down Slide", postl.slide("D", 3))

    print(pos.diag("LU", 3))
    # print(pos.left(2))
    # pos.diag("right", "down", 3)
    # print(pos.current())
    print(pos.diag("LU", 2))
    print(pos.current())

    # assert pos.x == 9
    # assert pos.y == 4

    # pos.right(5)
    # assert pos.x == 9
    # assert pos.y == 4


# test()
