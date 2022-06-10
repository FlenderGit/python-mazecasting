from random import choice
from Maze import Maze
from const import *
import os as os

# Function test data

## Function test if object is Maze
def isMaze(object:Maze)->bool:
    return isinstance(object,Maze)

## Function test if object is tuple
def isTuple(object:tuple)->bool:
    return isinstance(object,tuple)

## Function test if object is direction
def isDirection(direction:str)->bool:
    if ( not isinstance(direction,str) ) : raise ValueError("La valeur rentré en temps que direction n'est pas de type str.")
    return direction in LS_DIRECTION


# Function test maze

## Function test if cell is in maze
def isInMaze(maze:Maze,coord:tuple)->bool:

    # Test type of parameters
    if ( not isMaze(maze) ) : raise ValueError("La valeur rentré en temps que maze n'est pas de type Maze.")
    if ( not isTuple(coord) ) : raise ValueError ("La valeur rentré en temps que coord n'est pas de type tuple.")

    # Test if x is in maze
    x = coord[0]
    if ( x < 0 or x >= maze.nbColumn ):
        raise ValueError(f'La valeur de x doit être comprise entre 0 et {maze.nbColumn-1}. Elle est ici de {x}.')

    # Test if y is in maze
    y = coord[1]
    if ( y < 0 or y >= maze.nbRow ):
        raise ValueError(f'La valeur de y doit être comprise entre 0 et {maze.nbRow-1}. Elle est ici de {y}.')

    return True

## Function test if cell is in maze without error
def isInMazeWithoutError(maze:Maze,coord:tuple)->bool:

    # Test type of parameters
    if ( not isMaze(maze) ) : raise ValueError("La valeur rentré en temps que maze n'est pas de type Maze.")
    if ( not isTuple(coord) ) : raise ValueError ("La valeur rentré en temps que coord n'est pas de type tuple.")

    x = coord[0]
    y = coord[1]

    return ( x >= 0 and x < maze.nbColumn and y >= 0 and y < maze.nbRow)


# Function convert data

## Function convert orientation ( str ) in tuple
def dirConvert(orientation: str) -> tuple:
    
    # Test type of parameters
    if ( not isDirection(orientation) ) : raise ValueError (f"La valeur rentré n'est pas une direction valide. La valeur doit être {' '.join(LS_DIRECTION)}. Elle est ici de {orientation} ")

    r = ""
    if (orientation == 'N'):
        r = (-1, 0)
    elif (orientation == 'S'):
        r = (1, 0)
    elif (orientation == 'W'):
        r = (0, -1)
    elif (orientation == 'E'):
        r = (0, 1)
    return r

## Function convert tuple in orientation ( str )  
def tupleConvert(orientation: tuple) -> str:

    # Test type of parameters
    if ( not isTuple(orientation) ) : raise ValueError ("La valeur rentré en temps que coord n'est pas de type tuple.")

    r = ""
    if (orientation == (-1, 0)):
        r = 'N'
    elif (orientation == (1, 0)):
        r = 'S'
    elif (orientation == (0, -1)):
        r = 'W'
    elif (orientation == (0, 1)):
        r = 'E'

    return r

## Function convert orientation ( str ) in is opposite
def dirInvert(orientation: str) -> tuple:

    # Test type of parameters
    if ( not isDirection(orientation) ) : raise ValueError (f"La valeur rentré n'est pas une direction valide. La valeur doit être {' '.join(LS_DIRECTION)}. Elle est ici de {orientation} ")

    r = ""
    if (orientation == 'N'):
        r = "S"
    elif (orientation == 'S'):
        r = "N"
    elif (orientation == 'W'):
        r = "E"
    elif (orientation == 'E'):
        r = "W"
    return r

## Function convert right orientation of orientation 
def dirDroite(orientation: str) -> tuple:
    r = ""
    if (orientation == 'N'):
        r = "E"
    elif (orientation == 'S'):
        r = "W"
    elif (orientation == 'W'):
        r = "N"
    elif (orientation == 'E'):
        r = "S"
    return r


# Function opération on tuple

## Function add two tuples
def addTuple(coord:tuple,dir:tuple)->tuple:
    return (coord[0] + dir[0], coord[1] + dir[1])

## Function substract two tuples
def subTuple(coord1:tuple,coord2:tuple)->tuple:
    return (coord1[0] - coord2[0], coord1[1] - coord2[1])


# Function getter cells

## Function get all cells around coord
def getNeighbour(maze:Maze,coord:tuple)->list:
    if ( not isInMaze(maze,coord) ) : raise ValueError('Cette cellule n est pas dans le labyrinthe')
    r = []
    for orientation in LS_DIRECTION:
        neighbour = addTuple(coord,dirConvert(orientation))
        if ( isInMazeWithoutError(maze,neighbour) ):
            r.append(neighbour)
    return r


# Function other

