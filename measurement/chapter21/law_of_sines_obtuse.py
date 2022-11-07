from manimlib import *


class LawOfSinesObtuse(Scene):
    def construct(self):
        question = Tex(r"\text{Does law of sines hold for an obtuse angle?}")
        law = Tex(r"\sin{A}:\sin{B}:\sin{C} = a:b:c")
        law.next_to(question, BOTTOM)
        self.play(Write(question))
        self.play(Write(law), runtime=2)
        self.wait(1)

        self.embed()