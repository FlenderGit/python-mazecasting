class Cell:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

        self.walls = {
            'N' : True,
            'S' : True,
            'W' : True,
            'E' : True
        }