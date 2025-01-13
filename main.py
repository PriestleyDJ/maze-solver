from graphics import Line, Point, Window


def main():
    window = Window(800, 600)
    line = Line(Point(50, 50), Point(100, 100))
    window.draw_line(line)
    window.wait_for_close()


if __name__ == "__main__":
    main()
