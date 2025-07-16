from manimlib import *
import numpy as np

class DotScene(InteractiveScene):
    def construct(self):
        ##write polies
        polies = VGroup( Tex(r"x^3+x^2+x-1").shift(UP),
                       Tex(r"-x^3-2x^2+2x+2")
                       )
        self.play(Write(polies))
        self.wait()
        self.play(polies[0].animate.shift(2.5*UP+0.4*RIGHT),polies[1].animate.shift(2.8*UP))
        procedure = VGroup(Line(start=5.8*LEFT,end=2*RIGHT).shift(2.5*UP),
                           Tex(r"2x^3+2x^2+2x-2").shift(2.2*UP),
                           Tex(r"2x^4+2x^3+2x^2-2x").shift(1.6*UP+1.1*LEFT),
                           Tex(r"-2x^5-2x^4-2x^3+2x^2").shift(0.9*UP+2.5*LEFT),
                           Tex(r"-x^6-x^5-x^4+x^3").shift(0.3*UP+3.6*LEFT)
                           )
        result = VGroup(Line(start=5.8*LEFT,end=2*RIGHT),
                           Tex(r"-x^6-3x^5-x^4+3x^3+6x^2+0x-2").shift(0.5*DOWN+1.9*LEFT))
        self.play(Write(procedure))
        self.play(Write(result))
        tongshi = Tex(r"(\sum_{i = 0}^{n-1}{a_ix^i})\cdot (\sum_{i = 0}^{n-1}{b_ix^i}) = \sum_{k = 0}^{2n-2}{c_kx^k},c_k=\sum_{\substack{i+j=k \\ i,j \geq 0}}a_ib_j").shift(2.5*DOWN)
        self.play(Write(tongshi))
        self.wait()
        rec = Rectangle(height = 2.5,width=8.1,color = RED).shift(1.25*UP+1.73*LEFT)
        bracex = Brace(rec, RIGHT)
        labelx = TexText(r"$n$",t2c={r"$n$": BLUE}).next_to(bracex, RIGHT)
        bracey = Brace(rec, DOWN)
        labely = TexText(r"$n$",t2c={r"$n$": BLUE}).next_to(bracey, DOWN)
        self.play(ShowCreation(rec))
        self.play(Write(bracex),Write(bracey),Write(labelx),Write(labely),result[1].animate.shift(0.8*DOWN))
        self.wait()
        on_2=Tex(r"O(n^2)",t2c={r"O(n^2)":BLUE}).shift(3.7*DOWN)
        self.play(FadeIn(on_2))
        self.wait()
        self.play(FadeOut(polies),FadeOut(procedure),FadeOut(tongshi),FadeOut(on_2),FadeOut(rec),FadeOut(bracex),FadeOut(labelx),FadeOut(bracey),FadeOut(labely),
                  FadeOut(result))
        ##dot expression
        xishushi = Tex(r"\sum_{i = 0}^{n-1}{a_ix^i}").shift(3*UP+2.5*LEFT)
        dots = Tex(r"(x_0,y_0),(x_1,y_1),\cdots,(x_{n-1},y_{n-1})").shift(3*UP+2.5*RIGHT)
        self.play(Write(xishushi))
        self.wait()
        self.play(Write(dots))
        self.wait()
        dotexpression = Tex(r"\begin{bmatrix} 1 & x_0 & x_0^2 & \cdots & x_0^{n-1} \\ 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n-1} & x_{n-1}^2 & \cdots & x_{n-1}^{n-1} \end{bmatrix}",r"\begin{bmatrix} a_0\\a_1\\ \vdots \\a_{n-1} \end{bmatrix}=",r"\begin{bmatrix} y_0\\y_1\\ \vdots \\ y_{n-1} \end{bmatrix}")
        self.play(Write(dotexpression))
        hanglieshi = Tex(r" \prod_{0 \leq i < j \leq n-1} (x_j - x_i) \neq0").shift(2.5*DOWN)
        self.play(Write(hanglieshi))
        self.wait()
        self.play(FadeOut(hanglieshi))
        ##ni
        dotexpression_deverse = Tex(r"\begin{bmatrix} a_0\\a_1\\ \vdots \\a_{n-1} \end{bmatrix}=",r"\begin{bmatrix} 1 & x_0 & x_0^2 & \cdots & x_0^{n-1} \\ 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n-1} & x_{n-1}^2 & \cdots & x_{n-1}^{n-1} \end{bmatrix}^{-1}",r"\begin{bmatrix} y_0\\y_1\\ \vdots \\ y_{n-1} \end{bmatrix}")
        self.play(TransformMatchingTex(dotexpression,dotexpression_deverse,
                                       key_map={
                                           r"\begin{bmatrix} a_0\\a_1\\ \vdots \\a_{n-1} \end{bmatrix}=":r"\begin{bmatrix} a_0\\a_1\\ \vdots \\a_{n-1} \end{bmatrix}=",
                                           r"\begin{bmatrix} y_0\\y_1\\ \vdots \\ y_{n-1} \end{bmatrix}":r"\begin{bmatrix} y_0\\y_1\\ \vdots \\ y_{n-1} \end{bmatrix}",
                                           r"\begin{bmatrix} 1 & x_0 & x_0^2 & \cdots & x_0^{n-1} \\ 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n-1} & x_{n-1}^2 & \cdots & x_{n-1}^{n-1} \end{bmatrix}":r"\begin{bmatrix} 1 & x_0 & x_0^2 & \cdots & x_0^{n-1} \\ 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n-1} & x_{n-1}^2 & \cdots & x_{n-1}^{n-1} \end{bmatrix}"
                                       }))
        self.wait()
        self.play(FadeOut(xishushi),FadeOut(dots),FadeOut(dotexpression_deverse))

