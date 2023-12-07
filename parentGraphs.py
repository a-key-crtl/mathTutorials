from manim import *
import math


class parentFunctions(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-6,6,1],
            y_range=[-4,4,1],
            axis_config={"color": BLUE}
        )
        axes.add_coordinates()
        
        axes2 = Axes(
            x_range=[0,6,1],
            y_range=[-4,4,1],
            axis_config={"color": BLUE}
        )
        axes2.add_coordinates()
        
        graph = axes.plot(lambda x: x, color=WHITE)
        graph_label = axes.get_graph_label(graph, label="y = x")
        
        graph2 = axes.plot(lambda x: x**2, color=WHITE)
        graph_label2 = axes.get_graph_label(graph2, label="y = x^{2}")
        
        graph3 = axes.plot(lambda x: x**3, color=WHITE)
        graph_label3 = axes.get_graph_label(graph3, label="y = x^{3}")
        
        graph4 = axes.plot(lambda x: abs(x), color=WHITE)
        graph_label4 = axes.get_graph_label(graph4, label=Tex("$y = |x|$"))
       
        graph5 = axes2.plot(lambda x: math.sqrt(x), color=WHITE)
        graph_label5 = axes2.get_graph_label(graph5, label=Tex("$y = \sqrt{x}$")).shift(UP)
        
        graph6 = axes.plot(lambda x: 2**x, color=WHITE)
        graph_label6 = axes.get_graph_label(graph6, label=Tex("$y = b^x $"))
        
        
        
        firstLine = Text("Parent function: most basic function", t2c = {"Parent function": BLUE}, disable_ligatures=True,)
        secondLine = Text("Transformation: changes in size, shape, or orientation" , t2c={"Transformation": BLUE}, disable_ligatures=True, ).scale(0.7)
        g = Text("Linear", color=GREEN).to_corner(DR)
        g2 = Text("Quadratic", color=GREEN).to_corner(DR)
        g3 = Text("Cubic", color=GREEN).to_corner(DR)
        g4 = Text("Absolute value", color=GREEN).to_corner(DR)
        g5 = Text("Square root", color=GREEN).to_corner(DR)
        g6 = Text("Exponential", color=GREEN).to_corner(DR)
        
        gDom = Tex("$Domain: (-\infty, +\infty)$", color=YELLOW).next_to(graph_label, DOWN * 3).scale(0.6).shift(LEFT)
        gRan = Tex("$Range: (-\infty, +\infty)$", color=YELLOW).next_to(gDom, DOWN).scale(0.6).shift(LEFT)
        
        g2Dom = Tex("$Domain: (-\infty, +\infty)$", color=YELLOW).next_to(graph_label2, DOWN * 3).scale(0.6)
        g2Ran = Tex("$Range: [0, +\infty)$", color=YELLOW).next_to(g2Dom, DOWN).scale(0.6)
        
        g3Dom = Tex("$Domain: (-\infty, +\infty)$", color=YELLOW).next_to(graph_label3, DOWN * 3).scale(0.6).shift(RIGHT)
        g3Ran = Tex("$Range: (-\infty, +\infty)$", color=YELLOW).next_to(g3Dom, DOWN).scale(0.6).shift(RIGHT)
        
        g4Dom = Tex("$Domain: (-\infty, +\infty)$", color=YELLOW).next_to(graph_label4, DOWN * 3).scale(0.6).shift(LEFT)
        g4Ran = Tex("$Range: [0, +\infty)$", color=YELLOW).next_to(g4Dom, DOWN).scale(0.6).shift(LEFT)
        
        g5Dom = Tex("$Domain: [0, +\infty)$", color=YELLOW).next_to(graph_label5, DOWN * 4).scale(0.6)
        g5Ran = Tex("$Range: [0, +\infty)$", color=YELLOW).next_to(g5Dom, DOWN).scale(0.6)
        
        g6Dom = Tex("$Domain: (-\infty, +\infty)$", color=YELLOW).next_to(graph_label6, DOWN * 3).scale(0.6).shift(DOWN)
        g6Ran = Tex("$Range: (0, +\infty)$", color=YELLOW).next_to(g6Dom, DOWN).scale(0.6)
        
        secondLine.next_to(firstLine, DOWN, buff = 1)
        self.wait(10)
        self.play(Write(firstLine))
        self.wait(10)
        self.play(Write(secondLine))
        self.wait(10)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)
        self.play(Create(axes), Create(graph),  Write(graph_label), Write(g), Write(gDom), Write(gRan))
        self.wait(10)
        self.play(Transform(graph, graph2), Transform(graph_label, graph_label2), Transform(g, g2), Transform(gDom, g2Dom), Transform(gRan, g2Ran))
        self.wait(15)
        self.play(Transform(graph, graph3), Transform(graph_label, graph_label3), Transform(g, g3), Transform(gDom, g3Dom), Transform(gRan, g3Ran))
        self.wait(10)
        self.play(Transform(graph, graph4), Transform(graph_label, graph_label4), Transform(g, g4), Transform(gDom, g4Dom), Transform(gRan, g4Ran))
        self.wait(10)
        self.play(Transform(graph, graph6), Transform(graph_label, graph_label6), Transform(g, g6), Transform(gDom, g6Dom), Transform(gRan, g6Ran))
        self.wait(10)
        self.play(Transform(axes, axes2), Transform(graph, graph5), Transform(graph_label, graph_label5), Transform(g, g5), Transform(gDom, g5Dom), Transform(gRan, g5Ran))
        self.wait(20)
        
        
        