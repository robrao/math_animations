from manimlib import *


class LawOfSinesObtuse(Scene):
    def construct(self):
        question = Tex(r"\text{Does law of sines hold for an obtuse angle?}")
        law = Tex(r"\sin{A}:\sin{B}:\sin{C} = a:b:c")
        law.next_to(question, BOTTOM)
        self.play(Write(question))
        self.play(Write(law), runtime=2)
        self.wait(1)
        self.clear()


        # NOTE: create obtuse triangle
        lf = [-3, 0, 0]
        rt = [3, 0, 0]
        tp = [-5, 4, 0]
        l1 = Line(lf, tp)
        l2 = Line(tp, rt)
        l3 = Line(rt, lf)
        obtuset = VGroup(l1, l2, l3).set_color(GREEN)
        obtuset.move_to([0,0,0])

        self.play(ShowCreation(obtuset), runtime=2)

        top = obtuset.get_top()
        bottom = obtuset.get_bottom()
        left_top = obtuset.get_left()
        left_btm = left_top - np.array([-2.0, 0, 0])
        right = obtuset.get_right()

        left = (left_top + left_btm)/2

        a_buffer = np.array([-1.0, -1.0, 0])
        b_buffer = np.array([1.0, 1.0, 0])
        c_buffer = np.array([0, -1.0, 0])
        a_placement = left + (top + bottom + a_buffer)/2
        b_placement = (left_top + right + top + bottom + b_buffer)/2
        c_placement = (left_btm + right + c_buffer)/2 + bottom


        a = Tex(r"a").move_to(a_placement)
        b = Tex(r"b").move_to(b_placement)
        c = Tex(r"c").move_to(c_placement)

        self.play(Write(a))
        self.play(Write(b))
        self.play(Write(c))

        # TODO: create anglesdd

        # NOTE: split obtuse angle with line h
        lbl = left_btm + bottom
        ltr = left_top + right + top + bottom
        slope_h = (ltr[1] - lbl[1])/(ltr[0] - lbl[0])
        lh = Line(lbl, ltr).set_color(ORANGE)
        self.play(ShowCreation(lh))

        # TODO: fix alignment of h to lh
        h = Tex(r"h").set_color(ORANGE)
        hx = 0.5 * (lbl[0] - ltr[0])
        hy = slope_h * hx
        hx = hx * 0.50 # buffer fraction since negative # add buffer
        h.move_to(np.array([hx, hy, 0]))
        self.play(Write(h))

        self.embed()
