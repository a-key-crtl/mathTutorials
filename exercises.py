from manim import *
import math

class exercises(Scene):
    def construct(self):
        
        
        axes = Axes(
            x_range=[-16,16,4],
            y_range=[-16,16,4],
            axis_config={"color": BLUE}
        )
        axes.add_coordinates()
        
        
        graphx = axes.plot(lambda x: x**2, color=WHITE)
        graph_labelx = axes.get_graph_label(graphx, label="y = x^{2}")
        
        
        
        graph = axes.plot(lambda x: abs(x), color=WHITE)
        graph_label = axes.get_graph_label(graph, label=Tex("$y = |x|$")).shift(DOWN)
        graph.save_state()
        graph_label.save_state()
        graph1 = axes.plot(lambda x: abs(x + 4), color=WHITE)
        graph_label1 = axes.get_graph_label(graph1, label=Tex("$y = |x + 4|$")).shift(DOWN)
        graph2 = axes.plot(lambda x: -(abs(x + 4)), color=WHITE)
        graph_label2 = axes.get_graph_label(graph2, label=Tex("$y = -|x + 4|$")).shift(UP)
        graph3 = axes.plot(lambda x: -(abs(x + 4)) - 7, color=WHITE)
        graph_label3 = axes.get_graph_label(graph3, label=Tex("$y = -|x + 4| - 7$")).shift(UP)
        
        
        trans = Text("EX: Describe the transformation").to_edge(UP, buff=1.5).scale(0.8)
        
        trans1 = Tex("$y = -|x + 4| - 7$").next_to(trans, DOWN)
        trans1a = Tex("$y = |x|$").next_to(trans1, DOWN)
        a1 = Text("Parent function", color=RED).next_to(trans1a, LEFT).scale(0.5)
        trans1b = MathTex(r"y = |x + 4|", substrings_to_isolate="+ 4").next_to(trans1a,DOWN)
        trans1b.set_color_by_tex("+ 4",GREEN)
        b1 = Text("Shift LEFT 4 units", color=GREEN).next_to(trans1b, LEFT).scale(0.5)
        trans1c = MathTex(r"y = -|x + 4|").next_to(trans1b, DOWN)
        c1 = Text("Reflect across x axis", color=BLUE).next_to(trans1c, LEFT).scale(0.5)
        trans1d = MathTex(r"y = -|x + 4| - 7").next_to(trans1c, DOWN)
        d1= Text("Shift DOWN 7 units", color=YELLOW).next_to(trans1d, LEFT, buff=-0.5).scale(0.5)
        
        trans2 = MathTex(r"y = 2|x - 1| + 3").next_to(trans, DOWN)
        trans2a = MathTex(r"y = |x|").next_to(trans2, DOWN)
        a2 = Text("Parent function", color=RED).next_to(trans2a, LEFT).scale(0.5)
        trans2b = MathTex(r"y = |x - 1|").next_to(trans2a,DOWN)
        b2 = Text("Shift RIGHT 1 unit", color=GREEN).next_to(trans2b, LEFT).scale(0.5)
        trans2c = MathTex(r"y = 2|x - 1|").next_to(trans2b, DOWN)
        c2 = Text("Stretch the function", color=BLUE).next_to(trans2c, LEFT).scale(0.5)
        trans2d = MathTex(r"y = 2|x - 1| + 3").next_to(trans2c, DOWN)
        d2= Text("Shift UP 3 units", color=YELLOW).next_to(trans2d, LEFT, buff=-0.5).scale(0.5)
        
        graph1a = axes.plot(lambda x: abs(x - 1), color=WHITE)
        graph_label1a = axes.get_graph_label(graph1a, label=Tex("$y = |x - 1|$")).shift(DOWN)
        graph2a = axes.plot(lambda x: 2 * abs(x - 1), color=WHITE)
        graph_label2a = axes.get_graph_label(graph2a, label=Tex("$y = 2|x - 1|$")).shift(DOWN * 2)
        graph3a = axes.plot(lambda x: 2 * abs(x - 1) + 3, color=WHITE)
        graph_label3a = axes.get_graph_label(graph3a, label=Tex("$y = 2|x - 1| + 3$")).shift(DOWN * 2)
        
        
        
        trans3 = Text("EX: Translate an absolute value function 4 units to the left, and 7 units down").to_edge(UP, buff=1.5).scale(0.5)
        trans3a = MathTex(r"y = |x|").next_to(trans3, DOWN)
        a3 = Text("Parent function", color=RED).next_to(trans3a, LEFT).scale(0.5)
        trans3b = MathTex(r"y = |x + 4|").next_to(trans3a,DOWN)
        b3 = Text("Translate LEFT 4 units", color=YELLOW).next_to(trans3b, LEFT, buff=-1).scale(0.5)
        trans3c = MathTex(r"y = |x + 4| - 7").next_to(trans3b, DOWN)
        c3 = Text("Translate DOWN 7 units", color=BLUE).next_to(trans3c, LEFT, buff=-1).scale(0.5)
        
        
        graph1b = axes.plot(lambda x: abs(x + 4), color=WHITE)
        graph_label1b = axes.get_graph_label(graph1b, label=Tex("$y = |x + 4|$")).shift(DOWN)
        graph2b = axes.plot(lambda x: abs(x + 4) - 7, color=WHITE)
        graph_label2b = axes.get_graph_label(graph2b, label=Tex("$y = |x + 4| - 7$")).shift(DOWN * 2)
        
        
        
        
        
        trans4 = Text("EX: Translate a quadratic function 3 units to the right and stretch it by a factor of 2").to_edge(UP, buff=1.5).scale(0.5)
        trans4a = Tex("$y = x^2$").next_to(trans4, DOWN)
        a4 = Text("Parent function", color=RED).next_to(trans4a, LEFT).scale(0.5)
        trans4b = MathTex(r"y = (x - 3)^2").next_to(trans4a,DOWN)
        b4 = Text("Translate RIGHT 3 units", color=YELLOW).next_to(trans4b, LEFT, buff=-1).scale(0.5)
        trans4c = MathTex(r"y = 2(x - 3)^2").next_to(trans4b, DOWN)
        c4 = Text("Stretch by a factor of 2", color=BLUE).next_to(trans4c, LEFT, buff=-1).scale(0.5)
        
        
        graph2c = axes.plot(lambda x: (x - 3)**2, color=WHITE) 
        graph_label2c = axes.get_graph_label(graph2c, label=Tex("$y = (x - 3)^2$")).shift(DOWN)
        graph3c = axes.plot(lambda x: 2 * (x-3)**2, color=WHITE)
        graph_label3c = axes.get_graph_label(graph3c, label=Tex("$y = 2(x - 3)^2$")).shift(DOWN * 2)
        
        

        self.play(Write(trans))
        self.wait(4)
        self.play(Write(trans1))
        self.wait(10)
        self.play(TransformFromCopy(trans1, trans1a))
        self.wait(2)
        self.play(Write(a1))
        self.wait(2)
        self.play(TransformFromCopy(trans1a, trans1b))
        self.wait(2)
        self.play(TransformFromCopy(a1,b1))
        self.wait(2)
        self.play(TransformFromCopy(trans1b, trans1c))
        self.wait(2)
        self.play(TransformFromCopy(b1,c1))
        self.wait(2)
        self.play(TransformFromCopy(trans1c, trans1d))
        self.wait(2)
        self.play(TransformFromCopy(c1,d1))
        self.wait(6)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)
        trans1.to_edge(UP)
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(2)
        self.play(Transform(graph, graph1), Transform(graph_label, graph_label1), run_time=3)
        self.wait(3)
        self.play(Transform(graph, graph2), Transform(graph_label, graph_label2), run_time=3)
        self.wait(3)
        self.play(Transform(graph, graph3), Transform(graph_label, graph_label3), run_time=3)
        self.wait(5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)
        self.play(Write(trans))
        self.wait(4)
        self.play(Write(trans2))
        self.wait(10)
        self.play(TransformFromCopy(trans2, trans2a))
        self.wait(2)
        self.play(Write(a2))
        self.wait(2)
        self.play(TransformFromCopy(trans2a, trans2b))
        self.wait(2)
        self.play(TransformFromCopy(a2,b2))
        self.wait(2)
        self.play(TransformFromCopy(trans2b, trans2c))
        self.wait(2)
        self.play(TransformFromCopy(b2,c2))
        self.wait(2)
        self.play(TransformFromCopy(trans2c, trans2d))
        self.wait(2)
        self.play(TransformFromCopy(c2,d2))
        self.wait(6)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)
        trans2.to_edge(UP)
        
        self.play(Create(axes), Restore(graph), Restore(graph_label))
        self.wait(2)
        self.play(Transform(graph, graph1a), Transform(graph_label, graph_label1a), run_time=3)
        self.wait(3)
        self.play(Transform(graph, graph2a), Transform(graph_label, graph_label2a), run_time=3)
        self.wait(3)
        self.play(Transform(graph, graph3a), Transform(graph_label, graph_label3a), run_time=3)
        self.wait(5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)
     
        self.play(Write(trans3))
        self.wait(10)
        self.play(TransformFromCopy(trans3, trans3a))
        self.wait(2)
        self.play(Write(a3))
        self.wait(2)
        self.play(TransformFromCopy(trans3a, trans3b))
        self.wait(2)
        self.play(TransformFromCopy(a3,b3))
        self.wait(2)
        self.play(TransformFromCopy(trans3b, trans3c))
        self.wait(2)
        self.play(TransformFromCopy(b3,c3))
        self.wait(6)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        
        self.play(Create(axes), Restore(graph), Restore(graph_label))
        self.wait(2)
        self.play(Transform(graph, graph1b), Transform(graph_label, graph_label1b), run_time=3)
        self.wait(3)
        self.play(Transform(graph, graph2b), Transform(graph_label, graph_label2b), run_time=3)
        self.wait(5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)
        self.play(Write(trans4))
        self.wait(10)
        self.play(TransformFromCopy(trans4, trans4a))
        self.wait(2)
        self.play(Write(a4))
        self.wait(2)
        self.play(TransformFromCopy(trans4a, trans4b))
        self.wait(2)
        self.play(TransformFromCopy(a4,b4))
        self.wait(2)
        self.play(TransformFromCopy(trans4b, trans4c))
        self.wait(2)
        self.play(TransformFromCopy(b4,c4))
        self.wait(6)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.play(Create(axes), Create(graphx), Create(graph_labelx))
        self.wait(2)
        self.play(Transform(graphx, graph2c), Transform(graph_labelx, graph_label2c), run_time=3)
        self.wait(3)
        self.play(Transform(graphx, graph3c), Transform(graph_labelx, graph_label3c), run_time=3)
        self.wait(5)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        
        
        
        
        
        
        
        
        
        