from graphics import Window
from maze import Maze

def main():
    

    win = Window(800, 900)
    m = Maze(100, 100, 10, 12, 50, 50, win)
    m.solve()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()