from manimlib import *


class LawOfSinesAcute(Scene):
    def construct(self):
        law = Tex(r"\sin{A}:\sin{B}:\sin{C} = a:b:c")
        self.play(Write(law), runtime=2)
        self.wait(1)
        self.clear()

        # TODO: make all drawings output of a function.
        # only need initial
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

        a = Tex(r"a").move_to(a_placement)
        b = Tex(r"b").move_to(b_placement)
        c = Tex(r"c").move_to(c_placement)

        self.play(Write(a))
        self.play(Write(b))
        self.play(Write(c))

        # NOTE: add angle B arc and labels
        arcB_start = np.array([(left_corner[0] - left_corner[0] * 0.10), left_corner[1], 0])
        slopeA = (tp[1]-lf[1])/(tp[0]-lf[0])
        intercept = bottom_half[1]
        arcB_endpoint = (slopeA * (arcB_start[0] - left_corner[0])) + intercept
        arcB_end = np.array([arcB_start[0], arcB_endpoint, 0])
        arcB = ArcBetweenPoints(start=arcB_start, end=arcB_end, stroke_color=YELLOW)
        self.play(ShowCreation(arcB))

        # NOTE: angle B label
        labelB_pos = arcB.get_corner(BOTTOM)
        labelB_pos = np.array([labelB_pos[0] + 0.35, labelB_pos[1] + 0.35, 0])
        B = Tex(r"B", color=YELLOW).move_to(labelB_pos)
        self.play(ShowCreation(B))

        # NOTE: add angle A arc and labels
        ratio_dist = (left_corner[0] - arcB_start[0])/(left_corner[0] - bottom_half[0])
        arcA_start = np.array([(right_corner[0] - right_corner[0] * ratio_dist), bottom_half[1], 0])
        slopeB = (rt[1]-tp[1])/(rt[0]-tp[0])
        arcA_endpoint = (slopeB * (arcA_start[0] - right_corner[0])) + intercept
        arcA_end = np.array([arcA_start[0], arcA_endpoint, 0])
        arcA = ArcBetweenPoints(end=arcA_start, start=arcA_end, stroke_color=YELLOW)  # NOTE: end and start reveresed so arc curves into triangle
        self.play(ShowCreation(arcA))

        # NOTE: angle A label
        labelA_pos = arcA.get_corner(BOTTOM)
        labelA_pos = np.array([labelA_pos[0] - 0.35, labelA_pos[1] + 0.30, 0])
        A = Tex(r"A", color=YELLOW).move_to(labelA_pos)
        self.play(ShowCreation(A))

        # TODO: dashed line would require multiple height lines
        # ie. one height line divided into multiple pieces
        lh = Line(top_corner, bottom_half).set_color(ORANGE)
        self.play(ShowCreation(lh))

        h = Text("h").set_color(ORANGE)
        h.next_to(lh)
        self.play(Write(h))

        # NOTE: group diagram and move to create space for algebra
        diagram = Group(acutet, a, b, c, arcA, arcB, A, B, lh, h)
        self.play(diagram.animate.move_to(np.array([0, 1.7,0])))

        # NOTE: Show algebra
        sinB = Tex(r"\sin{B}=\frac{h}{a}").move_to(np.array([-2, -2, 0]))
        sinA = Tex(r"\sin{A}=\frac{h}{b}").move_to(np.array([1, -2, 0]))
        self.play(ShowCreation(sinB))
        self.play(ShowCreation(sinA))
        self.wait(2)

        # NOTE: clear previous equations
        eq1 = VGroup(sinB, sinA)
        self.remove(eq1)

        eq_point = np.array([-1,-2,0])
        eq2 = Tex(r"\frac{\sin{B}}{\sin{A}}=\frac{\frac{h}{a}}{\frac{h}{b}}").move_to(eq_point)
        self.play(Write(eq2))
        self.wait(2)

        eq3 = Tex(r"\frac{\sin{B}}{\sin{A}}=\frac{h}{a}\times\frac{b}{h}").move_to(eq_point)
        self.play(ReplacementTransform(eq2, eq3), runtime=2)
        self.wait(2)

        eq4 = Tex(r"\frac{\sin{B}}{\sin{A}}=\frac{b}{a}").move_to(eq_point)
        self.play(ReplacementTransform(eq3, eq4), runtime=2)
        self.wait(2)

        eq5 = Tex(r"\sin{B} : \sin{A} = b : a").move_to(eq_point)
        self.play(ReplacementTransform(eq4, eq5), runtime=2)
        self.wait(2)

        # TODO: NEXT
        # * move grouped items from top, to center
        # * clear angles and h line
        # * rotate triangle
        # * repeat steps to calculate sinC:sinA/B = c:a/b

        # self.play(acutet.animate.move_to([0,0,0]), runtime=2)
        self.wait()
        self.embed()