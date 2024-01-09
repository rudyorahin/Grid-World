# Grid World

## Description

Grid World is an interactive Python application that uses AI methodologies to find the fastest route in a grid environment. The application visually demonstrates various pathfinding algorithms navigating from a start point (yellow node) to a goal point (orange node). The grid contains different terrains like grass (green nodes, representing high cost) and puddles (blue nodes, which are impassable), challenging the pathfinding process.

## Features

- **AI-Based Pathfinding Algorithms:**
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - Uniform Cost Search (UCS)
  - A* Search using Manhattan Distance as the heuristic.
- **Interactive Grid Environment:**
  - Customizable grid to test different pathfinding scenarios.
  - Visually distinct nodes for different terrains and states.
- **Test Cases:**
  - Includes predefined test cases with random setups and specific patterns like spiral and zigzag.

## Installation

Ensure you have Python 3.\* and the latest pip (>= 20) installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/rudyorahin/GridWorld.git
   ```

2. Navigate to the project directory:
   ```bash
   cd GridWorld
   ```

3. Install required packages (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application:

```bash
python main.py -l [test case number]
```

Test case numbers:
- `0`: Random 1
- `1`: Random 2
- `2`: Spiral
- `3`: Zigzag

## Contributing

Contributions to enhance Grid World are welcome. Please read the contributing guidelines before submitting your pull requests.

## License

Copyright © 2024 Rudy Orahin.

Licensed under the MIT License. See `LICENSE` for more information.
