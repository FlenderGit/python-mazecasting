from Cell import Cell


class Maze:
    def __init__(self, row, column) -> None:
        self.nbRow = row
        self.nbColumn = column
        self.maze = [[Cell(x, y) for y in range(column)] for x in range(row)]

    def __str__(self) -> str:

        r = "+"

        for x in range(self.nbColumn):
            if (self.maze[0][x].walls['N']):
                r += '---+'
            else:
                r += '   +'
        r += '\n'
        for y in range(self.nbRow):
            if (self.maze[y][0].walls['W']):
                r += '|'
            else:
                r += ' '
            for x in range(self.nbColumn):
                if (self.maze[y][x].walls['E']):
                    r += '   |'
                else:
                    r += '    '
            r += '\n'
            r += '+'
            for x in range(self.nbColumn):
                
                if (self.maze[y][x].walls['S']):
                    r += '---+'
                else:
                    r += '   +' 
            r += '\n'

        return r