class ProcedureScene(InteractiveScene):
    def construct(self):
        ##draw procedure
        poly1 = Tex(r"\sum_{i = 0}^{n-1}{a_ix^i}").shift(3*UP+2*LEFT)
        poly2 = Tex(r"\sum_{i = 0}^{n-1}{b_ix^i}").shift(3*UP+2*RIGHT)
        arr11 = Arrow((2.3,2.9),(2.3,1.5))
        arr21 = Arrow((-1.7,2.9),(-1.7,1.5))
        self.play(FadeIn(poly1),FadeIn(poly2))
        self.wait()
        self.play(FadeIn(arr11),FadeIn(arr21))
        self.wait()
        pots1 = Tex(r"(x_0,y_0),(x_1,y_1)\dots(x_{2n-1},y_{2n-1})").shift(3.5*LEFT+1.5*UP)
        pots2 = Tex(r"(x_0,y_0'),(x_1,y_1')\dots(x_{2n-1},y_{2n-1}')").shift(3.5*RIGHT+1.5*UP)
        self.play(Write(pots1),Write(pots2))
        self.wait()
        pots = Tex(r"(x_0,y_0y_0'),(x_1,y_1y_1'),\dots,(x_{2n-1},y_{2n-1}y_{2n-1}')")
        arr12=Arrow((-3.5,1.3),(-2,0.2))
        arr22=Arrow((3.5,1.3),(2,0.2))
        self.play(FadeIn(arr12),FadeIn(arr22),Write(pots))
        self.wait()
        arr = Arrow((0,-0.2),(0,-1.9))
        result = Tex(r"\sum_{i = 0}^{2n-1}{c_ix^i}").shift(2.5*DOWN)
        self.play(FadeIn(arr),Write(result))
        self.wait()
        o_n = Tex(r"O(n)").shift(0.7*UP)
        self.play(FadeIn(o_n))
        self.wait()
        o_nlogn_1 = Tex(r"O(n \log n)").shift(3.7*RIGHT+2.2*UP)
        o_nlogn_2 = Tex(r"O(n \log n)").shift(1.5*RIGHT+1*DOWN)
        self.play(FadeIn(o_nlogn_1),FadeIn(o_nlogn_2))
        self.wait()
        self.play(FadeOut(poly1),FadeOut(poly2),FadeOut(arr11),FadeOut(arr12),FadeOut(arr21),
                  FadeOut(arr22),FadeOut(o_nlogn_1),FadeOut(o_nlogn_2),FadeOut(arr),FadeOut(pots1),
                  FadeOut(pots2),FadeOut(pots),FadeOut(result),FadeOut(o_n))

