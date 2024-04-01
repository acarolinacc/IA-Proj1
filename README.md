# Cogito Game

Step into the world of Cogito, a mesmerizing puzzle game for Windows that rekindles the essence of the classic Milton Bradley board game. Your mission: skillfully manipulate vertical and horizontal levers to rearrange pieces, aligning them perfectly to solve an intricate pattern.

Official game website: https://www.myabandonware.com/game/cogito-1d4

![Game](Assets/images/game.png)

## Compilation & Running Instructions

To run the game, you will need to have Python installed on your computer, as well as the Pygame library, which is used for the game's graphical interface.

### Prerequisites
Ensure you have the following installed to embark on the Cogito adventure:

- Python 
- Pygame library

Install Pygame using pip if it's not already set up:

```sh
pip install pygame
```

## Launching the Game

To start the game, execute the main.py file with Python. You can do this using your preferred IDE or from the command line as follows:

```sh
python main.py
```

## Gameplay Instructions

Upon launching Cogito, the main menu unfolds with options beckoning your choice:

![Menu](Assets/images/main_menu.png)

Play: Dive into the game and commence your puzzle-solving journey.

PC Solve: Watch an AI-powered bot untangle the puzzles.

### Bot Algorithm

If you choose to let a bot play, you can select the algorithm it uses to solve the puzzles. 
The options are:

- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Iterative Deepening
- Uniform Cost Search
- Greedy
- A* (A-Star)

![Algoritmos](Assets/images/algoritmos.png)

In the "Greedy" and "A*" search algorithms for the Cogito game, two heuristics are often used: the Manhattan distance and the Out of Place Cells.

**Manhattan Distance Heuristic**: This heuristic calculates the total distance each piece must move on the grid to reach its goal position, moving only horizontally or vertically. It is effective in gauging how close each piece is to its final destination.

  Greedy Search: Chooses moves that seem closest to the goal, based on the Manhattan distance, prioritizing immediate progress towards the goal without considering the path cost.

  A Search*: Combines the path cost from the start node with the Manhattan distance to the goal. This balances both the traveled path and the estimated distance to the goal, ensuring an optimal solution is found.

**Out of Place Cells Heuristic**: This heuristic counts the number of pieces that are not in their goal position. It provides a straightforward measure of how many pieces are incorrectly placed, regardless of their distance from the correct position.

  Greedy Search: Using this heuristic, Greedy Search will prioritize moves that result in the fewest number of pieces being out of place, aiming for a state where all pieces are in their correct positions.

  A Search*: When applied in A* Search, this heuristic helps to balance between the cost of the path taken and the number of pieces that still need to be moved to their correct positions. It aids in finding an efficient path that reduces the number of out of place pieces as quickly as possible.

![Heuristicas](Assets/images/heuristicas.png)


## Controls

### Menu
- Move up and down with the arrows
- 'Enter' to select an option
- 'ESC' to go back to the previous menu

### In-Game
- Choose an row/column with the keyboard arrows (up, down, left or right) or with the mouse (by clicking on the desired arrow)
- Press 'Enter' to make a move

Immerse yourself in the strategic depths of Cogito, where every move is a step towards mastering this enthralling puzzle game.
