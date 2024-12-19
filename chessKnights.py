import os
from manim import *
from manim_chess.chess_board import ChessBoard

class Chess(Scene):
    def construct(self):
        board = ChessBoard("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        board.move_to(ORIGIN)
        self.add(board)

        fade_out, movement = board.move_piece(0, 0, 1, 1)
        if fade_out is not None:
            self.play(fade_out)
            self.wait()
        self.play(movement)
        self.wait()