class ImportComplexScene(InteractiveScene):
    def construct(self):
        ##draw duoxiangshi
        poly = Tex(r"-1+x+x^2+x^3")
        self.play(Write(poly))
        self.wait()
        axes = Axes()
        graph = axes.get_graph(lambda x: -1+2*x+x**2+x**3, color=GREEN)
        self.play(poly.animate.move_to(3*UP+2*LEFT),Write(axes))
        self.play(ShowCreation(graph))
        self.wait()
        self.play(FadeOut(graph),FadeOut(poly))
        ##ji
        poly_ji = Tex(r"x+x^3").shift(3*UP+2*LEFT)
        graph_ji = axes.get_graph(lambda x:x+x**3,color=GREEN)
        self.play(Write(poly_ji))
        self.wait()
        self.play(ShowCreation(graph_ji))
        self.wait()
        pnt1 = Dot((1,2,0))
        pnt2 = Dot((-1,-2,0))
        self.play(FadeIn(pnt1))
        self.wait()
        self.play(FadeIn(pnt2))
        self.play(Indicate(pnt2))
        self.wait()
        self.play(FadeOut(poly_ji),FadeOut(graph_ji),FadeOut(pnt1),FadeOut(pnt2))
        ##ou
        poly_ou = Tex(r"-1+x^2").shift(3*UP+3.2*LEFT)
        graph_ou = axes.get_graph(lambda x:-1+x**2,color=GREEN)
        self.play(Write(poly_ou))
        self.wait()
        self.play(ShowCreation(graph_ou))
        self.wait()
        pnt1 = Dot((2,3,0))
        pnt2 = Dot((-2,3,0))
        self.play(FadeIn(pnt1))
        self.wait()
        self.play(FadeIn(pnt2))
        self.play(Indicate(pnt2))
        self.wait()
        self.play(FadeOut(poly_ou),FadeOut(graph_ou),FadeOut(pnt1),FadeOut(pnt2),FadeOut(axes))
        ##defininations
        polyA=Tex(r"A(x)=a_0+a_1x+a_2x^2+\cdots+a_{n-1}x^{n-1}").shift(3*UP)
        polyA0=Tex(r"A^{[0]}(x)=a_0+a_2x+a_4x^2+\cdots +a_{n-2}x^{\frac{n}{2}-1}").shift(2.2*UP)
        polyA1=Tex(r"A^{[1]}(x)=a_1+a_3x+a_5x^2+\cdots +a_{n-1}x^{\frac{n}{2}-1}").shift(1.4*UP)
        polyrelation1 = Tex(r"A(x)=A^{[0]}(x^2)+xA^{[1]}(x^2)",t2c={
            r"xA^{[1]}(x^2)":RED,
            r"A^{[0]}(x^2)":BLUE
        }).shift(0.6*UP)
        polyrelation2 = Tex(r"A(-x)=A^{[0]}(x^2)-xA^{[1]}(x^2)",t2c={
            r"xA^{[1]}(x^2)":RED,
            r"A^{[0]}(x^2)":BLUE
        }).shift(-0.2*UP)
        self.play(Write(polyA))
        self.wait()
        self.play(Write(polyA0),Write(polyA1),Write(polyrelation1))
        self.wait()
        self.play(Write(polyrelation2))
        self.wait()
        self.play(Indicate(polyrelation1[10]),Indicate(polyrelation1[11]),Indicate(polyrelation1[20]),Indicate(polyrelation1[21]),Indicate(polyrelation2[11]),Indicate(polyrelation2[12]),Indicate(polyrelation2[21]),Indicate(polyrelation2[22]))
        arr1 = Arrow((-0.3,-0.4),(-0.3,-2))
        arr2 = Arrow((2,-0.4),(2,-2))
        ##notice
        notice_part1 = Text("只需求出新多项式在",font="Microsoft YaHei",font_size=20).shift(-2.8*UP+1*RIGHT)
        notice_part2 = Tex(r"x^2",color=BLUE).next_to(notice_part1,buff=0.05)
        notice_part3 = Text("处的值，递归求解",font="Microsoft YaHei",font_size=20).next_to(notice_part2,buff=0.05)
        notice = VGroup(
            notice_part1,
            notice_part2,
            notice_part3
        )
        self.play(FadeIn(arr1),FadeIn(arr2),Write(notice))
        self.wait()
        self.play(FadeOut(polyA),FadeOut(polyA0),FadeOut(polyA1),FadeOut(polyrelation1),
                  FadeOut(polyrelation2),FadeOut(arr1),FadeOut(arr2),FadeOut(notice))
        ##example
        example = Tex(r"A(x)=1+3x+2x^2+x^3 |_{x=2}").shift(3*UP)
        self.play(Write(example))
        self.wait()
        procedure1 = Tex(r"A^{[0]}(x)=1+2x").shift(2*UP)
        procedure2 = Tex(r"A^{[1]}(x)=3+x").shift(1*UP)
        self.play(Write(procedure1),Write(procedure2))
        self.wait()
        trans1 = Tex(r"A(x)=1+3x+2x^2+x^3=A^{[0]}(x^2)+xA^{[1]}(x^2) |_{x=2}").shift(3*UP)
        self.play(TransformMatchingTex(example, trans1))
        procedure1_2 = Tex(r"A^{[0]}(x)=1+2x |_{x=4}").shift(2*UP)
        procedure2_2 = Tex(r"A^{[1]}(x)=3+x |_{x=4}").shift(1*UP)
        self.play(TransformMatchingTex(procedure1, procedure1_2),
                  TransformMatchingTex(procedure2, procedure2_2))
        self.wait()
        procedure3_1_1 = Tex(r"A^{{[0]}^{[0]}}(x) = 1")
        procedure3_1_2 = Tex(r"A^{{[0]}^{[1]}}(x) = 2").shift(1*DOWN)
        trans1_2 = Tex(r"A^{[0]}(x)=1+2x=A^{{[0]}^{[0]}}(x^2)+xA^{{[0]}^{[1]}}(x^2) |_{x=4}").shift(2*UP)
        self.play(Write(procedure3_1_1),Write(procedure3_1_2))
        self.play(TransformMatchingTex(procedure1_2, trans1_2))
        procedure3_1 = Tex(r"A^{[0]}(x)=1+2x |_{x=4}=A^{{[0]}^{[0]}}(16)+4A^{{[0]}^{[1]}}(16)=1+4\cdot2=9").shift(2*UP)
        self.play(TransformMatchingTex(trans1_2, procedure3_1))
        self.play(FadeOut(procedure3_1_1),FadeOut(procedure3_1_2))
        self.wait()
        procedure3_2 = Tex(r"A^{[1]}(x)=3+x |_{x=4}=A^{{[1]}^{[0]}}(16)+4A^{{[1]}^{[1]}}(16)=3+4\cdot1=7").shift(1*UP)
        self.play(TransformMatchingTex(procedure2_2, procedure3_2))
        result = Tex(r"A(2)=A^{[0]}(4)+2A^{[1]}(4)=9+2\cdot7=23")
        self.play(Write(result))
        example_regular = Tex(r"A(2) = 1+3\cdot2+2\cdot2^2+2^3 = 23").shift(1*DOWN)
        self.play(Write(example_regular))
        self.wait()
        self.play(FadeOut(procedure3_1),FadeOut(procedure3_2))
        self.play(result.animate.shift(2*UP),example_regular.animate.shift(2*UP))
        result2 = Tex(r"A(-2) =A^{[0]}(4)-2A^{[1]}(4)= 9-2\cdot7 = -5")
        example_regular2 = Tex(r"A(-2) = 1+3\cdot(-2)+2\cdot(-2)^2+(-2)^3 = -5").shift(1*DOWN)
        self.play(Write(result2))
        self.play(Write(example_regular2))
        self.wait()
        self.play(FadeOut(example_regular2),FadeOut(result2),FadeOut(result),FadeOut(example_regular),FadeOut(trans1))
        ##proof time limit
        A = Tex(r"A(x)=a_0+a_1x+a_2x^2+\cdots+a_{n-1}x^{n-1}").shift(3*UP)
        self.play(Write(A))
        A_0 = Tex(r"A^{[0]}(x)=a_0+a_2x+a_4x^2+\cdots +a_{n-2}x^{\frac{n}{2}-1}",font_size=29).shift(1.6*UP+2.8*LEFT)
        A_1 = Tex(r"A^{[1]}(x)=a_1+a_3x+a_5x^2+\cdots +a_{n-1}x^{\frac{n}{2}-1}",font_size=29).shift(1.6*UP+2.8*RIGHT)
        arr1_1 = Arrow((0,2.7),(2.3,1.8))
        arr1_2 = Arrow((0,2.7),(-1.7,1.8))
        self.play(Write(A_0),Write(A_1),FadeIn(arr1_1),FadeIn(arr1_2))
        A_trans1 = Tex(r"A(x)=a_0+a_1x+a_2x^2+\cdots+a_{n-1}x^{n-1}=A^{[0]}(x^2)+xA^{[1]}(x^2)",font_size=38,t2c={
            r"xA^{[1]}(x^2)":RED,
            r"A^{[0]}(x^2)":BLUE
        }).shift(3*UP)
        self.play(TransformMatchingTex(A, A_trans1))
        time_limit = Tex(r"FFT(n)=2FFT(\frac{n}{2})+\Theta(n)",font_size=34).shift(UP)
        self.play(Write(time_limit))
        self.wait()
        self.play(time_limit.animate.shift(2*DOWN))
        ##tree
        arr2_1 = Arrow((-2,1.4,0),(-3,0.2,0))
        arr2_2 = Arrow((-2,1.4,0),(-1,0.2,0))
        arr2_3 = Arrow((2,1.4,0),(1,0.2,0))
        arr2_4 = Arrow((2,1.4,0),(3,0.2,0))
        arr3_1 = Arrow((-3,0.2,0),(-4,-0.4,0))
        arr3_2 = Arrow((-3,0.2,0),(-2,-0.4,0))
        A_0_0 = Tex(r"A^{{[0]}^{[0]}}(x)=a_0+\cdots+a_{n-4}x^{\frac{n}{4}-1}",font_size=30).shift(3.5*LEFT+0.3*UP)
        etc1 = Tex(r"\cdots").shift(1*LEFT+0.3*UP)
        etc2 = Tex(r"\cdots").shift(1*RIGHT+0.3*UP)
        etc3 = Tex(r"\cdots").shift(3*RIGHT+0.3*UP)
        self.play(FadeIn(arr2_1),FadeIn(arr2_2),FadeIn(arr2_3),FadeIn(arr2_4),FadeIn(arr3_1),FadeIn(arr3_2),
                  Write(etc1),Write(etc2),Write(etc3),Write(A_0_0))
        mergeconsume = Tex(r"\Theta(n)=c\cdot n,c\in\mathbb{R}^+",font_size=34).shift(1.6*DOWN)
        arr_UP2 = Arrow((-3,0.2,0),(-3,1.4,0),fill_color=YELLOW)
        label2 = Tex(r"\frac{cn}{2}",font_size=34).shift(3.3*LEFT+0.8*UP)
        self.play(Write(mergeconsume),Write(label2),FadeIn(arr_UP2))
        self.wait()
        label2_trans1 = Tex(r"\frac{cn}{2}\cdot2=cn",font_size=34).shift(4*LEFT+0.8*UP)
        self.play(TransformMatchingTex(label2, label2_trans1))
        self.wait()
        rec = Rectangle(width=11.2,height=4,color=RED).shift((0,1.5,0))
        self.play(ShowCreation(rec))
        brace = Brace(rec,LEFT,buff=0.01)
        label = Tex(r"\Theta(\log n)",font_size=34).next_to(brace,LEFT,buff=0.01)
        self.play(Write(brace),Write(label))
        self.wait()
        ##solve
        condition1 = Tex(r"FFT(1)=\Theta(1)",font_size=34).shift(2.3*DOWN)
        self.play(Write(condition1))
        self.wait()
        ##conclusion
        conclusion = Tex(r"FFT(n)=n\Theta(1)+c\cdot n\log n",font_size=34).shift(3*DOWN)
        self.play(Write(conclusion))
        conclusion2 = Tex(r"FFT(n)=n\Theta(1)+c\cdot n\log n=\Theta(n)+c\cdot n\log n",font_size=34).shift(3*DOWN)
        self.play(TransformMatchingTex(conclusion, conclusion2))
        conclusion3 = Tex(r"FFT(n)=n\Theta(1)+c\cdot n\log n=\Theta(n)+c\cdot n\log n=\Theta(n\log n)",font_size=34).shift(3*DOWN)
        self.play(TransformMatchingTex(conclusion2, conclusion3))
        self.wait()
