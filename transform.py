from manim import *
import math


class transformations(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-20,20,5],
            y_range=[-15,15,5],
            axis_config={"color": BLUE}
        )
        axes.add_coordinates()
        axes.save_state()
        axes2 = Axes(
            x_range=[0,6,1],
            y_range=[-4,4,1],
            axis_config={"color": BLUE}
        )
        axes2.add_coordinates()
        axes2.save_state()
        
        axes3 = Axes(
            x_range=[-5,0,1],
            y_range=[-4,4,1],
            axis_config={"color": BLUE}
        )
        axes3.add_coordinates()
        
        
        transUp = Text("To translate up, we add to the parent function", color=YELLOW).scale(0.4).to_corner(DR)
        transDown = Text("To translate down, we subtract from the parent function", color=YELLOW).scale(0.4).to_corner(DL)
        transRight = Text("To translate right, we subtract from inside the parent function", color=YELLOW).scale(0.4).to_corner(DL)
        transLeft = Text("To translate left, we add from inside the parent function", color=YELLOW).scale(0.4).to_corner(DL)
        outsideNeg = Text("A negative sign on the outside shows a reflection (flip) across the x axis", color=YELLOW).scale(0.4).to_corner(DL)
        insideNeg = Text("A negative sign on the inside shows a reflection (flip) across the y axis", color=YELLOW).scale(0.4).to_corner(DL)
        stretch = Text("Multiplying by a number bigger than 1 stretches the function", color=YELLOW).scale(0.4).to_corner(DL)
        shrink = Text("Multiplying by a number less than 1 (fraction or decimal) shrinks the function", color=YELLOW).scale(0.4).to_corner(DL)
        
        
        graph = axes.plot(lambda x: x**2, color=WHITE)
        graph_label = axes.get_graph_label(graph, label="y = x^{2}")
        graph.save_state()
        graph_label.save_state()
        
        graph2 = axes2.plot(lambda x: math.sqrt(x), color=WHITE)
        graph_label2 = axes2.get_graph_label(graph2, label=Tex("$y = \sqrt{x}$")).shift(UP)
        graph2.save_state()
        graph_label2.save_state()
        
        graphUp = axes.plot(lambda x: (x**2) + 5, color=GREEN)
        graph_labelUp = axes.get_graph_label(graphUp, label="y = x^{2} + 5")
        LabelUp = Text("translates up 5").scale(0.5).move_to([3,1,0])
        
        graphDown = axes.plot(lambda x: (x**2) - 3, color=GREEN)
        graph_labelDown = axes.get_graph_label(graphDown, label="y = x^{2} - 3")
        LabelDown = Text("translates DOWN 3").scale(0.5).move_to([3,-1,0])
        
        graphRight = axes.plot(lambda x: ((x-4)**2), color=GREEN)
        graph_labelRight = axes.get_graph_label(graphRight, label="y = (x-4)^{2}")
        LabelRight = Text("translates RIGHT 4").scale(0.5).move_to([4,1,0])
        
        graphLeft = axes.plot(lambda x: ((x+2)**2), color=GREEN)
        graph_labelLeft = axes.get_graph_label(graphLeft, label="y = (x+2)^{2}")
        LabelLeft = Text("translates LEFT 2").scale(0.5).move_to([3,1,0])
        
        graphFlipX = axes2.plot(lambda x: -(math.sqrt(x)), color=GREEN)
        graph_labelFlipX = axes2.get_graph_label(graphFlipX, label=Tex("$y = -(\sqrt{x})$")).shift(DOWN)
        
        graphIn = axes3.plot(lambda x: math.sqrt(-x), color=GREEN)
        graph_labelIn = axes3.get_graph_label(graphIn, label=Tex("$y = \sqrt{-x}$")).to_corner(UL)
        
        graphStretch = axes.plot(lambda x: 2*(x**2), color=GREEN)
        graph_labelStretch = axes.get_graph_label(graphStretch, label="y = 2x^{2}")
        LabelStretch = Text("Makes the function taller/skinnier").scale(0.4).move_to([4,1,0])
        
        graphShrink = axes.plot(lambda x: 0.5*(x**2), color=GREEN)
        graph_labelShrink = axes.get_graph_label(graphStretch, label="y = 0.5x^{2}").shift(RIGHT)
        LabelShrink = Text("Makes the function shorter/wider").scale(0.4).move_to([4,1,0])
        
        self.play(Create(axes), Create(graph),  Write(graph_label))
        self.wait(2)
        self.play(Write(transUp))
        self.wait(5)
        self.play(Transform(graph, graphUp),Transform(graph_label, graph_labelUp), Write(LabelUp))
        self.wait(2)
        self.play(Restore(graph), Restore(graph_label), Unwrite(LabelUp))
        self.play(Unwrite(transUp))
        self.wait(2)
        self.play(Write(transDown))
        self.wait(5)
        self.play(Transform(graph, graphDown),Transform(graph_label, graph_labelDown), Write(LabelDown))
        self.wait(2)
        self.play(Restore(graph), Restore(graph_label), Unwrite(LabelDown))
        self.play(Unwrite(transDown))
        self.wait(2)
        self.play(Write(transRight))
        self.wait(5)
        self.play(Transform(graph, graphRight), Transform(graph_label, graph_labelRight), Write(LabelRight))
        self.wait(2)
        self.play(Restore(graph), Restore(graph_label), Unwrite(LabelRight))
        self.play(Unwrite(transRight))
        self.wait(2)
        self.play(Write(transLeft))
        self.wait(5)
        self.play(Transform(graph, graphLeft), Transform(graph_label, graph_labelLeft), Write(LabelLeft))
        self.wait(10)
        self.play(Transform(axes, axes2),Unwrite(transLeft), Unwrite(LabelLeft), Transform(graph, graph2), Transform(graph_label, graph_label2), run_time=3)
        self.wait(2)
        self.play(Write(outsideNeg))
        self.wait(5)
        self.play(TransformFromCopy(graph, graphFlipX), TransformFromCopy(graph_label, graph_labelFlipX))
        self.wait(5)
        self.remove(graphFlipX)
        self.remove(graph_labelFlipX)
        self.play(Unwrite(outsideNeg))
        self.wait(2)
        self.play(Write(insideNeg))
        self.wait(2)
        self.play(Transform(axes, axes3), Transform(graph, graphIn), Transform(graph_label, graph_labelIn), run_time=3)
        self.wait(3)
        self.remove(graphIn)
        self.remove(graph_labelIn)
        self.play(Unwrite(insideNeg))
        self.wait(3)
        self.play(Restore(axes), Restore(graph), Restore(graph_label), run_time=3)
        self.wait(1)
        self.play(Write(stretch))
        self.wait(2)
        self.play(Transform(graph, graphStretch), Transform(graph_label,graph_labelStretch), Write(LabelStretch))
        self.wait(3)
        self.play(Restore(graph), Restore(graph_label), Unwrite(stretch), Unwrite(LabelStretch))
        self.wait(2)
        self.play(Write(shrink))
        self.wait(3)
        self.play(Transform(graph, graphShrink), Transform(graph_label, graph_labelShrink), Write(LabelShrink))
        self.wait(15)
        
        
        
        
        
        