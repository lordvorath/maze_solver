from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell_size = 50
    cells:list[Cell] = []
    for x in range(1, 800, 60):
        for y in range(1, 600, 60):
            new_cell = Cell(x,y, x + cell_size, y + cell_size, win)
            cells.append(new_cell)
    for cell in cells:
        cell.draw()
    cells[0].draw_move(cells[1])
    cells[2].draw_move(cells[3], True)
    print(len(cells))
    
    win.wait_for_close()

if __name__ == "__main__":
    main()