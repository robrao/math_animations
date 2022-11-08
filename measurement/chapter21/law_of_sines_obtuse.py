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
        self.embed()