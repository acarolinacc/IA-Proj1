# Cogito Game

Step into the world of Cogito, a mesmerizing puzzle game for Windows that rekindles the essence of the classic Milton Bradley board game. Your mission: skillfully manipulate vertical and horizontal levers to rearrange pieces, aligning them perfectly to solve an intricate pattern.

Official game website: https://www.myabandonware.com/game/cogito-1d4

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

IMAGE

Play: Dive into the game and commence your puzzle-solving journey.
Mode: Watch an AI-powered bot untangle the puzzles.

### Bot Algorithm

If you choose to let a bot play, you can select the algorithm it uses to solve the puzzles. 
The options are:

- DFS (Depth-First Search)
- BFS (Breadth-First Search)
- Iterative Deepening
- Uniform Cost Search
- Greedy
- A* (A-Star)

IMAGE

### Heuristics Explained

In the "Greedy" and "A*" search algorithms for the Cogito game, the Manhattan distance heuristic is used. This heuristic calculates the total distance each piece must move on the grid to reach its goal position, moving only horizontally or vertically.

Greedy Search: Chooses moves that seem closest to the goal, based on the Manhattan distance, prioritizing immediate progress towards the goal without considering the path cost.

A Search:* Combines the path cost from the start node with the Manhattan distance to the goal, balancing both the traveled path and the estimated distance to the goal, ensuring an optimal solution is found.

IMAGE

## Controls

### Menu
- Move up and down with the arrows
- 'Enter' to select an option
- 'ESC' to go back to the previous menu

### In-Game
- Move around with the arrows (up, down, left or right)
- Press 'Enter' to make a move

Immerse yourself in the strategic depths of Cogito, where every move is a step towards mastering this enthralling puzzle game.