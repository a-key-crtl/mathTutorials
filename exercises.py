from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import math

class exercises(Scene):
    def construct(self):
        self.set_speech_service(GTTSService())
        
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
        c2 = Text("Stretch by a factor of 2", color=BLUE).next_to(trans2c, LEFT).scale(0.5)
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
        
        
        self.wait(2)
        with self.voiceover(text="In this example we are asked to describe the transformation.") as tracker:
            self.play(Write(trans))
        self.wait(2)
        with self.voiceover(text="Here our equation is y equals negative absolute value of x plus four, then outside the absolute value sign we have a minus seven") as tracker:
            self.play(Write(trans1))
        self.wait(2)
        with self.voiceover(text="If you remember, transformations are what we apply to our parent function so let's first take out our parent function from the equation and apply each transformation step by step.") as tracker:
            self.play(TransformFromCopy(trans1, trans1a))
        self.wait(2)
        with self.voiceover(text="Since there is an x written inside an absolute value symbol from our original equation, we know that y equals the absolute value of x is going to be our parent function.") as tracker:
            self.play(Write(a1))
        self.wait(2)
        with self.voiceover(text="Next, we see we are adding four to x inside the absolute value symbol.") as tracker:
            self.play(TransformFromCopy(trans1a, trans1b))
        self.wait(2)
        with self.voiceover(text="Since we are adding four inside the parent function we will shift the graph left four units.") as tracker:
            self.play(TransformFromCopy(a1,b1))
        self.wait(2)
        with self.voiceover(text="We are also multiplying a negative to the outside of the absolute value.") as tracker:
            self.play(TransformFromCopy(trans1b, trans1c))
        self.wait(2)
        with self.voiceover(text="A negative on the outside will reflect the parent graph across the x axis.") as tracker:
            self.play(TransformFromCopy(b1,c1))
        self.wait(2)
        with self.voiceover(text="Finally, we are subtracting seven at the end of the equation.") as tracker:
            self.play(TransformFromCopy(trans1c, trans1d))
        self.wait(2)
        with self.voiceover(text="Our final transformation then will to shift the graph down seven units. Now that we have all of our transformations laid out let's see how this will transform our parent graph.") as tracker:
            self.play(TransformFromCopy(c1,d1))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)
        trans1.to_edge(UP)
        with self.voiceover(text="Here is our parent graph of y equals the absolute value of x.") as tracker:
            self.play(Create(axes), Create(graph), Write(graph_label))
        self.wait(2)
        with self.voiceover(text="Adding four to x inside the absolute value shifts the graph left four units.") as tracker:
            self.play(Transform(graph, graph1), Transform(graph_label, graph_label1), run_time=3)
        self.wait(2)
        with self.voiceover(text="Then if we place a negative on the outside of the absolute value the graph reflects over the x axis.") as tracker:
            self.play(Transform(graph, graph2), Transform(graph_label, graph_label2), run_time=3)
        self.wait(3)
        with self.voiceover(text="Lastly, we subtract seven from the whole absolute value term which shifts our graph down seven units. After applying these transformations, our new equation has now become y equals the negative absolute value of x plus four minus seven.") as tracker:
            self.play(Transform(graph, graph3), Transform(graph_label, graph_label3), run_time=3)
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)
        with self.voiceover(text="Let's look at another example. Again we want to describe the transformation.") as tracker:
            self.play(Write(trans))
        self.wait(2)
        with self.voiceover(text="Here our equation is two times the absolute value of x minus one plus three.") as tracker:
            self.play(Write(trans2))
        self.wait(2)
        with self.voiceover(text="If you remember again, transformations are what we apply to our parent function so let's first take out our parent function from the equation and apply each transformation step by step.") as tracker:
            self.play(TransformFromCopy(trans2, trans2a))
        self.wait(2)
        with self.voiceover(text="y equals the absolute value of x is our parent function.") as tracker:
            self.play(Write(a2))
        self.wait(2)
        with self.voiceover(text="Then we subtract one from x inside the absolute value sign.") as tracker:
            self.play(TransformFromCopy(trans2a, trans2b))
        self.wait(2)
        with self.voiceover(text="This will shift the graph right one unit.") as tracker:
            self.play(TransformFromCopy(a2,b2))
        self.wait(2)
        with self.voiceover(text="Next we multiply two on the outside of the absolute value symbol.") as tracker:
            self.play(TransformFromCopy(trans2b, trans2c))
        self.wait(2)
        with self.voiceover(text="Since two is greater than one, we will stretch the graph by a factor of two.") as tracker:
            self.play(TransformFromCopy(b2,c2))
        self.wait(2)
        with self.voiceover(text="Finally we add three to the end of the equation. ") as tracker:
            self.play(TransformFromCopy(trans2c, trans2d))
        self.wait(2)
        with self.voiceover(text="Adding three will shift the graph up three units. Now let's see how the transformations we have ust described will transform our parent graph.") as tracker:
            self.play(TransformFromCopy(c2,d2))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        trans2.to_edge(UP)
        with self.voiceover(text="Here we are back to our parent graph for our parent function y equals the absolute value of x.") as tracker:
            self.play(Create(axes), Restore(graph), Restore(graph_label))
        self.wait(2)
        with self.voiceover(text="Inside the absolute value we subtract one from x which shifts the graph to the right one unit.") as tracker:
            self.play(Transform(graph, graph1a), Transform(graph_label, graph_label1a), run_time=3)
        self.wait(2)
        with self.voiceover(text="Then we multiply two to the outside of the absolute value and stretch the graph by a factor of two.") as tracker:
            self.play(Transform(graph, graph2a), Transform(graph_label, graph_label2a), run_time=3)
        self.wait(2)
        with self.voiceover(text="Last but not least, we add three to the absolute value term and shift our graph up three units. So after applying our transformation, our new function is y equals two times the absolute value of x minus one plus three and our graphs shape and position has changed.") as tracker:
            self.play(Transform(graph, graph3a), Transform(graph_label, graph_label3a), run_time=3)
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        with self.voiceover(text="In our next example, we are told to translate an absolute value function four units to the left, and seven units down.") as tracker:
            self.play(Write(trans3))
        self.wait(2)
        with self.voiceover(text="Since we are translating an absolute value function, we know our parent function will be y equals the absolute value of x.") as tracker:
            self.play(TransformFromCopy(trans3, trans3a))
        self.wait(2)
        with self.voiceover(text="This is our parent function.") as tracker:
            self.play(Write(a3))
        self.wait(2)
        with self.voiceover(text="Next we will add four to x inside the absolute value symbol.") as tracker:
            self.play(TransformFromCopy(trans3a, trans3b))
        self.wait(2)
        with self.voiceover(text="This translates or shifts the function to the left four units.   ") as tracker:
            self.play(TransformFromCopy(a3,b3))
        self.wait(2)
        with self.voiceover(text="Lastly, we will subtract seven.") as tracker:
            self.play(TransformFromCopy(trans3b, trans3c))
        self.wait(2)
        with self.voiceover(text="This will translate function down seven units. Having applied our translations let's see how this would look graphically.") as tracker:
            self.play(TransformFromCopy(b3,c3))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        with self.voiceover(text="Here we have an absolute value function's parent graph.") as tracker:
            self.play(Create(axes), Restore(graph), Restore(graph_label))
        self.wait(2)
        with self.voiceover(text="To translate left four units, we add four to x inside the absolute value function. ") as tracker:
            self.play(Transform(graph, graph1b), Transform(graph_label, graph_label1b), run_time=3)
        self.wait(2)
        with self.voiceover(text="Then to translate down seven units, we simply subtract seven outside the absolute value term. So after applying our translations, our new function becomes y equals the absolute value of x plus four minus seven.") as tracker:
            self.play(Transform(graph, graph2b), Transform(graph_label, graph_label2b), run_time=3)
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        with self.voiceover(text="In our next example we are asked to translate a quadratic function three units to the right and stretch it by a factor of two.") as tracker:
            self.play(Write(trans4))
        self.wait(2)
        with self.voiceover(text="Since we are asked to translate a quadratic function, we can write y equals x squared. ") as tracker:
            self.play(TransformFromCopy(trans4, trans4a))
        self.wait(2)
        with self.voiceover(text="This quadratic function is our parent function.") as tracker:
            self.play(Write(a4))
        self.wait(2)
        with self.voiceover(text="Next, we want to translate our quadratic function three units to the right. To do this we will subtract three from inside our parent function so the equation now becomes y equals then in parentheses, x minus three squared. ") as tracker:
            self.play(TransformFromCopy(trans4a, trans4b))
        self.wait(2)
        with self.voiceover(text="Subtracting three inside the parentheses will translate the function right three units.") as tracker:
            self.play(TransformFromCopy(a4,b4))
        self.wait(2)
        with self.voiceover(text="Next we multiply by two outside the parentheses.") as tracker:
            self.play(TransformFromCopy(trans4b, trans4c))
        self.wait(2)
        with self.voiceover(text="This will stretch it by a factor of two. Now with all of our translations taken care of let's see how this would look graphically.") as tracker:
            self.play(TransformFromCopy(b4,c4))
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        with self.voiceover(text="Here is the parent graph of our quadratic function y equals x squared.") as tracker:
            self.play(Create(axes), Create(graphx), Create(graph_labelx))
        self.wait(2)
        with self.voiceover(text="Subtracting three from x inside the function will shift the graph right three units.") as tracker:
            self.play(Transform(graphx, graph2c), Transform(graph_labelx, graph_label2c), run_time=3)
        self.wait(3)
        with self.voiceover(text="Then multiplying by two will stretch the graph by a factor of two.") as tracker:
            self.play(Transform(graphx, graph3c), Transform(graph_labelx, graph_label3c), run_time=3)
        self.wait(2)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        
        
        
        
        
        
        
        
        
        