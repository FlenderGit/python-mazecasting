# MazeCasting
MazeCasting is a project to render a maze in 3D.

# Start the project
To play the game, launch the main.py file.
Use Z,Q,S,D to move around the maze.

# Informations
To achieve this result, the program performs the following actions.

1) Create a maze with class :
I used the binary tree method to randomly break walls and generate the maze.
_(Methode : utils.arbreBinaire(maze:Maze)->Maze )_
Link : http://weblog.jamisbuck.org/2011/2/1/maze-generation-binary-tree-algorithm

Result:
```
+---+---+---+---+---+  
|       |       |   |  
+---+   +---+   +   +  
|   |           |   |  
+   +---+---+   +   +  
|       |           |  
+---+   +---+---+   +  
|                   |  
+---+---+---+---+   +  
|                   |  
+---+---+---+---+---+
```


2) Convert this maze to bitmap
Construct bitmap using maze's data.
True mean wall, and False is empty.
_(Methode : utils.constructBitMap(maze:Maze)->list )_

Result:
```
[True , True , True , True , True , True , True , True , True , True , True]
[True , False, False, False, True , False, True , False, True , False, True]
[True , True , True , False, True , False, True , False, True , False, True]
[True , False, False, False, False, False, False, False, False, False, True]
[True , True , True , True , True , True , True , True , True , False, True]
[True , False, False, False, False, False, False, False, True , False, True]
[True , True , True , True , True , True , True , False, True , False, True]
[True , False, True , False, True , False, True , False, True , False, True]
[True , False, True , False, True , False, True , False, True , False, True]
[True , False, False, False, False, False, False, False, False, False, True]
[True , True , True , True , True , True , True , True , True , True , True]
```


3) Add movements to player
Change x,y and direction of player using inputs.

Result:
```
Vous êtes en  0.5 0.5 . Direction :  E
Dans quelle direction veux-tu aller ? (Z,Q,S,D)
```

4) Add Raycasting
Add an optimized raycasting algorithm with the DDA method and let the magic happen.
_(Methode : utils.print3DMaze(bitmap:list,coord:tuple,orientation:str)->None )_

```
WWMMMMMM####uuuunnn                                                               nnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxx                                                           xxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxr                                                       rxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjj                                                 jjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjft                                             tfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/                                         /ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/                                       |\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/                                     )(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/                                   }1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------                         ?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<                     <+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<!:                 :!<+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<!:                .:!<+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<!:                .:!<+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<!:                .:!<+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<!:                .:!<+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<!:                .:!<+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<!:                .:!<+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<!:                .:!<+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<!:                 :!<+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------+<                     <+?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/--------                         ?[}1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/                                   }1)(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/                                     )(|\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/                                       |\/ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjftt/                                         /ttfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjjft                                             tfjjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxrrjj                                                 jjrrxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxxxr                                                       rxxxnnnuuuu####MMMMMMW
WWMMMMMM####uuuunnnxx                                                           xxnnnuuuu####MMMMMMW
```
