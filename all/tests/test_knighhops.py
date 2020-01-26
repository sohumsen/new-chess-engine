from pieces import Knight
from utils import algebra_to_cartesian
from board import Board
from exceptions import InvalidMoveException
from pos import Pos

# The code to test
import unittest  # The test framework


class Test_King(unittest.TestCase):
    def test_knight(self):
        board = Board()
        Board.populate_board(board)
        # b = Bishop("ddd", Pos("b8"), board)
        # self.assertEqual(b.move_piece(Pos("a7")), True)

        # b = Knight("ddd", Pos("c5"), board)
        # board.update(b)

        # self.assertRaises(InvalidMoveException, b.move_piece, Pos("h3"))
        # self.assertEqual(b.move_piece(Pos("h3")), False)

        b = Knight("ddd", Pos("b1"), board)
        board.update(b)

        # self.assertEqual(b.move_piece(Pos("a3")), True)
        print("####################################")
        print(b.move_piece(Pos("d2")))


if __name__ == "__main__":
    unittest.main()
