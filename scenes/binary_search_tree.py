from manim import (
    BLUE,
    DOWN,
    GREEN,
    LEFT,
    RED,
    RIGHT,
    UP,
    WHITE,
    YELLOW,
    Circle,
    Create,
    FadeIn,
    FadeOut,
    Group,
    Line,
    Scene,
    Text,
    Transform,
    VGroup,
    Write,
)

from scenes.bst_model import BinarySearchTree


TITLE = "Árbol binario de búsqueda"
AUTHORS = "Autor: Mikael Quinto Ramos"
VALUES = [8, 3, 10, 1, 6, 14, 4, 7]

POSITIONS = {
    8: UP * 1.8,
    3: LEFT * 3 + UP * 0.4,
    10: RIGHT * 3 + UP * 0.4,
    1: LEFT * 4.5 + DOWN * 1.1,
    6: LEFT * 1.5 + DOWN * 1.1,
    14: RIGHT * 4.5 + DOWN * 1.1,
    4: LEFT * 2.2 + DOWN * 2.6,
    7: LEFT * 0.8 + DOWN * 2.6,
}

PARENTS = {3: 8, 10: 8, 1: 3, 6: 3, 14: 10, 4: 6, 7: 6}


class ArbolBinarioBusqueda(Scene):

    def construct(self) -> None:
        self.tree = BinarySearchTree()
        self.nodes: dict[int, VGroup] = {}
        self.edges: dict[int, Line] = {}
        self.current_heading: Text | None = None

        self.show_title()
        self.explain_concept()
        self.animate_insertions()
        self.animate_search(7)
        self.animate_failed_search(5)
        self.animate_inorder()
        self.show_complexity()
        self.show_closing()

    def show_title(self) -> None:
        title = Text(TITLE, font_size=48, color=BLUE)
        course = Text("CS2023 - Algoritmos y Estructuras de Datos", font_size=28)
        authors = Text(AUTHORS, font_size=25)
        presentation = VGroup(title, course, authors).arrange(DOWN, buff=0.35)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(course), FadeIn(authors), run_time=1)
        self.wait(6)
        self.play(FadeOut(presentation), run_time=1)

    def explain_concept(self) -> None:
        heading = self.create_heading("¿Qué es un árbol binario de búsqueda?")
        self.current_heading = heading
        root = self.create_node(8, UP * 0.8)
        left_child = self.create_node(3, LEFT * 2 + DOWN * 0.8)
        right_child = self.create_node(10, RIGHT * 2 + DOWN * 0.8)
        left_edge = self.create_edge(root, left_child)
        right_edge = self.create_edge(root, right_child)

        rule_left = Text("Menores", font_size=26, color=BLUE).next_to(left_child, DOWN)
        rule_right = Text("Mayores", font_size=26, color=GREEN).next_to(right_child, DOWN)
        rule = Text(
            "Cada nodo tiene como máximo dos hijos",
            font_size=28,
        ).to_edge(DOWN)

        self.play(Write(heading))
        self.play(Create(root))
        self.play(Create(left_edge), Create(right_edge))
        self.play(Create(left_child), Create(right_child))
        self.play(FadeIn(rule_left), FadeIn(rule_right), Write(rule))
        self.wait(13)
        self.clear_scene()

    def animate_insertions(self) -> None:
        heading = self.create_heading("Construcción del árbol: inserción")
        self.current_heading = heading
        self.play(Write(heading))

        for value in VALUES:
            path = self.tree.insert(value)
            message = Text(f"Insertar {value}", font_size=30).to_edge(DOWN)
            self.play(Write(message), run_time=0.5)

            for current_value in path:
                comparison = self.comparison_text(value, current_value)
                comparison.move_to(message)
                self.play(
                    self.nodes[current_value].animate.set_color(YELLOW),
                    Transform(message, comparison),
                    run_time=0.7,
                )
                self.wait(1.5)
                self.play(
                    self.nodes[current_value].animate.set_color(WHITE),
                    run_time=0.3,
                )

            self.add_visual_node(value)
            self.play(FadeOut(message), run_time=0.3)

        self.wait(8)

    def animate_search(self, value: int) -> None:
        heading = self.replace_heading(f"Búsqueda del valor {value}")
        path, found = self.tree.search(value)
        message = Text("Comenzamos desde la raíz", font_size=28).to_edge(DOWN)
        self.play(Write(message))

        for current_value in path:
            if current_value == value:
                text = f"Encontramos {value}"
                color = GREEN
            else:
                text = self.comparison_sentence(value, current_value)
                color = YELLOW

            next_message = Text(text, font_size=28, color=color).move_to(message)
            self.play(
                self.nodes[current_value].animate.set_color(color),
                Transform(message, next_message),
                run_time=0.8,
            )
            self.wait(2.5)

            if current_value != value:
                self.play(self.nodes[current_value].animate.set_color(WHITE), run_time=0.3)

        if found:
            self.wait(5)
            self.play(self.nodes[value].animate.set_color(WHITE), FadeOut(message))

        self.wait(1)

    def animate_failed_search(self, value: int) -> None:
        self.replace_heading(f"Búsqueda del valor {value}")
        path, found = self.tree.search(value)
        message = Text("Comenzamos desde la raíz", font_size=28).to_edge(DOWN)
        self.play(Write(message))

        for current_value in path:
            next_message = Text(
                self.comparison_sentence(value, current_value),
                font_size=28,
                color=YELLOW,
            ).move_to(message)
            self.play(
                self.nodes[current_value].animate.set_color(YELLOW),
                Transform(message, next_message),
                run_time=0.8,
            )
            self.wait(2)
            self.play(self.nodes[current_value].animate.set_color(WHITE), run_time=0.3)

        if not found:
            not_found = Text(
                f"{value} no está en el árbol",
                font_size=30,
                color=RED,
            ).move_to(message)
            self.play(Transform(message, not_found))
            self.wait(6)
            self.play(FadeOut(message))

    def animate_inorder(self) -> None:
        self.replace_heading("Recorrido in-order: izquierda, raíz, derecha")
        result = Text("Resultado:", font_size=28).to_edge(DOWN)
        self.play(Write(result))

        visited: list[str] = []
        for value in self.tree.inorder():
            visited.append(str(value))
            updated_result = Text(
                f"Resultado: {', '.join(visited)}",
                font_size=28,
                color=GREEN,
            ).move_to(result)

            self.play(self.nodes[value].animate.set_color(GREEN), run_time=0.4)
            self.play(Transform(result, updated_result), run_time=0.5)
            self.wait(1.5)
            self.play(self.nodes[value].animate.set_color(WHITE), run_time=0.3)

        explanation = Text(
            "El recorrido produce los valores en orden",
            font_size=26,
            color=GREEN,
        ).next_to(result, UP)
        self.play(Write(explanation))
        self.wait(8)
        self.clear_scene()

    def show_complexity(self) -> None:
        heading = self.create_heading("Complejidad de búsqueda")
        average = Text("Árbol equilibrado: O(log n)", font_size=34, color=GREEN)
        worst = Text("Árbol degenerado: O(n)", font_size=34, color=RED)
        explanation = Text(
            "El rendimiento depende de la forma del árbol",
            font_size=28,
        )
        content = VGroup(average, worst, explanation).arrange(DOWN, buff=0.7)

        self.play(Write(heading))
        self.play(Write(average))
        self.wait(5)
        self.play(Write(worst))
        self.wait(5)
        self.play(FadeIn(explanation))
        self.wait(12)
        self.clear_scene()

    def show_closing(self) -> None:
        title = Text("Árbol binario de búsqueda", font_size=46, color=BLUE)
        summary = VGroup(
            Text("Inserción", font_size=30),
            Text("Búsqueda", font_size=30),
            Text("Recorrido in-order", font_size=30),
        ).arrange(DOWN, buff=0.35)
        authors = Text(AUTHORS, font_size=24)
        closing = VGroup(title, summary, authors).arrange(DOWN, buff=0.6)

        self.play(Write(title))
        self.play(FadeIn(summary))
        self.play(FadeIn(authors))
        self.wait(10)
        self.play(FadeOut(closing))

    def add_visual_node(self, value: int) -> None:
        node = self.create_node(value, POSITIONS[value])
        self.nodes[value] = node

        if value in PARENTS:
            parent_value = PARENTS[value]
            edge = self.create_edge(self.nodes[parent_value], node)
            self.edges[value] = edge
            self.play(Create(edge), Create(node), run_time=0.8)
        else:
            self.play(Create(node), run_time=0.8)

        self.play(node.animate.set_color(GREEN), run_time=0.3)
        self.wait(2)
        self.play(node.animate.set_color(WHITE), run_time=0.3)

    def create_node(self, value: int, position) -> VGroup:
        circle = Circle(radius=0.42, color=WHITE, fill_opacity=0.15)
        label = Text(str(value), font_size=28)
        return VGroup(circle, label).move_to(position)

    def create_edge(self, parent: VGroup, child: VGroup) -> Line:
        return Line(parent.get_center(), child.get_center(), buff=0.45, color=WHITE)

    def create_heading(self, text: str) -> Text:
        return Text(text, font_size=34, color=BLUE).to_edge(UP)

    def replace_heading(self, text: str) -> Text:
        if self.current_heading is None:
            raise RuntimeError("No hay un encabezado activo para reemplazar")

        new_heading = self.create_heading(text)
        self.play(Transform(self.current_heading, new_heading))
        return self.current_heading

    def comparison_text(self, value: int, current: int) -> Text:
        return Text(self.comparison_sentence(value, current), font_size=28)

    def comparison_sentence(self, value: int, current: int) -> str:
        if value < current:
            return f"{value} < {current}: avanzamos a la izquierda"
        if value > current:
            return f"{value} > {current}: avanzamos a la derecha"
        return f"{value} = {current}: valor encontrado"

    def clear_scene(self) -> None:
        if self.mobjects:
            self.play(FadeOut(Group(*self.mobjects)), run_time=0.8)
        self.current_heading = None