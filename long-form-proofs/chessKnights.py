from manim import *


class ChessBoardScene(Scene):
    def construct(self):
        # test_square = Square(color=WHITE)
        # self.play(Create(test_square))
        # self.wait(1)

        self.board = ChessBoard()
        self.play(Create(self.board))
        self.wait(1)
        self.play(Create(self.board.get_grid()[0]))
        self.wait(1)
        self.play(Create(self.board.get_grid()[1]))
        self.wait(1)
        self.play(Create(self.board.get_grid()[2]))
        self.wait(1)
        self.play(Create(self.board.get_grid()[3]))
        self.wait(1)
        self.play(Create(self.board.get_grid()[4]))
        self.wait(1)
        self.play(Create(self.board.get_grid()[5]))
        self.wait(1)


class ChessBoard(VGroup):
    CONFIG = {
        "height": 6,
        "width": 6,
    }

    def __init__(self, height=8, width=8, **kwargs):
        super().__init__(**kwargs)
        n_rows = 8
        n_cols = 8
        grid = []
        for row in range(n_rows):
            for col in range(n_cols):
                color = BLUE_D if (row + col) % 2 == 0 else BLUE_E
                grid.append(
                    Rectangle(
                        height=height / n_rows,
                        width=width / n_cols,
                        stroke_width=0,
                        fill_color=color,
                        fill_opacity=1,
                    )
                )
        self.add(*grid)
        self.center()
        self.grid = grid
        self.n_rows = n_rows
        self.n_cols = n_cols

    def get_grid(self):
        return self.grid

    def get_rows(self):
        return self.n_rows

    def get_cols(self):
        return self.n_cols


class KnightMoves(VGroup):
    CONFIG = {
        "radius": 0.12,
        "direction": UP + RIGHT,
        "color": YELLOW,
    }

    def __init__(self, direction=None, radius=None, color=None, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.direction = direction
        self.color = color
        self.add(self.create_arrow())

    def create_arrow(self):
        arrow = Arrow(
            ORIGIN, self.radius * self.direction, buff=0, color=self.color
        )
        arrow.set_stroke(width=6)
        return arrow

# if __name__ == "__main__":
#     scene = ChessBoardScene()

#     scene.construct()
