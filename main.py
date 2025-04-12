from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell_size = 50
    cells:list[Cell] = []
    for x in range(1, 800, cell_size):
        for y in range(1, 600, cell_size):
            new_cell = Cell(x,y, x + cell_size, y + cell_size, win)
            cells.append(new_cell)
    for cell in cells:
        cell.draw()
    cells[0].draw_move(cells[1])
    cells[20].draw_move(cells[30], True)
    print(len(cells))
    
    win.wait_for_close()

if __name__ == "__main__":
    main()