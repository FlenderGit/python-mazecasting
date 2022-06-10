from lib2to3.pgen2.token import TILDE
from Cell import Cell
from Maze import Maze
from const import *
import utils as utils
from time import sleep

# Variables
nbRay = MAX_RAY
state = True

maze = Maze(5,5)

direction = 'E'
x = 0.5
y = 0.5


# Create maze
maze = utils.arbreBinaire(maze)

# Shape maze
bitmap = utils.constructBitMap(maze)


utils.clearConsole()

print("\n".join(TITLE))

input("Press enter to start... ")



# Game
while ( state ):

    # Print for current coord
    utils.clearConsole()
    utils.print3DMaze(bitmap,(y*2+.5,x*2+.5),direction)
    

    # Informations + ask new direction
    print("Vous êtes en " , x , y , '. Direction : ' , direction)
    change = input("Dans quelle direction veux-tu aller ? (Z,Q,S,D) ").upper()


    # Create vector null if coord not change
    vector = (0,0)
    
    # Check input
    if ( change == 'S' ):
        newDirection = utils.dirInvert(direction)
    elif ( change == 'Z'):
        newDirection = direction
        vector = utils.dirConvert(newDirection)
    elif ( change == 'D'):
        newDirection = utils.dirDroite(direction)
    elif ( change == 'Q'):
        newDirection = utils.dirInvert(utils.dirDroite(direction))

    direction = newDirection

    # get next cell
    newCell = utils.addTuple((y,x),(vector[0],vector[1]))

    # get cell for test collision
    testCell = utils.addTuple((y,x),(vector[0]/2,vector[1]/2))

    # Test collision and newCell not outside
    if ( not utils.isInMazeWithoutError(maze,newCell) or bitmap[int(testCell[0]*2)][int(testCell[1]*2)]):
        print("Cette direction est impossible...")
    else:

        # Animation
        if ( change == 'Z'):
            utils.clearConsole()
            utils.print3DMaze(bitmap,(testCell[0]*2+.5,testCell[1]*2+.5),direction)
            sleep(.5)

        # Add coord
        x = newCell[1]
        y = newCell[0]