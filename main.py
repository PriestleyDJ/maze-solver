from cell import Cell
from graphics import Window


def main():
    window = Window(800, 600)

    c1 = Cell(window)
    c1.has_left_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(window)
    c2.has_right_wall = False
    c2.draw(125, 125, 200, 200)

    c3 = Cell(window)
    c3.has_bottom_wall = False
    c3.draw(225, 225, 250, 250)

    c4 = Cell(window)
    c4.has_top_wall = False
    c4.draw(300, 300, 500, 500)

    c1.draw_move(c2)
    c2.draw_move(c3, True)
    c3.draw_move(c4)

    window.wait_for_close()


if __name__ == "__main__":
    main()
