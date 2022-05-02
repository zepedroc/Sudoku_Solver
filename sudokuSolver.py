import curses
from curses import wrapper


def drawSudoku(grid, stdscr):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 0:
                stdscr.addstr(i*2, j*4, str(value), RED)
            else:
                stdscr.addstr(i*2, j*4, str(value), BLUE)


def isValidMove(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False

    for x in range(9):
        if grid[x][col] == number:
            return False

    cornerRow = row - row % 3
    cornerCol = col - col % 3

    for x in range(3):
        for y in range(3):
            if grid[cornerRow + x][cornerCol + y] == number:
                return False

    return True


def solve(grid, stdscr, row, col):
    # Re-draw the screen
    stdscr.clear()
    drawSudoku(grid, stdscr)
    stdscr.refresh()

    if col == 9:
        if row == 8:  # if it didn't return false until now then the sudoku is solved
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, stdscr, row, col + 1)

    for num in range(1, 10):  # from 1 to 9

        if isValidMove(grid, row, col, num):
            grid[row][col] = num

            if solve(grid, stdscr, row, col + 1):
                return True

        grid[row][col] = 0

    return False


# sudoku template
grid = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]]


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    GREEN = curses.color_pair(3)
    RED = curses.color_pair(2)

    if solve(grid, stdscr, 0, 0):
        for i in range(9):
            for j in range(9):
                stdscr.addstr(i*2, j*4, str(grid[i][j]), GREEN)
    else:
        stdscr.addstr(5, 15, 'This sudoku has no solution', RED)

    stdscr.getch()


wrapper(main)