class ComplexScene(InteractiveScene):
    def construct(self):
        ##intro
        plane = ComplexPlane()
        plane.add_coordinate_labels()
        self.play(Write(plane))
        self.wait()
        z=3/2+2j
        point = plane.n2p(z)
        dot = Dot(point)
        arrow = Arrow(start=ORIGIN, end=point, color=YELLOW,buff=0)
        complex_num = Tex(r"z =\frac{3}{2} + 2i").shift(2.5*UP+2*RIGHT)
        self.play(Write(complex_num))
        self.play(FadeIn(dot))
        self.play(GrowArrow(arrow))
        self.wait()
        arc = Arc(
            radius=0.8,
            start_angle=0,
            angle=np.angle(z),
            arc_center=ORIGIN,
            color=GREEN
        )
        arc_label = Tex(r"\theta=\arctan(\frac{4}{3})").next_to(arc, RIGHT, buff=0.1)
        self.play(FadeIn(arc),Write(arc_label))
        self.wait()
        self.play(FadeOut(arc),FadeOut(arc_label),FadeOut(arrow),FadeOut(dot),FadeOut(complex_num))
        ##oler's formula
        theta = ValueTracker(0)
        formula = Tex(r"e^{i\theta} = \cos\theta + i\sin\theta",tex_to_color_map={r"\cos\theta": BLUE,r"\sin\theta": RED}).shift(1.5*UP+2*RIGHT)
        arrow = always_redraw(lambda: Arrow(ORIGIN, plane.n2p(np.exp(1j*theta.get_value())),fill_color=YELLOW,buff=0))
        proj_x = always_redraw(lambda: Line(ORIGIN, plane.c2p(np.cos(theta.get_value()),0), color=BLUE))
        proj_x2 = always_redraw(lambda: DashedLine(plane.c2p(np.cos(theta.get_value()),0),plane.n2p(np.exp(1j*theta.get_value()))))
        proj_y = always_redraw(lambda: Line(ORIGIN, plane.c2p(0,np.sin(theta.get_value())),color=RED))
        proj_y2 = always_redraw(lambda: DashedLine(plane.c2p(0,np.sin(theta.get_value())),plane.n2p(np.exp(1j*theta.get_value()))))
        labelx = TexText(r"$ \cos\theta $ = 1.00")
        bracex = always_redraw(Brace, proj_x, DOWN)
        labelx.always.next_to(bracex, DOWN)
        numberx = labelx.make_number_changeable("1.00")
        numberx.f_always.set_value(lambda : np.cos(theta.get_value()))
        labely = TexText(r"$ \sin\theta $ = 0.00")
        bracey = always_redraw(Brace, proj_y,  LEFT)
        labely.always.next_to(bracey, LEFT)
        numbery = labely.make_number_changeable("0.00")
        numbery.f_always.set_value(lambda : np.sin(theta.get_value()))
        circle = Circle(stroke_color=GREEN)
        self.play(Write(circle),Write(formula),self.camera.frame.animate.set_width(8))
        self.play(FadeIn(arrow),FadeIn(proj_x),FadeIn(proj_x2),FadeIn(proj_y),FadeIn(proj_y2),FadeIn(bracex),FadeIn(bracey),FadeIn(labelx),FadeIn(labely))
        self.play(theta.animate.set_value(2*PI), run_time=8, rate_func=linear)
        self.play(FadeOut(arrow),FadeOut(proj_x),FadeOut(proj_x2),FadeOut(proj_y),FadeOut(proj_y2),
                  FadeOut(theta),FadeOut(bracex),FadeOut(labelx),FadeOut(bracey),FadeOut(labely),FadeOut(arrow))
        self.play(self.camera.frame.animate.set_width(14.222222),FadeOut(formula),FadeOut(plane.coordinate_labels))
        ##danweigen definition
        definition1 = Tex("z^n=1").shift(2*UP+2*RIGHT)
        n=8
        niseight = Tex("n=8=2^3").shift(2*UP+2.2*LEFT)
        roots = [np.exp(1j * 2 * PI * k / n) for k in range(n)]
        dots = [Dot(plane.n2p(root), fill_color=YELLOW) for root in roots]
        labels = [Tex(r"\omega_n"+(r"^"+str(i%8) if i !=1 else r"")).next_to(dots[i%8],direction=plane.n2p(np.exp(1j*2*PI/n*i))) for i in range(n)]
        self.play(Write(definition1))
        self.wait()
        self.play(Write(niseight))
        self.play(*[FadeIn(dot) for dot in dots],*[Write(label) for label in labels])
        self.wait()
        self.play(FadeOut(definition1))
        self.wait()
        property1 = Tex(r"\omega_n^k=e^{i(\frac{2\pi}{n}k)}").shift(1*UP+3*LEFT)
        property2 = Tex(r"\omega_n^{\frac{n}{2}+k}=-\omega_n^k(k=0,1,\dots,\frac{n}{2}-1)").shift(3*DOWN)
        self.play(Write(property1))
        self.play(Write(property2))
        self.wait()
        self.play(FadeOut(property1),FadeOut(property2))
        ##danweigen
        squared_roots = [root**2 for root in roots]
        squared_roots = squared_roots[0:4]
        squared_dots = [Dot(plane.n2p(root), fill_color=BLUE, radius=0.08) for root in squared_roots]
        self.play(*[FadeOut(dot) for dot in dots[4:]],*[FadeOut(label) for label in labels[4:]])
        self.wait()
        labels2 = [Tex(r"\omega_{\frac{n}{2}}"+(r"^"+str(i) if i !=1 else r"")).next_to(squared_dots[i%4],direction=plane.n2p(np.exp(1j*PI/2*i))) for i in range(4)]
        for dot, squared_dot,label,label2 in zip(dots, squared_dots,labels[:4],labels2):
            self.play(Transform(dot, squared_dot),Transform(label, label2))
        self.wait()
        n2isfour=Tex(r"\frac{n}{2} = 4 = 2^2").shift(2.8*LEFT+0.7*UP)
        self.play(Write(n2isfour))
        self.play(*[Indicate(dot) for dot in squared_dots])
        self.wait()
        conclusion1 = Tex(r"(\omega_n^k)^2=\omega_{\frac{n}{2}}^k(k=0,1,\dots,\frac{n}{2}-1)").shift(3*DOWN)
        self.play(Write(conclusion1))
