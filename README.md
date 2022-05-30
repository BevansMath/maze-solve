# maze-solve
Implementation of Depth-First Search to find first available path through a randomly generated maze array of cells. 

# Goals
The goal of this project is to utilize depth first search to olve any number of complex mazes. Maze-Solve creates a blank window gui using the built-in python module tkinter, and begins drawing cells in a row-column fashion. Once the results of the maze is printed, it implements the depth-first search algorithm alongside the draw function and draws a line into its chosen path. The function will backtrack with a different line to show you how depth-first search behaves under these conditions. 

# Installation
Firstly, make sure you have python and git installed on your local machine. I did everything in VSCode, so make sure where you install the repository is under your current workspace path. Go to your workspace path and do the following.
```
# Clone the repository into your local machine
git clone https://github.com/BevansMath/maze-solve

# Change directory into directory of repository
cd maze-solve

# Run maze-solver
python3 main.py
```
# Stability 
I plan to update this code as much as possible. Coming extensions to the project may include implementation of different algorithms such as A*, Djikstra, and linear programming algorithms. The maze could also be extended into three dimensions, as well as having a separate gui to display how each algorithm behaves. 

# Contributing
I love collaborating and receiving tips on how my code can improve. If you see anything that you would like to improve on this code, feel free to fork the repo and open a pull request. Please ensure the code passes the existing tests, and write tests to see if the changes are applicable. Please submit all pull requests on the main branch.
