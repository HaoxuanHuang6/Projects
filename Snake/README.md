## This Project Is Based On 
```
https://github.com/jl4r1991/SnakeQlearning/tree/master
```

## Changes
The original project only implemented Q-learning for the game Snake. This version adds the Sarsa algorithm and compares the performance between Sarsa and Q-learning.
After running both algorithms, the rolling 30 average calculation is applied to make data look more comparable.

## Dependencies
Code is written in python 3.<br>
The only extra dependecies are:
- Pygame
```
pip3 install pygame
```
- Depending on the Python version, may need to install dataclasses
```
pip3 install dataclasses
```

## To Run This Experiment
1. Run the following file to initialize the Q Table. If the text file <i>qvalues.json</i> does not exits in the folder, it will generate one after running the file.
```
python3 InitializeQvalues.py
```
2. Run <i>snake.py</i>.<br>
In <i>snake.py</i> set the constant FRAMESPEED with different number can control the game speed.
Set this to a smaller number (20-30) to better watch the snake's movements.
```
python3 snake.py
```
