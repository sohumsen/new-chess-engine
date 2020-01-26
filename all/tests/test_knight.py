from pieces import Knight
from utils import algebra_to_cartesian
from board import Board
from exceptions import InvalidMoveException
from pos import Pos

# The code to test
import unittest  # The test framework


class Test_Knight(unittest.TestCase):
    def test_Knight1(self):
        board = Board()
        Board.populate_board(board)
        b = Knight("ddd", Pos("b1"), board)
        # b = Bishop("ddd", Pos("c5"), board)
        # b.move_piece([0, 5])

        # b = Bishop("ddd", Pos("c5"), board)
        board.update(b)

        # self.assertRaises(InvalidMoveException, b.move_piece, Pos("h3"))
        self.assertEqual(b.move_piece(Pos("a2")), False)

        b = Knight("ddd", Pos("b1"), board)
        board.update(b)

        self.assertEqual(b.move_piece(Pos("a3")), True)
        # print("#######################")
        # print(b.move_piece(Pos("a3")))


if __name__ == "__main__":
    unittest.main()
