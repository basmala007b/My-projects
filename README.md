# Snake Game with BFS Pathfinding - README

## Overview
This is a Python implementation of the classic Snake game with an AI twist - the snake uses Breadth-First Search (BFS) algorithm to find the shortest path to the food while avoiding obstacles. The game features colorful visuals and some debugging tools to visualize the pathfinding process.

## Features
- AI-controlled snake using BFS algorithm
- Obstacle avoidance
- Score tracking
- Visual pathfinding markers (toggle with keys)
- Colorful snake segments
- Custom GIF graphics for snake and food

## Requirements
- Python 3.x
- Turtle module (comes with Python standard library)
- Pillow library (for image processing - only needed if modifying graphics)

## Installation
1. Clone the repository or download the files
2. Ensure you have Python installed
3. Install Pillow if you want to modify graphics:
   ```
   pip install pillow
   ```

## Files
- `main.py`: Main game logic and BFS implementation
- `snake.py`: Snake class implementation
- `food.py`: Food class implementation
- `obs.py`: Obstacles class implementation
- `make.py`: Helper script for resizing images (optional)

## How to Run
Simply execute the `main.py` file:
```
python main.py
```

## Controls
- The snake moves automatically using the BFS algorithm
- Debugging controls:
  - `x`: Toggle pathfinding markers visibility
  - `z`: Show BFS exploration markers
  - `c`: Slow down the BFS visualization

## Game Rules
- The snake grows when it eats food
- The game ends if the snake hits an obstacle or itself
- Score increases by 1 for each food eaten

## Customization
You can modify:
- Game speed by adjusting the timers in `main.py`
- Number of obstacles by changing the parameter in `Obs()` initialization
- Colors throughout the various classes
- GIF paths to use your own images

## Known Issues
- The snake may get stuck in certain obstacle configurations
- Pathfinding visualization can slow down the game

## Future Improvements
- Implement different pathfinding algorithms
- Add difficulty levels
- Add sound effects
- Implement high score tracking

Enjoy the game!
