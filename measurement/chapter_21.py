from manimlib import *


class LawOfSinesAcute(Scene):
    def construct(self):
        # create acute triangle
        tp = [0, 3, 0]
        lf = [-2, 0, 0]
        rt = [5, 0, 0]
        l1 = Line(lf, tp)
        l2 = Line(tp, rt)
        l3 = Line(rt, lf)
        acutet = Group(l1, l2, l3).set_color(GREEN)
        acutet.move_to([0,0,0])

        # Initial triangle
        self.play(ShowCreation(acutet), runtime=2)

        # placing side labels
        top_corner = acutet.get_corner(TOP)
        top_corner[0] = acutet.get_corner(LEFT)[0] + 2  # NOTE: because inital top corner +2 from left
        bottom_half = acutet.get_bottom()
        bottom_half[0] = top_corner[0]
        left_corner = acutet.get_corner(LEFT) + acutet.get_bottom()
        right_corner = acutet.get_corner(RIGHT) + acutet.get_bottom()

        left_buf = [-1.0, 0, 0]
        right_buf = [1.0, 0, 0]
        top_buf = [0, 0.5, 0]
        btm_buf = [-0.5, -1.0, 0]
        a_placement = (left_corner + left_buf + top_corner + top_buf)/2
        b_placement = (right_corner + right_buf + top_corner + top_buf)/2
        c_placement = (left_corner + left_buf + right_corner + btm_buf)/2

        # TODO: find better font styles
        a = Text("a").move_to(a_placement)
        b = Text("b").move_to(b_placement)
        c = Text("c").move_to(c_placement)

        self.play(Write(a))
        self.play(Write(b))
        self.play(Write(c))

        # TODO: add angle arcs and labels

        # TODO: dased line would require multiple height lines
        # ie. one height line divided into multiple pieces
        lh = Line(top_corner, bottom_half).set_color(ORANGE)
        self.play(ShowCreation(lh))

        # self.play(acutet.animate.move_to([0,0,0]), runtime=2)
        self.wait()
        self.embed()