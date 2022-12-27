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

        top_corner = obtuset.get_corner(TOP)
        # top_corner[0] = obtuset.get_corner(LEFT)[0]   # NOTE: because inital top corner +2 from left
        bottom_half = obtuset.get_bottom()
        bottom_half[0] = top_corner[0]
        left_corner = top_corner + obtuset.get_bottom()
        right_corner = obtuset.get_corner(RIGHT) + obtuset.get_bottom()

        left_buf = [-1.0, 0, 0]
        right_buf = [1.0, 0, 0]
        top_buf = [0, 0.5, 0]
        btm_buf = [-0.5, -1.0, 0]
        a_placement = (left_corner + left_buf + top_corner + top_buf)/2
        b_placement = (right_corner + right_buf + top_corner + top_buf)/2
        c_placement = (left_corner + left_buf + right_corner + btm_buf)/2

        a = Tex(r"a").move_to(a_placement)
        b = Tex(r"b").move_to(b_placement)
        c = Tex(r"c").move_to(c_placement)

        self.play(Write(a))
        self.play(Write(b))
        self.play(Write(c))

        self.embed()
