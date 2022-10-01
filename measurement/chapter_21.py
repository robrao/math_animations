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

        # TODO: fix placement, font type
        a = Text("a").next_to(acutet, LEFT, buff=0.1)
        b = Text("b").next_to(acutet, RIGHT, buff=0.1)
        c = Text("c").next_to(acutet, BOTTOM, buff=0.1)

        self.play(Write(a))
        self.play(Write(b))
        self.play(Write(c))

        # TODO: add angle arcs and labels

        # TODO: dased line would require multiple height lines
        # ie. one height line divided into multiple pieces
        top_corner = acutet.get_corner(TOP)
        bottom_corner = acutet.get_bottom()
        top_corner[0] = acutet.get_corner(LEFT)[0] + 2  # NOTE: because inital top corner +2 from left
        bottom_corner[0] = top_corner[0]
        lh = Line(top_corner, bottom_corner).set_color(ORANGE)
        self.play(ShowCreation(lh))

        # self.play(acutet.animate.move_to([0,0,0]), runtime=2)
        self.wait()
        self.embed()