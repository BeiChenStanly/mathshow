from manimlib import *
import numpy as np

class DotScene(InteractiveScene):
    def construct(self):
        ##write polies
        polies = VGroup( Tex(r"x^3+x^2+x-1").shift(3.5*UP+0.4*RIGHT),
                       Tex(r"-x^3-2x^2+2x+2").shift(2.8*UP)
                       )
        self.play(Write(polies))
        self.wait()
        procedure = VGroup(Line(start=5.8*LEFT,end=2*RIGHT).shift(2.5*UP),
                           Tex(r"2x^3+2x^2+2x-2").shift(2.2*UP),
                           Tex(r"2x^4+2x^3+2x^2-2x").shift(1.6*UP+1.1*LEFT),
                           Tex(r"-2x^5-2x^4-2x^3+2x^2").shift(0.9*UP+2.5*LEFT),
                           Tex(r"-x^6-x^5-x^4+x^3").shift(0.3*UP+3.6*LEFT),
                           Line(start=5.8*LEFT,end=2*RIGHT),
                           Tex(r"-x^6-3x^5-x^4+3x^3+6x^2+0x-2").shift(0.5*DOWN+1.9*LEFT)
                           )
        self.play(Write(procedure))
        self.wait()
        tongshi = Tex(r"\sum_{n = 0}^{N-1}{a_nx^n}\cdot \sum_{n = 0}^{N-1}{b_nx^n} = \sum_{n = 0}^{2N-2}{(\sum_{i = 0}^{n}a_ib_{n-i})\cdot x^i}").shift(2*DOWN)
        self.play(Write(tongshi))
        self.wait()
        on_2=Tex(r"O(N^2)").shift(3.5*DOWN)
        self.play(FadeIn(on_2))
        self.wait()
        self.play(FadeOut(polies),FadeOut(procedure),FadeOut(tongshi),FadeOut(on_2))
        ##dot expression
        xishushi = Tex(r"\sum_{i = 0}^{n-1}{a_ix^i}").shift(3*UP+2.5*LEFT)
        dots = Tex(r"(x_0,y_0),(x_1,y_1),\cdots,(x_{n-1},y_{n-1})").shift(3*UP+2.5*RIGHT)
        self.play(Write(xishushi))
        self.wait()
        self.play(Write(dots))
        self.wait()
        dotexpression = Tex(r"\begin{bmatrix} 1 & x_0 & x_0^2 & \cdots & x_0^{n-1} \\ 1 & x_1 & x_1^2 & \cdots & x_1^{n-1} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n-1} & x_{n-1}^2 & \cdots & x_{n-1}^{n-1} \end{bmatrix}",r"\begin{bmatrix} a_0\\a_1\\ \vdots \\a_{n-1} \end{bmatrix}=",r"\begin{bmatrix} y_0\\y_1\\ \vdots \\ y_{n-1} \end{bmatrix}")
        self.play(Write(dotexpression))
        hanglieshi = Tex(r" \prod_{0 \leq i < j \leq n-1} (x_j - x_i)").shift(2.5*DOWN)
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
        poly1 = Tex(r"\sum_{n = 0}^{N-1}{a_nx^n}").shift(3*UP+2*LEFT)
        poly2 = Tex(r"\sum_{n = 0}^{N-1}{b_nx^n}").shift(3*UP+2*RIGHT)
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
        result = Tex(r"\sum_{n = 0}^{2N-1}{c_nx^n}").shift(2.5*DOWN)
        self.play(FadeIn(arr),Write(result))
        self.wait()
        o_n = Tex(r"O(N)").shift(0.7*UP)
        self.play(FadeIn(o_n))
        self.wait()
        o_nlogn_1 = Tex(r"O(NlogN)").shift(3.7*RIGHT+2.2*UP)
        o_nlogn_2 = Tex(r"O(NlogN)").shift(1.5*RIGHT+1*DOWN)
        self.play(FadeIn(o_nlogn_1),FadeIn(o_nlogn_2))
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
        notice = Text("递归不成立",font="Maple Mono NF CN").shift(-2.8*UP+1*RIGHT)
        self.play(FadeIn(arr1),FadeIn(arr2),Write(notice))
        self.wait()
        self.play(FadeOut(polyA),FadeOut(polyA0),FadeOut(polyA1),FadeOut(polyrelation1),
                  FadeOut(polyrelation2),FadeOut(arr1),FadeOut(arr2),FadeOut(notice))
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
        # ##oler's formula
        # theta = ValueTracker(0)
        # formula = Tex(r"e^{i\theta} = \cos\theta + i\sin\theta",tex_to_color_map={r"\cos\theta": BLUE,r"\sin\theta": RED}).shift(1.5*UP+2*RIGHT)
        # arrow = always_redraw(lambda: Arrow(ORIGIN, plane.n2p(np.exp(1j*theta.get_value())),fill_color=YELLOW,buff=0))
        # proj_x = always_redraw(lambda: Line(ORIGIN, plane.c2p(np.cos(theta.get_value()),0), color=BLUE))
        # proj_x2 = always_redraw(lambda: DashedLine(plane.c2p(np.cos(theta.get_value()),0),plane.n2p(np.exp(1j*theta.get_value()))))
        # proj_y = always_redraw(lambda: Line(ORIGIN, plane.c2p(0,np.sin(theta.get_value())),color=RED))
        # proj_y2 = always_redraw(lambda: DashedLine(plane.c2p(0,np.sin(theta.get_value())),plane.n2p(np.exp(1j*theta.get_value()))))
        # labelx = TexText(r"$ \cos\theta $ = 1.00")
        # bracex = always_redraw(Brace, proj_x, DOWN)
        # labelx.always.next_to(bracex, DOWN)
        # numberx = labelx.make_number_changeable("1.00")
        # numberx.f_always.set_value(lambda : np.cos(theta.get_value()))
        # labely = TexText(r"$ \sin\theta $ = 0.00")
        # bracey = always_redraw(Brace, proj_y,  LEFT)
        # labely.always.next_to(bracey, LEFT)
        # numbery = labely.make_number_changeable("0.00")
        # numbery.f_always.set_value(lambda : np.sin(theta.get_value()))
        circle = Circle(stroke_color=GREEN)
        self.play(Write(circle),FadeOut(plane.coordinate_labels))
        # self.play(Write(circle),Write(formula),self.camera.frame.animate.set_width(8))
        # self.play(FadeIn(arrow),FadeIn(proj_x),FadeIn(proj_x2),FadeIn(proj_y),FadeIn(proj_y2),FadeIn(bracex),FadeIn(bracey),FadeIn(labelx),FadeIn(labely))
        # self.play(theta.animate.set_value(2*PI), run_time=8, rate_func=linear)
        # self.play(FadeOut(arrow),FadeOut(proj_x),FadeOut(proj_x2),FadeOut(proj_y),FadeOut(proj_y2),
        #           FadeOut(theta),FadeOut(bracex),FadeOut(labelx),FadeOut(bracey),FadeOut(labely),FadeOut(arrow))
        # self.play(self.camera.frame.animate.set_width(14.222222),FadeOut(formula),FadeOut(plane.coordinate_labels))
        ##danweigen definition
        definition1 = Tex("z^n=1").shift(2*UP+2*RIGHT)
        n=8
        niseight = Tex("n=8").shift(2*UP+2.2*LEFT)
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
        n2isfour=Tex(r"\frac{n}{2} = 4").shift(2.8*LEFT+0.7*UP)
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
        A0 = Tex(r"A^{[0]}(\omega_{\frac{n}{2}}^k)").shift(1.6*DOWN+3*LEFT)
        A1 = Tex(r"A^{[1]}(\omega_{\frac{n}{2}}^k)").shift(1.6*DOWN+1*LEFT)
        label = Text("这两个都是次数折半的多项式\n同时单位根的次数也对应折半\n递归成立",font_size=18,font="Microsoft YaHei").shift(1.6*DOWN+4*RIGHT)
        arr  = Arrow(A1.get_right(),label.get_left())
        self.play(Write(A0),Write(A1))
        self.play(FadeIn(arr),Write(label))
        time_limit = Tex(r"FFT(n)=2FFT(\frac{n}{2})+\Theta(n)=\Theta(n\log n)").shift(3*DOWN)
        self.play(Write(time_limit))
        self.wait()

