from classes import Window, Point, Line, Cell

def main():
    win = Window(800, 600)
    cell = Cell(win)
    p1 = Point(100, 150)
    p2 = Point(400, 300)
    line = Line(p1, p2)

    win.draw_line(line, "black")
    cell.draw(100, 100, 150, 150)

    win.wait_for_close()

if __name__ == "__main__":
    main()
