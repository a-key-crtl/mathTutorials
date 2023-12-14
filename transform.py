from manim import *
import math
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class transformations(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())
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
        
        self.wait(1)
        with self.voiceover(text="Here we have the parent graph of our quadratic function y equals x squared. ") as tracker:
            self.play(Create(axes), Create(graph),  Write(graph_label))
        self.wait(2)
        with self.voiceover(text="If we want to translate our graph up, we simply add to the parent function.") as tracker:
            self.play(Write(transUp))
        self.wait(2)
        with self.voiceover(text="If we add 5 to the parent function, we now have y equals x squared plus five. This will translate the graph up five units.") as tracker:
            self.play(Transform(graph, graphUp),Transform(graph_label, graph_labelUp), Write(LabelUp))
        self.wait(2)
        with self.voiceover(text="Let's restore back to our parent graph again and remove the five we added.") as tracker:
            self.play(Restore(graph), Restore(graph_label), Unwrite(LabelUp))
        self.play(Unwrite(transUp))
        self.wait(2)
        with self.voiceover(text="If we wanted to translate our parent function down, we subtract from the parent function.") as tracker:
            self.play(Write(transDown))
        self.wait(2)
        with self.voiceover(text="Subtracting three from the parent function will shift the graph down three units. ") as tracker:
            self.play(Transform(graph, graphDown),Transform(graph_label, graph_labelDown), Write(LabelDown))
        self.wait(2)
        with self.voiceover(text="Removing our minus three restores our parent graph.") as tracker:
            self.play(Restore(graph), Restore(graph_label), Unwrite(LabelDown))
            self.play(Unwrite(transDown))
        self.wait(2)
        with self.voiceover(text="Now if we want to translate our graph to the right we would subtract from inside the parent function.") as tracker:
            self.play(Write(transRight))
        self.wait(2)
        with self.voiceover(text="Notice we subtracted four from x inside the parentheses of our parent function. It is x minus 4 squared instead of x squared minus 4. This will translate the graph right four units") as tracker:
            self.play(Transform(graph, graphRight), Transform(graph_label, graph_labelRight), Write(LabelRight))
        self.wait(2)
        with self.voiceover(text="Here we are back to our parent function.") as tracker:
            self.play(Restore(graph), Restore(graph_label), Unwrite(LabelRight))
            self.play(Unwrite(transRight))
        self.wait(2)
        with self.voiceover(text="To translate our graph to the left, we add to the parent function.") as tracker:
            self.play(Write(transLeft))
        self.wait(2)
        with self.voiceover(text="Adding two to x inside the parent function shifts the graph left two units.") as tracker:
            self.play(Transform(graph, graphLeft), Transform(graph_label, graph_labelLeft), Write(LabelLeft))
        self.wait(2)
        with self.voiceover(text="Let's look at more transformations with another parent graph, the square root function.") as tracker:
            self.play(Transform(axes, axes2),Unwrite(transLeft), Unwrite(LabelLeft), Transform(graph, graph2), Transform(graph_label, graph_label2), run_time=3)
        self.wait(2)
        with self.voiceover(text="A negative sign on the outside shows a reflection across the x axis") as tracker:
            self.play(Write(outsideNeg))
        self.wait(2)
        with self.voiceover(text="So if we put a negative on the outside of our square root we see the graph flips across the x axis.") as tracker:
            self.play(TransformFromCopy(graph, graphFlipX), TransformFromCopy(graph_label, graph_labelFlipX))
        self.wait(2)
        with self.voiceover(text="Removing the negative restores our parent graph.") as tracker:
            self.remove(graphFlipX)
            self.remove(graph_labelFlipX)
            self.play(Unwrite(outsideNeg))
        self.wait(2)
        with self.voiceover(text="A negative sign on the inside shows a reflection across the y axis.") as tracker:
            self.play(Write(insideNeg))
        self.wait(2)
        with self.voiceover(text="If we apply a negative directly to x inside the square root, the graph flips across the y axis and is now pointing  to the left.") as tracker:
            self.play(Transform(axes, axes3), Transform(graph, graphIn), Transform(graph_label, graph_labelIn), run_time=3)
        self.wait(2)
        with self.voiceover(text="You can see the importance of where you place a negative sign to your parent function. A negative on the outside will flip the graph across the x axis and a negative being multiplied to x inside flips the graph across the y axis.") as tracker:
            self.remove(graphIn)
            self.remove(graph_labelIn)
            self.play(Unwrite(insideNeg))
        self.wait(3)
        with self.voiceover(text="Let us return to our quadratic parent graph.") as tracker:
            self.play(Restore(axes), Restore(graph), Restore(graph_label), run_time=2)
        self.wait(1)
        with self.voiceover(text="Multiplying by a number bigger than 1 stretches the function") as tracker:
            self.play(Write(stretch))
        self.wait(2)
        with self.voiceover(text="If we multiply x squared by two, we stretch the graph by a factor of two which makes the graph appear taller.") as tracker:
            self.play(Transform(graph, graphStretch), Transform(graph_label,graph_labelStretch), Write(LabelStretch))
        self.wait(3)
        with self.voiceover(text="Here is our parent graph.") as tracker:
            self.play(Restore(graph), Restore(graph_label), Unwrite(stretch), Unwrite(LabelStretch))
        self.wait(2)
        with self.voiceover(text="Multiplying by a number less than 1 (fraction or decimal) shrinks the function") as tracker:
            self.play(Write(shrink))
        self.wait(3)
        with self.voiceover(text="If we multiply x squared by zero point five, we are shrinking the graph by a factor of zero point five which makes the graph appear shorter or wider. ") as tracker:
            self.play(Transform(graph, graphShrink), Transform(graph_label, graph_labelShrink), Write(LabelShrink))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        
        
        
        
        
        