class IDFTScene(InteractiveScene):
    def construct(self):
        ##draw idft
        formula1 = Tex(r"\begin{bmatrix}  1&  1&  1&  1& \dots& 1\\  1&  \omega_n&  \omega_n^2&  \omega_n^3&  \dots& \omega_n^{n-1}\\  1&  \omega_n^2&  \omega_n^4&  \omega_n^6&  \dots& \omega_n^{2(n-1)}\\  1&  \omega_n^3&  \omega_n^6&  \omega_n^9&  \dots& \omega_n^{3(n-1)}\\  \vdots&  \vdots&  \vdots&  \vdots&  \ddots & \vdots \\  1&  \omega_n^{(n-1)}&  \omega_n^{2(n-1)}&  \omega_n^{3(n-1)}&  \dots& \omega_n^{(n-1)(n-1)}\end{bmatrix}\begin{bmatrix} a_0\\ a_1\\ a_2\\ a_3\\ \vdots\\a_{n-1}\end{bmatrix}=\begin{bmatrix} y_0\\ y_1\\ y_2\\ y_3\\ \vdots\\y_{n-1}\end{bmatrix}",font_size=32).shift(2*UP)
        self.play(Write(formula1))
        calculate_A = Tex(r"\begin{bmatrix} a_0\\ a_1\\ a_2\\ a_3\\ \vdots\\a_{n-1}\end{bmatrix}=\begin{bmatrix}  1&  1&  1&  1& \dots& 1\\  1&  \omega_n&  \omega_n^2&  \omega_n^3&  \dots& \omega_n^{n-1}\\  1&  \omega_n^2&  \omega_n^4&  \omega_n^6&  \dots& \omega_n^{2(n-1)}\\  1&  \omega_n^3&  \omega_n^6&  \omega_n^9&  \dots& \omega_n^{3(n-1)}\\  \vdots&  \vdots&  \vdots&  \vdots&  \ddots & \vdots \\  1&  \omega_n^{(n-1)}&  \omega_n^{2(n-1)}&  \omega_n^{3(n-1)}&  \dots& \omega_n^{(n-1)(n-1)}\end{bmatrix}^{-1}\begin{bmatrix} y_0\\ y_1\\ y_2\\ y_3\\ \vdots\\y_{n-1}\end{bmatrix}",font_size=32).shift(2*UP)
        self.play(TransformMatchingTex(formula1, calculate_A,
                                       key_map={
                                           r"\begin{bmatrix} a_0\\ a_1\\ a_2\\ a_3\\ \vdots\\a_{n-1}\end{bmatrix}":r"\begin{bmatrix} a_0\\ a_1\\ a_2\\ a_3\\ \vdots\\a_{n-1}\end{bmatrix}",
                                           r"\begin{bmatrix} y_0\\ y_1\\ y_2\\ y_3\\ \vdots\\y_{n-1}\end{bmatrix}":r"\begin{bmatrix} y_0\\ y_1\\ y_2\\ y_3\\ \vdots\\y_{n-1}\end{bmatrix}",
                                       }))
        self.wait()
        NiJuZhen = Tex(r"\begin{bmatrix}  1&  1&  1&  1& \dots& 1\\  1&  \omega_n&  \omega_n^2&  \omega_n^3&  \dots& \omega_n^{n-1}\\  1&  \omega_n^2&  \omega_n^4&  \omega_n^6&  \dots& \omega_n^{2(n-1)}\\  1&  \omega_n^3&  \omega_n^6&  \omega_n^9&  \dots& \omega_n^{3(n-1)}\\  \vdots&  \vdots&  \vdots&  \vdots&  \ddots & \vdots \\  1&  \omega_n^{(n-1)}&  \omega_n^{2(n-1)}&  \omega_n^{3(n-1)}&  \dots& \omega_n^{(n-1)(n-1)}\end{bmatrix}^{-1}=\frac{1}{n}\begin{bmatrix}1 & 1 & 1 & 1 & \cdots & 1 \\1 & \omega_n^{-1} & \omega_n^{-2} & \omega_n^{-3} & \cdots & \omega_n^{-(n-1)} \\1 & \omega_n^{-2} & \omega_n^{-4} & \omega_n^{-6} & \cdots & \omega_n^{-2(n-1)} \\1 & \omega_n^{-3} & \omega_n^{-6} & \omega_n^{-9} & \cdots & \omega_n^{-3(n-1)} \\\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\1 & \omega_n^{-(n-1)} & \omega_n^{-2(n-1)} & \omega_n^{-3(n-1)} & \cdots & \omega_n^{-(n-1)(n-1)}\end{bmatrix}",font_size=24).shift(0.5*DOWN)
        self.play(Write(NiJuZhen))
        self.wait()
        calculate_A2 = Tex(r"\begin{bmatrix} a_0 \\ a_1 \\ a_2 \\ a_3 \\ \vdots \\ a_{n-1} \end{bmatrix} = \frac{1}{n}\begin{bmatrix}1 & 1 & 1 & 1 & \cdots & 1 \\1 & \omega_n^{-1} & \omega_n^{-2} & \omega_n^{-3} & \cdots & \omega_n^{-(n-1)} \\1 & \omega_n^{-2} & \omega_n^{-4} & \omega_n^{-6} & \cdots & \omega_n^{-2(n-1)} \\1 & \omega_n^{-3} & \omega_n^{-6} & \omega_n^{-9} & \cdots & \omega_n^{-3(n-1)} \\\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\1 & \omega_n^{-(n-1)} & \omega_n^{-2(n-1)} & \omega_n^{-3(n-1)} & \cdots & \omega_n^{-(n-1)(n-1)}\end{bmatrix}\begin{bmatrix} y_0 \\ y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_{n-1} \end{bmatrix}",font_size=32,
                           t2c={
                               r"\frac{1}{n}": RED,
                               r"-":BLUE,
                               r"n-1":WHITE
                           }).shift(-2*DOWN)
        self.play(TransformMatchingTex(calculate_A,calculate_A2))
class SumUpScene(InteractiveScene):
    def construct(self) :
        pass #TODO: Add a summary scene