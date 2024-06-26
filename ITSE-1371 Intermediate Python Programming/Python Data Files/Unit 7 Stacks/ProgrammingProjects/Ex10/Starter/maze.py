"""
File: maze.py
Project 7.10

Determine the solution to a maze problem.
Uses a gid to represent the maze.  This grid is input from
a text file.  Uses a stack-based backtracking algorithm.
Also maintains a count of the number of grid cells visited
during the course of the process.
"""

from grid import Grid
from arraystack import ArrayStack
from counter import Counter

def main():
    counter = Counter()
    maze = getMazeFromFile()
    print(maze)
    (startRow, startCol) = findStartPos(maze)
    success = getOut(startRow, startCol, maze, counter)
    if success:
        print("Maze solved:")
        print(maze)
    else:
        print("No path out of this maze")
    print("Number of cells visited:", counter)
    
def getMazeFromFile():
    """Reads the maze from a text file and returns a grid that
    represents it."""
    name = input("Enter a file name for the maze: ")
    fileObj = open(name, 'r')
    firstLine = list(map(int, fileObj.readline().strip().split()))
    rows = firstLine[0]
    columns = firstLine[1]
    maze = Grid(rows, columns, "*")
    for row in range(rows):
        line = fileObj.readline().strip()
        column = 0
        for ch in line:
            maze[row][column] = ch
            column += 1
    return maze

def findStartPos(maze):
    """Returns the position of the start symbol in the grid."""
    for row in range(maze.getHeight()):
        for column in range(maze.getWidth()):
            if maze[row][column] == 'P':
                return (row, column)
    return (-1, -1)
                
def getOut(row, column, maze):
    """(row,column) is the position of the start symbol in the maze.
    Returns True if the maze can be solved or False otherwise."""
    # States are tuples of coordinates of cells in the grid.
    stack = ArrayStack()
    stack.push((row, column))
    while not stack.isEmpty():
        (row, column) = stack.pop()
        if  maze[row][column] == 'T': 
            return True
        elif maze[row][column] != '.':
            # Cell has not been visited, so mark it and push adjacent unvisited
            # positions onto the stack
            maze[row][column] = '.'
            # Try NORTH
            if row != 0 and not maze[row - 1][column] in ('*', '.'):
                stack.push((row - 1, column))             
            # Try SOUTH
            if row + 1 != maze.getHeight() and not maze[row + 1][column] in ('*', '.'):         
                stack.push((row + 1, column))             
            # Try EAST
            if column + 1 != maze.getWidth() and not maze[row][column + 1] in ('*', '.'):         
                stack.push((row, column + 1))             
            # Try WEST
            if column != 0 and not maze[row][column - 1] in ('*', '.'):         
                stack.push((row, column - 1))
    return False

if __name__ == "__main__": main()
