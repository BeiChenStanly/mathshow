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
        tongshi = Tex(r"(\sum_{i = 0}^{n-1}{a_ix^i})\cdot (\sum_{i = 0}^{n-1}{b_ix^i}) = \sum_{k = 0}^{2n-2}{c_kx^k},\quad c_k=\sum_{\substack{i+j=k \\ i,j \geq 0}}a_ib_j").shift(2.5*DOWN)
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
        ##example
        example_1 = Tex(r"kx+b").shift(3*UP+4*LEFT)
        axes = Axes()
        graph = axes.get_graph(lambda x: 2*x+1, color=GREEN)
        dot_1 = Dot((1,3,0))
        label_1 = Tex(r"(1,3)").next_to(dot_1, RIGHT)
        dot_2 = Dot((-1,-1,0))
        label_2 = Tex(r"(-1,-1)").next_to(dot_2, DOWN)
        self.play(Write(example_1))
        self.play(ShowCreation(axes),ShowCreation(dot_1),ShowCreation(dot_2))
        self.play(Write(label_1),Write(label_2))
        procedure_1 = Tex(r"\left\{\begin{matrix}k+b=3\\-k+b=-1\end{matrix}\right.").shift(1.4*UP+4*LEFT)
        procedure_2 = Tex(r"\left\{\begin{matrix}k=2\\b=1\end{matrix}\right.").shift(-0.2*UP+4*LEFT)
        self.play(Write(procedure_1))
        self.wait()
        self.play(TransformMatchingTex(procedure_1.copy(), procedure_2))
        self.play(ShowCreation(graph))
        example_2 = Tex(r"ax^2+bx+c").shift(3*UP+4*RIGHT)
        graph_2 = axes.get_graph(lambda x: x**2+2*x, color=RED)
        dot_3 = Dot((0,0,0))
        label_3 = Tex(r"(0,0)").next_to(dot_3, RIGHT)
        procedure_3 = Tex(r"\left\{\begin{matrix}a+b+c=3\\a-b+c=-1\\c=0\end{matrix}\right.").shift(1.1*UP+4*RIGHT)
        procedure_4 = Tex(r"\left\{\begin{matrix}a=1\\b=2\\c=0\end{matrix}\right.").shift(1.4*DOWN+4*RIGHT)
        self.play(Write(example_2))
        self.play(ShowCreation(dot_3),Write(label_3))
        self.play(Write(procedure_3),ShowCreation(graph_2))
        self.wait()
        self.play(TransformMatchingTex(procedure_3.copy(), procedure_4))
        self.wait()
        self.play(FadeOut(example_1),FadeOut(example_2),FadeOut(axes),FadeOut(graph),FadeOut(graph_2),
                    FadeOut(dot_1),FadeOut(dot_2),FadeOut(dot_3),
                    FadeOut(label_1),FadeOut(label_2),FadeOut(label_3),
                    FadeOut(procedure_1),FadeOut(procedure_2),FadeOut(procedure_3),FadeOut(procedure_4))
        ##dot expression
        xishushi = Tex(r"\sum_{i = 0}^{n-1}{a_ix^i}").shift(3*UP+2.5*LEFT)
        dots = Tex(r"(x_0,y_0),(x_1,y_1),\cdots,(x_{n-1},y_{n-1})").shift(3*UP+2.5*RIGHT)
        self.play(Write(xishushi))
        self.wait()
        self.play(Write(dots))
        self.wait()
        dotexpression = Tex(r"\begin{bmatrix} 1 & x_0 & x_0^2 & \cdots & x_0^{n-1} \\ 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n-1} & x_{n-1}^2 & \cdots & x_{n-1}^{n-1} \end{bmatrix}",r"\begin{bmatrix} a_0\\a_1\\ \vdots \\a_{n-1} \end{bmatrix}=",r"\begin{bmatrix} y_0\\y_1\\ \vdots \\ y_{n-1} \end{bmatrix}")
        self.play(Write(dotexpression))
        self.wait()
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
        ##ji
        poly_ji = Tex(r"x+x^3").shift(2*UP+2*LEFT)
        graph_ji = axes.get_graph(lambda x:x+x**3,color=RED)
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
        ##ou
        poly_ou = Tex(r"-1+x^2").shift(1*UP+3.2*LEFT)
        graph_ou = axes.get_graph(lambda x:-1+x**2,color=BLUE)
        self.play(Write(poly_ou))
        self.wait()
        self.play(ShowCreation(graph_ou))
        self.wait()
        pnt3 = Dot((1,0,0))
        pnt4 = Dot((-1,0,0))
        self.play(FadeIn(pnt3))
        self.wait()
        self.play(FadeIn(pnt4))
        self.play(Indicate(pnt4))
        self.wait()
        self.play(FadeOut(graph),FadeOut(poly),FadeOut(poly_ji),FadeOut(graph_ji),FadeOut(pnt3),FadeOut(pnt4),FadeOut(poly_ou),FadeOut(graph_ou),FadeOut(pnt1),FadeOut(pnt2),FadeOut(axes))
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
        notice_part3 = Text("处的值",font="Microsoft YaHei",font_size=20).next_to(notice_part2,buff=0.05)
        notice = VGroup(
            notice_part1,
            notice_part2,
            notice_part3
        )
        self.play(FadeIn(arr1),FadeIn(arr2),Write(notice))
        self.wait()
        self.play(FadeOut(polyA),FadeOut(polyA0),FadeOut(polyA1),FadeOut(polyrelation1),FadeOut(polyrelation2),FadeOut(arr1),FadeOut(arr2),FadeOut(notice))
        ##example
        example = Tex(r"A(x)=1+3x+2x^2+x^3").shift(3*UP)
        self.play(Write(example))
        self.wait()
        procedure1 = Tex(r"A^{[0]}(x)=1+2x").shift(2*UP)
        procedure2 = Tex(r"A^{[1]}(x)=3+x").shift(1*UP)
        self.play(Write(procedure1),Write(procedure2))
        self.wait()
        trans1 = Tex(r"A(x)=1+3x+2x^2+x^3=A^{[0]}(x^2)+xA^{[1]}(x^2)").shift(3*UP)
        self.play(TransformMatchingTex(example, trans1))
        procedure1_2 = Tex(r"A^{[0]}(x)=1+2x |_{x=4}").shift(2*UP)
        procedure2_2 = Tex(r"A^{[1]}(x)=3+x |_{x=4}").shift(1*UP)
        self.play(TransformMatchingTex(procedure1, procedure1_2),
                  TransformMatchingTex(procedure2, procedure2_2))
        self.wait()
        procedure3_1_1 = Tex(r"A^{{[0]}^{[0]}}(x) = 1")
        procedure3_1_2 = Tex(r"A^{{[0]}^{[1]}}(x) = 2").shift(1*DOWN)
        trans1_2 = Tex(r"A^{[0]}(x)=1+2x=A^{{[0]}^{[0]}}(x^2)+xA^{{[0]}^{[1]}}(x^2)").shift(2*UP)
        self.play(Write(procedure3_1_1),Write(procedure3_1_2))
        self.play(TransformMatchingTex(procedure1_2, trans1_2))
        procedure3_1 = Tex(r"A^{[0]}(4)=A^{{[0]}^{[0]}}(16)+4A^{{[0]}^{[1]}}(16)=1+4\cdot2=9").shift(2*UP)
        self.play(TransformMatchingTex(trans1_2, procedure3_1))
        self.play(FadeOut(procedure3_1_1),FadeOut(procedure3_1_2))
        self.wait()
        procedure3_2 = Tex(r"A^{[1]}(4)=A^{{[1]}^{[0]}}(16)+4A^{{[1]}^{[1]}}(16)=3+4\cdot1=7").shift(1*UP)
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
        self.play(FadeOut(example_regular2),FadeOut(result2),FadeOut(example_regular))
        ##further more
        self.play(result.animate.shift(-2*UP))
        self.play(FadeIn(procedure3_1),FadeIn(procedure3_2))
        procedure3_3 = Tex(r"A^{[0]}(-4)=A^{{[0]}^{[0]}}(16)-4A^{{[0]}^{[1]}}(16)=1-4\cdot2=-7").shift(1*DOWN)
        procedure3_4 = Tex(r"A^{[1]}(-4)=A^{{[1]}^{[0]}}(16)-4A^{{[1]}^{[1]}}(16)=3-4\cdot1=-1").shift(2*DOWN)
        note = Tex(r"x^2=-4").shift(3*DOWN+1.3*LEFT)
        note2 = Tex(r"x=\pm 2i").shift(3*DOWN+1.3*RIGHT)
        self.play(Write(procedure3_3),Write(procedure3_4))
        self.play(Write(note),Write(note2))
        self.wait()
        self.play(FadeOut(procedure3_1),FadeOut(procedure3_2),result.animate.shift(2*UP))
        result_3 = Tex(r"A(2i)=A^{[0]}(-4)+2iA^{[1]}(-4)=-7+2i\cdot(-1)=-7-2i").shift(UP)
        result_4 = Tex(r"A(-2i)=A^{[0]}(-4)-2iA^{[1]}(-4)=-7-2i\cdot(-1)=-7+2i")
        self.play(Write(result_3), Write(result_4))
        self.wait()
        self.play(FadeOut(procedure3_3),FadeOut(procedure3_4))
        self.play(result2.animate.shift(UP),result_3.animate.shift(DOWN),result_4.animate.shift(DOWN))
        self.play(FadeOut(note),FadeOut(note2),FadeOut(result2),FadeOut(result_3),FadeOut(result_4),FadeOut(result),FadeOut(trans1))
        ##how to choose proper x
        tree1 = VGroup(
            Tex(r"z_0").shift(0.2*UP),
            Arrow((0,0.2,0),(-2,1.3,0)),
            Arrow((0,0.2,0),(2,1.3,0)),
            Tex(r"-z_1").shift(-2*LEFT+1.3*UP),
            Tex(r"z_1").shift(2*LEFT+1.3*UP),
            Arrow((2,1.3,0),(3,2.5,0)),
            Arrow((2,1.3,0),(1,2.5,0)),
            Arrow((-2,1.3,0),(-1,2.5,0)),
            Arrow((-2,1.3,0),(-3,2.5,0)),
            Tex(r"z_2").shift(3*LEFT+2.5*UP),
            Tex(r"-z_2").shift(1*LEFT+2.5*UP),
            Tex(r"iz_2").shift(-1*LEFT+2.5*UP),
            Tex(r"-iz_2").shift(-3*LEFT+2.5*UP),
            Tex(r"iz_2").shift(-1*LEFT+2.5*UP),
            Tex(r"\cdots").shift(3*LEFT+3*UP),
            Tex(r"\cdots").shift(1*LEFT+3*UP),
            Tex(r"\cdots").shift(1*RIGHT+3*UP),
            Tex(r"\cdots").shift(3*RIGHT+3*UP)
        )
        self.play(Write(tree1))
        self.wait()
        Rectangle1 = Rectangle(width=6.4,height=2.7).shift(1.6*UP)
        bracex = Brace(Rectangle1, UP)
        labelx = TexText(r"$n$",t2c={r"$n$": BLUE}).next_to(bracex, UP,buff=0.04)
        bracey = Brace(Rectangle1, LEFT)
        labely = TexText(r"$\log_2n$",t2c={r"$\log_2n$": BLUE}).next_to(bracey, LEFT)
        self.play(Write(bracex),Write(labelx))
        self.wait()
        self.play(Write(bracey),Write(labely))
        self.wait()
        formula = Tex(r"z^n=z_0").shift(0.6*DOWN+2*LEFT)
        assumption = Tex(r"z=re^{i\theta},\quad z_0=r_0e^{i\theta_0}").shift(0.6*DOWN+2*RIGHT)
        self.play(Write(formula))
        self.wait()
        self.play(Write(assumption))
        self.wait()
        tui = Tex(r"\left\{\begin{matrix} r^n=r_0\\ n\theta=\theta_0+2k\pi,k\in \mathbb Z\end{matrix}\right.").shift((0,-1.6,0))
        self.play(Write(tui))
        self.wait()
        tui_2 = Tex(r"\left\{\begin{matrix} r^n=r_0\\ n\theta=\theta_0+2k\pi,k\in \mathbb Z\end{matrix}\right.\Rightarrow \left\{\begin{matrix} r=\sqrt[n]{r_0} \\ \theta=\frac{\theta_0}{n}+\frac{2\pi}{n}\cdot k,k\in \mathbb Z\end{matrix}\right.").shift((0,-1.6,0))
        self.play(TransformMatchingTex(tui, tui_2))
        self.wait()
        conclution = Tex(r"z=z'\cdot \omega_n^k,\quad z'=\sqrt[n]{r_0}e^{i\frac{\theta_0}{n}}").shift((-2.5,-2.8,0))
        self.play(Write(conclution))
        self.wait()
        bufang = Tex(r"z'=1,\quad z=\omega_n^k").shift((3,-2.8,0))
        self.play(Write(bufang))
        self.wait()
        self.play(FadeOut(tree1),FadeOut(bracex),FadeOut(labelx),FadeOut(bracey),
                  FadeOut(labely),FadeOut(formula),FadeOut(assumption),FadeOut(tui_2),
                  FadeOut(bufang),FadeOut(conclution))
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
        etcs = [Tex(r"\vdots").shift((1.05*(i-4)+0.5025,-0.5,0)) for i in range(8)]
        self.play(FadeIn(arr2_1),FadeIn(arr2_2),FadeIn(arr2_3),FadeIn(arr2_4),FadeIn(arr3_1),FadeIn(arr3_2),
                  Write(etc1),Write(etc2),Write(etc3),Write(A_0_0),*[Write(etcs[i]) for i in range(8)])
        time_limit = Tex(r"FFT(n)=2FFT(\frac{n}{2})+c\cdot n,c\in\mathbb{R}^+",font_size=34).shift(2.1*DOWN)
        self.play(Write(time_limit))
        rec1 = Rectangle(width=1.6,height=0.8,color=GREEN).shift((-0.25,-2.1,0))
        rec2 = Rectangle(width=0.7,height=0.4,color=BLUE).shift((1.2,-2.1,0))
        self.play(ShowCreation(rec1))
        self.wait()
        self.play(ShowCreation(rec2))
        self.wait()
        self.play(FadeOut(rec1),FadeOut(rec2))
        ##solve
        condition1 = Tex(r"FFT(1)=O(1)",font_size=34).shift(2.6*DOWN)
        self.play(Write(condition1))
        labels = [Tex(r"O(1)",font_size=34).shift((1.05*(i-4)+0.5025,-1,0)) for i in range(8)]
        self.play(*[Write(labels[i]) for i in range(8)])
        self.wait()
        bracey = Brace(VGroup(*labels),DOWN,buff=0.01)
        labely = Tex(r"n",font_size=34).next_to(bracey,DOWN,buff=0.01)
        self.play(Write(bracey),Write(labely))
        conclusion = Tex(r"FFT(n)=O(n)+\dots",font_size=34).shift(3*DOWN)
        self.play(Write(conclusion))
        ##merge
        arr_UP1 = Arrow((0.15,1.7,0),(0.15,2.8,0),fill_color=YELLOW)
        label1 = Tex(r"c\cdot n",font_size=30).shift(0.2*LEFT+2.2*UP)
        self.play(Write(label1),FadeIn(arr_UP1))
        arr_UP2 = Arrow((-1.8,0.2,0),(-1.8,1.4,0),fill_color=YELLOW)
        label2 = Tex(r"c\cdot \frac{n}{2}",font_size=30).shift(2.15*LEFT+0.8*UP)
        arr_UP3 = Arrow((2.2,0.2,0),(2.2,1.4,0),fill_color=YELLOW)
        label3 = Tex(r"c\cdot \frac{n}{2}",font_size=30).shift(1.85*RIGHT+0.8*UP)
        self.play(Write(label2),FadeIn(arr_UP2),Write(label3),FadeIn(arr_UP3))
        self.wait()
        label2_trans1 = Tex(r"\frac{cn}{2}\cdot2=cn",font_size=34).shift(4.7*RIGHT+0.8*UP)
        label2_trans3 = Tex(r"\frac{cn}{4}\cdot4=cn",font_size=34).shift(4.7*RIGHT)
        label2_trans2 = Tex(r"cn\cdot 1=cn",font_size=34).shift(4.7*RIGHT+2.3*UP)
        self.play(Write(label2_trans1))
        self.wait()
        self.play(Write(label2_trans2), Write(label2_trans3))
        rec = Rectangle(width=11.3,height=5.2,color=RED).shift((0,0.9,0))
        self.play(ShowCreation(rec))
        brace = Brace(rec,LEFT,buff=0.01)
        label = Tex(r"\log n",font_size=34).next_to(brace,LEFT,buff=0.01)
        self.play(Write(brace),Write(label))
        self.wait()
        ##conclusion
        conclusion1 = Tex(r"FFT(n)=O(n)+c\cdot n\log n",font_size=34).shift(3*DOWN)
        self.play(TransformMatchingTex(conclusion, conclusion1))
        conclusion2 = Tex(r"FFT(n)=O(n)+c\cdot n\log n=O(n\log n)",font_size=34).shift(3*DOWN)
        self.play(TransformMatchingTex(conclusion1, conclusion2))
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
        complex_num = Tex(r"z =\frac{3}{2} + 2i,\quad  i=\sqrt{-1}").shift(2.5*UP+2.5*RIGHT)
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
        labelx = TexText(r"$ \cos\theta $ = 1.00",t2c={
            r"\cos\theta": BLUE
        }).shift(UP+2*LEFT)
        numberx = labelx.make_number_changeable("1.00")
        numberx.f_always.set_value(lambda : np.cos(theta.get_value()))
        labely = TexText(r"$ \sin\theta $ = 0.00",t2c={
            r"\sin\theta": RED
        }).shift(UP+2*RIGHT)
        numbery = labely.make_number_changeable("0.00")
        numbery.f_always.set_value(lambda : np.sin(theta.get_value()))
        circle = Circle(stroke_color=GREEN)
        self.play(Write(circle),Write(formula),self.camera.frame.animate.set_width(8))
        self.play(FadeIn(arrow),FadeIn(proj_x),FadeIn(proj_x2),FadeIn(proj_y),FadeIn(proj_y2),FadeIn(labelx),FadeIn(labely))
        self.play(theta.animate.set_value(2*PI), run_time=4, rate_func=linear)
        self.play(FadeOut(arrow),FadeOut(proj_x),FadeOut(proj_x2),FadeOut(proj_y),FadeOut(proj_y2),
                  FadeOut(theta),FadeOut(labelx),FadeOut(labely),FadeOut(arrow))
        self.play(self.camera.frame.animate.set_width(14.222222),FadeOut(formula),FadeOut(plane.coordinate_labels))
        ##danweigen definition
        definition1 = Tex(r"z^n=1").shift(2*UP+3*RIGHT)
        assumption = Tex(r"z=re^{i\theta},r > 0").shift(1*UP+3*RIGHT)
        p1 = Tex(r"z^n=r^ne^{in\theta}=1").shift(3.5*RIGHT)
        conclution = Tex(r"\left\{\begin{matrix}r=1\\\theta = \frac{2k\pi}{n},\quad k\in\{0,1,\dots,n-1\}\end{matrix}\right.").shift(2.5*DOWN+2.5*RIGHT)
        n=8
        niseight = Tex("n=8=2^3").shift(2*UP+2.2*LEFT)
        roots = [np.exp(1j * 2 * PI * k / n) for k in range(n)]
        dots = [Dot(plane.n2p(root), fill_color=YELLOW) for root in roots]
        labels = [Tex(r"\omega_n"+(r"^"+str(i%8) if i !=1 else r"")).next_to(dots[i%8],direction=plane.n2p(np.exp(1j*2*PI/n*i))) for i in range(n)]
        self.play(Write(definition1))
        self.play(Write(assumption))
        self.play(Write(p1))
        self.play(Write(conclution))
        self.wait()
        self.play(Write(niseight))
        self.play(*[FadeIn(dot) for dot in dots],*[Write(label) for label in labels])
        self.wait()
        self.play(FadeOut(definition1),FadeOut(assumption),FadeOut(p1),FadeOut(conclution))
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
        polyA0.shift(0.8*DOWN)
        polyA1.shift(0.8*DOWN)
        self.play(Write(polyA0),Write(polyA1))
        self.wait()
        A0 = Tex(r"A^{[0]}(\omega_{\frac{n}{2}}^k)").shift(1.8*DOWN+3*LEFT)
        A1 = Tex(r"A^{[1]}(\omega_{\frac{n}{2}}^k)").shift(1.8*DOWN+1*LEFT)
        label = Text("这两个多项式的项数都折半\n同时单位根的次数也对应折半\n递归求解",font_size=18,font="Microsoft YaHei").shift(1.8*DOWN+4*RIGHT)
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
        ##proof
        self.play(NiJuZhen.animate.shift(2.7*UP))
        condition = Tex(r"(F_n)_{j,k} = \omega_n^{j \cdot k}  ,\quad(F_n^{-1})_{j,k} = \frac{1}{n} \omega_n^{-j \cdot k},\quad 0 \leq j,k \leq n-1",font_size=32).shift(UP)
        self.play(Write(condition))
        self.wait()
        lines = VGroup(
            Tex(r"(F_nF_n^{-1})_{j,k}=\sum_{i=0}^{n-1}\omega_n^{ji}\frac{1}{n}\omega_n^{-ik}",font_size=32),
            Tex(r"(F_nF_n^{-1})_{j,k}=\sum_{i=0}^{n-1}\omega_n^{ji}\frac{1}{n}\omega_n^{-ik}=\frac{1}{n}\sum_{i=0}^{n-1}\omega_n^{i(j-k)}",font_size=32)
        )
        self.play(Write(lines[0]))
        self.wait()
        self.play(TransformMatchingTex(lines[0], lines[1]))
        self.wait()
        lines_j_equal_k = VGroup(
            Tex(r"j=k \Rightarrow (F_nF_n^{-1})_{j,k}=\frac{1}{n}\sum_{i=0}^{n-1}\omega_n^{0}",font_size=32).shift(DOWN),
            Tex(r"j=k \Rightarrow (F_nF_n^{-1})_{j,k}=\frac{1}{n}\sum_{i=0}^{n-1}\omega_n^{0}=\frac{1}{n}\cdot n=1",font_size=32).shift(DOWN)
        )
        self.play(Write(lines_j_equal_k[0]))
        self.wait()
        self.play(TransformMatchingTex(lines_j_equal_k[0], lines_j_equal_k[1]))
        self.wait()
        ##test
        lines_j_not_equal_k = VGroup(
            Tex(r"j\neq k \Rightarrow (F_nF_n^{-1})_{j,k}=\frac{1}{n}\sum_{i=0}^{n-1}\omega_n^{i(j-k)}",font_size=32).shift(2*DOWN),
            Tex(r"j\neq k \Rightarrow (F_nF_n^{-1})_{j,k}=\frac{1}{n}\sum_{i=0}^{n-1}\omega_n^{i(j-k)}=\frac{1}{n}\frac{\omega_n^{n(j-k)}-1}{\omega_n^{j-k}-1}",font_size=32).shift(2*DOWN),
            Tex(r"j\neq k \Rightarrow (F_nF_n^{-1})_{j,k}=\frac{1}{n}\sum_{i=0}^{n-1}\omega_n^{i(j-k)}=\frac{1}{n}\frac{e^{i\frac{2\pi}{n}\cdot n(j-k)}-1}{\omega_n^{j-k}-1}",font_size=32).shift(3*DOWN),
            Tex(r"j\neq k \Rightarrow (F_nF_n^{-1})_{j,k}=\frac{1}{n}\sum_{i=0}^{n-1}\omega_n^{i(j-k)}=\frac{1}{n}\frac{e^{i\frac{2\pi}{n}\cdot n(j-k)}-1}{\omega_n^{j-k}-1}=\frac{1}{n}\frac{1-1}{\omega_n^{j-k}-1}=0",font_size=32).shift(3*DOWN)
        )
        self.play(Write(lines_j_not_equal_k[0]))
        self.wait()
        notice = Tex(r"(j-k)\in[-(n-1),n-1] \setminus \{0\}\Rightarrow n\nmid(j-k)\Rightarrow \omega_n^{j-k}\neq1",font_size=32).shift(3*DOWN)
        self.play(Write(notice))
        self.play(TransformMatchingTex(lines_j_not_equal_k[0], lines_j_not_equal_k[1]))
        self.wait()
        self.play(FadeOut(notice))
        self.play(TransformMatchingTex(lines_j_not_equal_k[1].copy(), lines_j_not_equal_k[2]))
        self.wait()
        self.play(TransformMatchingTex(lines_j_not_equal_k[2], lines_j_not_equal_k[3]))
        self.wait()
        self.play(FadeOut(NiJuZhen),FadeOut(condition),FadeOut(lines[1]),FadeOut(lines_j_equal_k[1]),FadeOut(lines_j_not_equal_k[1]),FadeOut(lines_j_not_equal_k[3]))
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
        ##sum up
        lines = VGroup(
            Tex(r"(1+2x)(3+4x)=3+10x+8x^2",font_size=30).shift(4.2*LEFT),
            Tex(r"(1+20)(3+40)=3+10\times10+8\times10^2",font_size=30).shift(RIGHT),
            Tex(r"21\times 43=903",font_size=30).shift(4.9*RIGHT)
        )
        self.play(Write(lines[0]))
        self.wait()
        self.play(TransformMatchingTex(lines[0].copy(), lines[1]))
        self.wait()
        self.play(TransformMatchingTex(lines[1].copy(), lines[2]))
        self.wait()
        special_use1 = Tex(r"\frac{1}{\sqrt n}\begin{bmatrix}  1&  1&  1&  1& \dots& 1\\  1&  \omega_n&  \omega_n^2&  \omega_n^3&  \dots& \omega_n^{n-1}\\  1&  \omega_n^2&  \omega_n^4&  \omega_n^6&  \dots& \omega_n^{2(n-1)}\\  1&  \omega_n^3&  \omega_n^6&  \omega_n^9&  \dots& \omega_n^{3(n-1)}\\  \vdots&  \vdots&  \vdots&  \vdots&  \ddots & \vdots \\  1&  \omega_n^{(n-1)}&  \omega_n^{2(n-1)}&  \omega_n^{3(n-1)}&  \dots& \omega_n^{(n-1)(n-1)}\end{bmatrix}",font_size=24).shift(1.7*DOWN+3.5*LEFT)
        special_use2 = Tex(r"\frac{1}{\sqrt n}\begin{bmatrix}1 & 1 & 1 & 1 & \cdots & 1 \\1 & \omega_n^{-1} & \omega_n^{-2} & \omega_n^{-3} & \cdots & \omega_n^{-(n-1)} \\1 & \omega_n^{-2} & \omega_n^{-4} & \omega_n^{-6} & \cdots & \omega_n^{-2(n-1)} \\1 & \omega_n^{-3} & \omega_n^{-6} & \omega_n^{-9} & \cdots & \omega_n^{-3(n-1)} \\\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\1 & \omega_n^{-(n-1)} & \omega_n^{-2(n-1)} & \omega_n^{-3(n-1)} & \cdots & \omega_n^{-(n-1)(n-1)}\end{bmatrix}",font_size=24).shift(1.7*DOWN+3.5*RIGHT)
        self.play(Write(special_use1),Write(special_use2))
        self.wait()
        juanjidingli = Tex(r"a\otimes b=DFT^{-1}_{2n}(DFT_{2n}(a)\cdot DFT_{2n}(b))",font_size=32).shift(3.5*DOWN)
        self.play(Write(juanjidingli))
        self.wait()