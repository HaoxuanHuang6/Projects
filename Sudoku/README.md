## How To Set Up And Run The Game
1. In the file <i>matrix.txt</i>, DIY your own sudoku. Type any number between 0-9 at every position, and make sure your sudoku is solvable.
Numbers 1-9 will be displayed as itself in the game, and 0 will be displayed as blank.
2. Make sure you have pygame and os installed
3. Open the <i>Sudoku</i> folder in your editor, then run <i>sudoku.py</i> to open the game.
(If you see FileNotFoundError, please make sure you open the <i>Sudoku</i> folder in your editor. If this cannot solve the problem, you can change the path in the following code to the path that can open the file <i>matrix.txt</i>)
```
with open (os.path.abspath("matrix.txt")) as file:
    matrix = file.read()
            |
            |
            |
            |
            V
with open (os.path.abspath("YOUR PATH TO matrix.txt")) as file:
    matrix = file.read()
```

## How To Play The Game
Click your right mouse key and click a number on your keyboard to change the number on the game board. If clicking the number doesn't make any change, re-click your right mouse key and input your number again.
```
Note: You can change numbers at any position, including those being set up initially.
Winning Condition: To solve the puzzle, you need to fill in the blank squares with numbers ranging from 1 to 9. The catch is that each square must contain a value that is unique to that row, column, and box.
```
