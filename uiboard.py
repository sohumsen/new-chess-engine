import pygame
from pos import Pos
from utils import cartesian_to_algebra, algebra_to_cartesian
from board import Board


class Uiboard:
    def __init__(self):

        # set color with rgb
        self.white, self.black, self.red = (255, 255, 255), (150, 150, 150), (255, 0, 0)

        # set display
        self.gameDisplay = pygame.display.set_mode((800, 700))

        # caption

        # beginning of logic
        self.gameExit = False

        self.size = 60
        pygame.init()
        pygame.display.set_caption("ChessBoard")
        self.font = pygame.font.Font("freesansbold.ttf", 24)
        self.gameDisplay.fill(self.white)
        self.textX, self.textY = 600, 60

        # board length, must be even
        self.boardLength = 8

    # def make_grid():
    def drawEmptyBoard(self):
        """ Setup the basic chess board """

        cnt = 0
        for i in range(1, self.boardLength + 1):
            for z in range(1, self.boardLength + 1):
                # check if current loop value is even
                if cnt % 2 == 0:
                    pygame.draw.rect(
                        self.gameDisplay,
                        self.white,
                        [self.size * z, self.size * i, self.size, self.size],
                    )
                else:
                    pygame.draw.rect(
                        self.gameDisplay,
                        self.black,
                        [self.size * z, self.size * i, self.size, self.size],
                    )
                cnt += 1
            # since theres an even number of squares go back one value
            cnt -= 1
        # Add a nice boarder
        pygame.draw.rect(
            self.gameDisplay,
            self.black,
            [
                self.size,
                self.size,
                self.boardLength * self.size,
                self.boardLength * self.size,
            ],
            1,
        )

        pygame.display.update()

    """
    def init_piece(self):
        # image =
        self.gameDisplay.blit(pygame.image.load("ui\\black_rook.png"), (60, 60))
        self.gameDisplay.blit(pygame.image.load("ui\\black_knight.png"), (120, 60))
        self.gameDisplay.blit(pygame.image.load("ui\\black_bishop.png"), (180, 60))
        self.gameDisplay.blit(pygame.image.load("ui\\black_queen.png"), (240, 60))
        self.gameDisplay.blit(pygame.image.load("ui\\black_king.png"), (300, 60))
        self.gameDisplay.blit(pygame.image.load("ui\\black_bishop.png"), (360, 60))
        self.gameDisplay.blit(pygame.image.load("ui\\black_knight.png"), (420, 60))
        self.gameDisplay.blit(pygame.image.load("ui\\black_rook.png"), (480, 60))
        self.gameDisplay.blit(pygame.image.load("ui\\black_pawn.png"), (60, 120))
        self.gameDisplay.blit(pygame.image.load("ui\\black_pawn.png"), (120, 120))
        self.gameDisplay.blit(pygame.image.load("ui\\black_pawn.png"), (180, 120))
        self.gameDisplay.blit(pygame.image.load("ui\\black_pawn.png"), (240, 120))
        self.gameDisplay.blit(pygame.image.load("ui\\black_pawn.png"), (300, 120))
        self.gameDisplay.blit(pygame.image.load("ui\\black_pawn.png"), (360, 120))
        self.gameDisplay.blit(pygame.image.load("ui\\black_pawn.png"), (420, 120))
        self.gameDisplay.blit(pygame.image.load("ui\\black_pawn.png"), (480, 120))

        self.gameDisplay.blit(pygame.image.load("ui\\white_rook.png"), (60, 480))
        self.gameDisplay.blit(pygame.image.load("ui\\white_knight.png"), (120, 480))
        self.gameDisplay.blit(pygame.image.load("ui\\white_bishop.png"), (180, 480))
        self.gameDisplay.blit(pygame.image.load("ui\\white_queen.png"), (240, 480))
        self.gameDisplay.blit(pygame.image.load("ui\\white_king.png"), (300, 480))
        self.gameDisplay.blit(pygame.image.load("ui\\white_bishop.png"), (360, 480))
        self.gameDisplay.blit(pygame.image.load("ui\\white_knight.png"), (420, 480))
        self.gameDisplay.blit(pygame.image.load("ui\\white_rook.png"), (480, 480))
        self.gameDisplay.blit(pygame.image.load("ui\\white_pawn.png"), (60, 420))
        self.gameDisplay.blit(pygame.image.load("ui\\white_pawn.png"), (120, 420))
        self.gameDisplay.blit(pygame.image.load("ui\\white_pawn.png"), (180, 420))
        self.gameDisplay.blit(pygame.image.load("ui\\white_pawn.png"), (240, 420))
        self.gameDisplay.blit(pygame.image.load("ui\\white_pawn.png"), (300, 420))
        self.gameDisplay.blit(pygame.image.load("ui\\white_pawn.png"), (360, 420))
        self.gameDisplay.blit(pygame.image.load("ui\\white_pawn.png"), (420, 420))
        self.gameDisplay.blit(pygame.image.load("ui\\white_pawn.png"), (480, 420))
    """

    def gameOn(self, board):
        """ This method has a while loop  until game exit is called"""

        self.paintBoard(board)

        # display_surface = pygame.display.set_mode((X, Y))
        buffer = None

        while not self.gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    pos = pygame.mouse.get_pos()
                    alg = self.eventpos_to_algebraic(pos)

                    if buffer:
                        # previous click selected the fella
                        print(buffer)
                        selectedPiece, orgalg = buffer

                        if selectedPiece.move_piece(Pos(alg)):
                            self.paintBoard(board)
                            self.paintMoveText(str(orgalg) + " " + str(alg))

                        else:
                            self.paintMoveText("Invalid Move")

                        buffer = None

                    else:
                        # this click is the first click
                        selectedPiece, nm = board.piece_from_algebraic_coord(alg)
                        if selectedPiece:
                            buffer = selectedPiece, alg

                    # TODO plug in ur board data structure to get the peice
                    # given a pos , go ask the board which piece it is
                    # save the pos and piece for another event to come
                    # if pos and piece is saved in buffer and an event comes with newpos
                    # ask the engine if pice can move
                    # if engine says yes , board is updated automatically

                    # print(event, pos, x, y, alg)

            # make_grid()
            # init_piece()
            pygame.display.update()
        # pygame.quit()
        # quit()

    def eventpos_to_algebraic(self, pos):
        x = (pos[0] - 60) // 60
        y = (pos[1] - 60) // 60
        # TODO utils cant return anything greater than 8 or g
        alg = cartesian_to_algebra((x, y))
        return alg

    def paintBoard(self, board: Board):
        """ Given any board it will blit the positions 
            Requires the pieces in the board to have specific names so that 
            the png paths can be found
        """
        self.drawEmptyBoard()
        for posstr, piece in board.pieceByPosDict.items():
            print(posstr, piece)
            res = piece.name.split("_")
            print(res)
            pngpath = "_".join([res[0], res[1]])
            displayimg = pygame.image.load("ui\\%s.png" % (pngpath))  # from piece
            X, Y = algebra_to_cartesian(posstr)
            print((X + 1) * 60, (Y + 1) * 60)
            self.gameDisplay.blit(displayimg, ((X + 1) * 60, (Y + 1) * 60))

    def paintMoveText(self, alg: str):
        """ Paints a string , keeps the latest position updated """
        text = self.font.render(alg, True, self.black, self.white)
        textRect = text.get_rect()
        textRect.center = (self.textX, self.textY)
        self.gameDisplay.blit(text, textRect)
        print(self.textX, self.textY)
        self.textY += 40


CHESSPIECEDICT = {}
# gameDisplay.blit(image, (120, 60))

# Change the x/y screen coordinates to grid coordinates
# column = (pos[0]-xDistanceFromEdge) // (width+margin)
# row = pos[1] // (height+margin)

# draw a rectangle
# gameDisplay.fill(white)
# pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 20, 20])
# pygame.display.update()

# quit from pygame & python

if __name__ == "__main__":
    # view
    uiboard = Uiboard()

    # model
    board = Board()
    board.populate_board()
    # board.printBoardOnScreen()

    uiboard.gameOn(board)

