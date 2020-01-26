from pos import Pos
from board import Board
from utils import algebra_to_cartesian, cartesian_to_algebra

# The code to test
import unittest  # The test framework


class Test_Pos(unittest.TestCase):
    def test_diag_LU(self):

        self.assertEquals(Pos(algebra_to_cartesian("a1")).diag("LU", 5), [])
        self.assertEquals(Pos(algebra_to_cartesian("a8")).diag("LU", 5), [])

        """self.assertEquals(
            Pos(algebra_to_cartesian("h1")).diag("LU", 5),
            [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2]],
        )
        """
        print(Pos(algebra_to_cartesian("h8")).diag("LU", 5))
        self.assertEquals(Pos(algebra_to_cartesian("h8")).diag("LU", 5), [])

    def test_diag_RU(self):

        self.assertEquals(
            Pos(algebra_to_cartesian("a1")).diag("RU", 5),
            [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2]],
        )
        self.assertEquals(Pos(algebra_to_cartesian("a8")).diag("RU", 5), [])

        self.assertEquals(Pos(algebra_to_cartesian("h1")).diag("RU", 5), [])

        self.assertEquals(Pos(algebra_to_cartesian("h8")).diag("RU", 5), [])

    def test_pos_slide_withboard(self):
        pos = Pos("a3")
        print(pos.slide("U", 3))
        # TODO self assert

        board = Board()
        board.populate_board()

        pos = Pos("a1")
        print(pos.slide("U", 2, board))
        # TODO self assert

        pos = Pos("h1")
        print(pos.slide("U", 2, board))
        # TODO self assert

    def test_knight_hops(self):

        # knight_pos = Pos(algebra_to_cartesian("b1"))
        # self.assertEquals((knight_pos).knight_hops("RU"), [])
        self.assertEquals(Pos(algebra_to_cartesian("b1")).knight_hops("RU"), [[2, 5]])

        # self.assertEquals(knight_pos).knight_hops("RD", [121])
        # self.assertEquals(knight_pos).knight_hops("LU", [1])
        # self.assertEquals(knight_pos).knight_hops("LD", [1])
        # print(knight_pos.knight_hops())
        print("8888", Pos(algebra_to_cartesian("b1")).knight_hops("RD"))
        print("8888", Pos(algebra_to_cartesian("b1")).knight_hops("RU"))
        print("8888", Pos(algebra_to_cartesian("b1")).knight_hops("LU"))
        print("8888", Pos(algebra_to_cartesian("b1")).knight_hops("LD"))


if __name__ == "__main__":
    unittest.main()