class FFTScene(InteractiveScene):
    def construct(self):
        ##draw fft
        polyA0=Tex(r"A^{[0]}(x)=a_0+a_2x+a_4x^2+\cdots +a_{n-2}x^{\frac{n}{2}-1}").shift(2.2*UP)
        polyA1=Tex(r"A^{[1]}(x)=a_1+a_3x+a_5x^2+\cdots +a_{n-1}x^{\frac{n}{2}-1}").shift(1.4*UP)
        polyrelation1 = Tex(r"A(x)=A^{[0]}(x^2)+xA^{[1]}(x^2)",t2c={
            r"xA^{[1]}(x^2)":RED,
            r"A^{[0]}(x^2)":BLUE
        }).shift(0.6*UP)
        polyrelation2 = Tex(r"A(-x)=A^{[0]}(x^2)-xA^{[1]}(x^2)",t2c={
            r"xA^{[1]}(x^2)":RED,
            r"A^{[0]}(x^2)":BLUE
        }).shift(-0.2*UP)
        polyrelation1_2 = Tex(r"A(\omega_n^k)=A^{[0]}((\omega_n^k)^2)+\omega_n^kA^{[1]}((\omega_n^k)^2)",t2c={
            r"\omega_n^kA^{[1]}((\omega_n^k)^2)":RED,
            r"A^{[0]}((\omega_n^k)^2)":BLUE
        }).shift(0.6*UP)
        polyrelation2_2 = Tex(r"A(-\omega_n^k)=A^{[0]}((\omega_n^k)^2)-\omega_n^kA^{[1]}((\omega_n^k)^2)",t2c={
            r"\omega_n^kA^{[1]}((\omega_n^k)^2)":RED,
            r"A^{[0]}((\omega_n^k)^2)":BLUE
        }).shift(-0.2*UP)
        self.play(Write(polyrelation1),Write(polyrelation2),Write(polyA0),Write(polyA1))
        self.wait()
        self.play(TransformMatchingTex(polyrelation1, polyrelation1_2,
                                       key_map={
                                           r"A^{[0]}(x^2)":r"A^{[0]}((\omega_n^k)^2)",
                                           r"xA^{[1]}(x^2)":r"\omega_n^kA^{[1]}((\omega_n^k)^2)"
                                       }),
                  TransformMatchingTex(polyrelation2, polyrelation2_2,
                                       key_map={
                                           r"A^{[0]}(x^2)":r"A^{[0]}((\omega_n^k)^2)",
                                           r"xA^{[1]}(x^2)":r"\omega_n^kA^{[1]}((\omega_n^k)^2)"
                                       })
        )
        self.wait()
        ## change form
        self.play(polyrelation1_2.animate.shift(2.5*UP),
                  polyrelation2_2.animate.shift(2.5*UP),FadeOut(polyA0),FadeOut(polyA1))
        reason1 = Tex(r"-\omega_n^k=\omega_n^{k+\frac{n}{2}}").shift(1.6*UP)
        polyrelation2_plus = Tex(r"A(\omega_n^{k+\frac{n}{2}})=A^{[0]}((\omega_n^k)^2)-\omega_n^kA^{[1]}((\omega_n^k)^2)",t2c=
                                 {
                                     r"-\omega_n^kA^{[1]}((\omega_n^k)^2)":RED,
                                     r"A^{[0]}((\omega_n^k)^2)":BLUE
                                 }).shift(2.3*UP)
        self.play(Write(reason1))
        self.play(TransformMatchingTex(polyrelation2_2, polyrelation2_plus))
        self.play(FadeOut(reason1))
        self.wait()
        reason2 = Tex(r"(\omega_n^k)^2=\omega_{\frac{n}{2}}^{k}(k=0,1,\dots,\frac{n}{2}-1)").shift(1.6*UP)
        self.play(Write(reason2))
        polyrelation2_3 = Tex(r"A(\omega_n^{k+\frac{n}{2}})=A^{[0]}(\omega_{\frac{n}{2}}^k)-\omega_n^kA^{[1]}(\omega_{\frac{n}{2}}^k)",
                              t2c={
                                  r"-\omega_n^kA^{[1]}(\omega_{\frac{n}{2}}^k)":RED,
                                  r"A^{[0]}(\omega_{\frac{n}{2}}^k)":BLUE
                              }
                              ).shift(2.3*UP)
        polyrelation1_3 = Tex(r"A(\omega_n^k)=A^{[0]}(\omega_{\frac{n}{2}}^k)+\omega_n^kA^{[1]}(\omega_{\frac{n}{2}}^k)",
                              t2c={
                                  r"\omega_n^kA^{[1]}(\omega_{\frac{n}{2}}^k)":RED,
                                  r"A^{[0]}(\omega_{\frac{n}{2}}^k)":BLUE
                              }
                              ).shift(3.1*UP)
        self.play(TransformMatchingTex(polyrelation2_plus, polyrelation2_3,
                                       ))
        self.play(TransformMatchingTex(polyrelation1_2, polyrelation1_3,
                                       key_map={
                                           r"A^{[0]}((\omega_n^k)^2)":r"A^{[0]}(\omega_{\frac{n}{2}}^k)",
                                           r"\omega_n^{k+\frac{n}{2}}A^{[1]}((\omega_n^k)^2)":r"\omega_n^{k+\frac{n}{2}}A^{[1]}(\omega_{\frac{n}{2}}^k)"
                                       }))
        self.play(FadeOut(reason2))
        self.wait()
        ##conclusion
        condition1 = Tex(r"n=2^k,k\in\mathbb{N}")
        condition2 = Tex(r"k\in\{0,1,\dots,\frac{n}{2}-1\}").shift(0.8*DOWN)
        polyA0.shift(0.8*DOWN)
        polyA1.shift(0.8*DOWN)
        self.play(Write(condition1))
        self.play(Write(condition2))
        self.play(Write(polyA0),Write(polyA1))
        self.wait()
        A0 = Tex(r"A^{[0]}(\omega_{\frac{n}{2}}^k)").shift(1.8*DOWN+3*LEFT)
        A1 = Tex(r"A^{[1]}(\omega_{\frac{n}{2}}^k)").shift(1.8*DOWN+1*LEFT)
        label = Text("这两个都是次数折半的多项式\n同时单位根的次数也对应折半\n递归求解",font_size=18,font="Microsoft YaHei").shift(1.8*DOWN+4*RIGHT)
        arr  = Arrow(A1.get_right(),label.get_left())
        self.play(Write(A0),Write(A1))
        self.play(FadeIn(arr),Write(label))
        self.wait()

