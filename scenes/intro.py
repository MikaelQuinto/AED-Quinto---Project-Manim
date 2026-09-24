from manim import BLUE, GREEN, UP, Circle, Create, Scene, Square, Text, Transform, VGroup, Write


class EscenaInicial(Scene):

    def construct(self) -> None:
        titulo = Text("Animando estructuras de datos", font_size=42)
        subtitulo = Text("Proyecto 1 - AED", font_size=28, color=BLUE)
        subtitulo.next_to(titulo, direction=-UP)

        encabezado = VGroup(titulo, subtitulo)
        self.play(Write(encabezado))
        self.wait(0.5)

        circulo = Circle(color=BLUE, fill_opacity=0.35)
        cuadrado = Square(color=GREEN, fill_opacity=0.35)

        self.play(encabezado.animate.to_edge(UP), Create(circulo))
        self.play(Transform(circulo, cuadrado))
        self.wait(1)