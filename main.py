import sys

from graphics import Window
from maze import Maze


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)

    window = Window(screen_x, screen_y)
    maze = Maze(
        margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window, 11
    )
    print("Maze created...")
    isSolvable = maze.solve()
    if isSolvable:
        print("Maze solved!")
    else:
        print("Maze cannot be solved")
    window.wait_for_close()


if __name__ == "__main__":
    main()