class IDFTScene(InteractiveScene):
    def construct(self):
        ##fourier
        NiJuZhen = Tex(r"\begin{bmatrix}  1&  1&  1&  1& \dots& 1\\  1&  \omega_n&  \omega_n^2&  \omega_n^3&  \dots& \omega_n^{n-1}\\  1&  \omega_n^2&  \omega_n^4&  \omega_n^6&  \dots& \omega_n^{2(n-1)}\\  1&  \omega_n^3&  \omega_n^6&  \omega_n^9&  \dots& \omega_n^{3(n-1)}\\  \vdots&  \vdots&  \vdots&  \vdots&  \ddots & \vdots \\  1&  \omega_n^{(n-1)}&  \omega_n^{2(n-1)}&  \omega_n^{3(n-1)}&  \dots& \omega_n^{(n-1)(n-1)}\end{bmatrix}^{-1}=\frac{1}{n}\begin{bmatrix}1 & 1 & 1 & 1 & \cdots & 1 \\1 & \omega_n^{-1} & \omega_n^{-2} & \omega_n^{-3} & \cdots & \omega_n^{-(n-1)} \\1 & \omega_n^{-2} & \omega_n^{-4} & \omega_n^{-6} & \cdots & \omega_n^{-2(n-1)} \\1 & \omega_n^{-3} & \omega_n^{-6} & \omega_n^{-9} & \cdots & \omega_n^{-3(n-1)} \\\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\1 & \omega_n^{-(n-1)} & \omega_n^{-2(n-1)} & \omega_n^{-3(n-1)} & \cdots & \omega_n^{-(n-1)(n-1)}\end{bmatrix}",font_size=28)
        self.play(Write(NiJuZhen))
        self.wait()
        self.play(FadeOut(NiJuZhen))
        ##draw idft
        formula1 = Tex(r"\begin{bmatrix}  1&  1&  1&  1& \dots& 1\\  1&  \omega_n&  \omega_n^2&  \omega_n^3&  \dots& \omega_n^{n-1}\\  1&  \omega_n^2&  \omega_n^4&  \omega_n^6&  \dots& \omega_n^{2(n-1)}\\  1&  \omega_n^3&  \omega_n^6&  \omega_n^9&  \dots& \omega_n^{3(n-1)}\\  \vdots&  \vdots&  \vdots&  \vdots&  \ddots & \vdots \\  1&  \omega_n^{(n-1)}&  \omega_n^{2(n-1)}&  \omega_n^{3(n-1)}&  \dots& \omega_n^{(n-1)(n-1)}\end{bmatrix}\begin{bmatrix} a_0\\ a_1\\ a_2\\ a_3\\ \vdots\\a_{n-1}\end{bmatrix}=\begin{bmatrix} y_0\\ y_1\\ y_2\\ y_3\\ \vdots\\y_{n-1}\end{bmatrix}",font_size=34).shift(2*UP)
        self.play(Write(formula1))
        self.wait()
        calculate_A2 = Tex(r"\begin{bmatrix} a_0 \\ a_1 \\ a_2 \\ a_3 \\ \vdots \\ a_{n-1} \end{bmatrix} = \frac{1}{n}\begin{bmatrix}1 & 1 & 1 & 1 & \cdots & 1 \\1 & \omega_n^{-1} & \omega_n^{-2} & \omega_n^{-3} & \cdots & \omega_n^{-(n-1)} \\1 & \omega_n^{-2} & \omega_n^{-4} & \omega_n^{-6} & \cdots & \omega_n^{-2(n-1)} \\1 & \omega_n^{-3} & \omega_n^{-6} & \omega_n^{-9} & \cdots & \omega_n^{-3(n-1)} \\\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\1 & \omega_n^{-(n-1)} & \omega_n^{-2(n-1)} & \omega_n^{-3(n-1)} & \cdots & \omega_n^{-(n-1)(n-1)}\end{bmatrix}\begin{bmatrix} y_0 \\ y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_{n-1} \end{bmatrix}",font_size=34,
                           t2c={
                               r"\frac{1}{n}": RED,
                               r"-":BLUE,
                               r"n-1":WHITE
                           }).shift(2*DOWN)
        self.play(Write(calculate_A2))
class SumUpScene(InteractiveScene):
    def construct(self) :
        pass #TODO: Add a summary scene