## Function get vector planaire of orientation
def getPlanaire(orientation:str)->tuple:
    # Test type of parameters
    if ( not isDirection(orientation) ) : raise ValueError (f"La valeur rentré n'est pas une direction valide. La valeur doit être {' '.join(LS_DIRECTION)}. Elle est ici de {orientation} ")

    if (orientation == 'N'):
        r = (0, 0.8)
    elif (orientation == 'S'):
        r = (0,-0.8)
    elif (orientation == 'W'):
        r = (-0.8,0)
    elif (orientation == 'E'):
        r = (0.8,0)
    return r

## Function clear console    
def clearConsole()->None:
    os.system('cls')

## Function construct bitmap from maze
def constructBitMap(maze:Maze)->list:

    r = []
    row = [True]
    for x in range(maze.nbColumn):
        if maze.maze[0][x].walls['N']:
            row.append(True)
        else:
            row.append(False)
        row.append(True)

    r.append(row)


    for y in range(maze.nbRow):
        row = [True]
        for x in range(maze.nbColumn):

            row.append(False)
            if maze.maze[y][x].walls['E']:
                row.append(True)
            else:
                row.append(False)
        r.append(row)
        
        
        row = [True]

        for x in range(maze.nbColumn):
            if maze.maze[y][x].walls['S']:
                row.append(True)
            else:
                row.append(False)
            row.append(True)
        r.append(row)

    return r


# Function render

## Function render maze in 3D using DDA
def print3DMaze(bitmap:list,coord:tuple,orientation:str)->None:

    plane = getPlanaire(orientation)
    lsRay = []

    # For all ray
    for i in range(MAX_RAY):

        # Calcul direction of ray
        cam = ( 2 * i ) / MAX_RAY - 1
        directionVector = dirConvert(orientation)
        rayDir = [ directionVector[0] + plane[0] * cam , directionVector[1] + plane[1] * cam ]

        mapCoord = [ int(coord[0]) , int(coord[1]) ]
        deltaDist = [ 0,0 ]


        if ( rayDir[0] == 0 ) :
            deltaDist[0] = float('inf')
        else:
            deltaDist[0] = abs( 1 / rayDir[0] )

        if ( rayDir[1] == 0 ) :
            deltaDist[1] = float('inf')
        else:
            deltaDist[1] = abs( 1 / rayDir[1] )

        # Create variables
        sideDist = [ 0,0 ]
        step = [ 0,0 ]

        hit = False
        side = False

        # Change sideStep and step with delta
        if ( rayDir[0] < 0 ):
            step[0] = -1
            sideDist[0] = ( coord[0] - mapCoord[0] ) * deltaDist[0]
        else:
            step[0] = 1
            sideDist[0] = ( -coord[0] + mapCoord[0] + 1 ) * deltaDist[0]

        if ( rayDir[1] < 0 ):
            step[1] = -1
            sideDist[1] = ( coord[1] - mapCoord[1] ) * deltaDist[1]
        else:
            step[1] = 1
            sideDist[1] = ( -coord[1] + mapCoord[1] + 1 ) * deltaDist[1]

        # While not touch, go forward
        while ( not hit ):

            if ( sideDist[0] < sideDist[1] ):
                sideDist[0] += deltaDist[0]
                mapCoord[0] += step[0]
                side = True
            else:
                sideDist[1] += deltaDist[1]
                mapCoord[1] += step[1]
                side = False

            if ( bitmap[mapCoord[0]][mapCoord[1]]):
                hit = True

        wallDist = 0

        if ( side ):
            wallDist = sideDist[0] - deltaDist[0]
        else:
            wallDist = sideDist[1] - deltaDist[1]

        if wallDist > MAX_RANGE: wallDist = MAX_RANGE

        wallHeight = int( HEIGHT / wallDist )
        lsRay.append(wallDist)

    
    r = ""

    for y in range(HEIGHT):

        for x in range(WIDTH):
            wallDist = lsRay[x]
            wallHeight = int( HEIGHT / wallDist )

            if ( y >= -wallHeight / 2 + HEIGHT/2 and y <= wallHeight /2 + HEIGHT/2):
                r += LS_DEGRADE[int((wallDist * len(LS_DEGRADE)-1) // MAX_RANGE )]
            else:
                r += " "

        r+= "\n"

    print(r)
    return


# Function change maze

## Function clear wall to remove wall
def clearWall(maze:Maze,coord:tuple,orientation:str)->None:

    co = (coord[1],coord[0])
    
    if ( not isInMaze(maze,coord) ) : raise ValueError('Cette cellule n est pas dans le labyrinthe')

    maze.maze[co[0]][co[1]].walls[orientation] = False

    nextCell = addTuple(co,dirConvert(orientation))

    if ( isInMazeWithoutError(maze,nextCell) ):
        maze.maze[nextCell[0]][nextCell[1]].walls[dirInvert(orientation)] = False

    return

## Function to create maze
def arbreBinaire(maze:Maze)->Maze:

    for y in range(maze.nbRow):
        for x in range(maze.nbColumn):

            if ( x != maze.nbColumn-1 or y != maze.nbRow-1 ):

                if (  x == maze.nbColumn-1 ):
                    clearWall(maze,(x,y),'S')

                elif (  y == maze.nbRow-1 ):
                    clearWall(maze,(x,y),'E')

                else:
                    d = choice(['E','S'])
                    clearWall(maze,(x,y),d)

    return maze

