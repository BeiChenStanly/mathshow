from manimlib import *

class UpdatersExample(Scene):
    def construct(self):
        ##test
        rec = Rectangle(height=2, width=3, color=BLUE).shift(LEFT)
        bracex = Brace(rec, UP)
        bracey = Brace(rec, RIGHT)
        self.add(rec, bracex, bracey)