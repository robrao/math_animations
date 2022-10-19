from manimlib import *


class LawOfSinesAcute(Scene):
    def construct(self):
        law = Text("sin A:sin B:sin C = a:b:c").set_color(ORANGE)
        self.play(Write(law), runtime=3)
        self.wait()
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

        # TODO: find better font styles
        a = Text("a").move_to(a_placement)
        b = Text("b").move_to(b_placement)
        c = Text("c").move_to(c_placement)

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
        B = Text("B", color=YELLOW).move_to(labelB_pos)
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
        A = Text("A", color=YELLOW).move_to(labelA_pos)
        self.play(ShowCreation(A))

        # TODO: dashed line would require multiple height lines
        # ie. one height line divided into multiple pieces
        lh = Line(top_corner, bottom_half).set_color(ORANGE)
        self.play(ShowCreation(lh))

        h = Text("h").set_color(ORANGE)
        h.next_to(lh)
        self.play(Write(h))

        # TODO: NEXT
        # * group all labels, arcs, and lines, and shrink + move them to top left corner
        # * show algebra to calculate sinA:sinB = a:b

        # TODO: NEXT NEXT
        # * move grouped items from left corner expand them
        # * clear angles and h line
        # * rotate triangle
        # * repeat steps to calculate sinC:sinA/B = c:a/b

        # self.play(acutet.animate.move_to([0,0,0]), runtime=2)
        self.wait()
        self.embed()