**N-Queens Problem Solver**

### Overview:

This GitHub repository contains a Python implementation of various algorithms to solve the N-Queens problem. The N-Queens problem involves placing N chess queens on an N×N chessboard in such a way that no two queens threaten each other. The implemented algorithms include steepest-ascent hill climbing, hill climbing with sideways moves, random restart hill climbing without sideways, and random restart hill climbing with sideways moves.

### Files:

1. **queens_solver.py:**
   - Contains the main implementation of the N-Queens problem solver.
   - Includes classes for representing the chessboard, functions for heuristics calculation, and various hill climbing algorithms.

2. **README.md:**
   - Provides essential information about the repository, including an overview, file descriptions, and instructions for running the program.

### Instructions:

1. **Requirements:**
   - Ensure you have Python installed on your machine (version 3.x).

2. **Running the Program:**
   - Execute `queens_solver.py` to run the N-Queens problem solver.
   - Follow the prompts to enter the value of N for the chessboard.

3. **Experimentation:**
   - Modify the parameters in the `main()` function of `queens_solver.py` for experimentation.
   - Explore success rates, average steps, and random restart statistics for different algorithms.

### Results:

- The program outputs success rates, average steps, and other relevant statistics for each algorithm based on 500 attempts.
- Results for steepest-ascent hill climbing, hill climbing with sideways moves, random restart hill climbing without sideways, and random restart hill climbing with sideways moves are provided.

### Acknowledgments:

This implementation is a part of the exploration of search algorithms for problem-solving. It is inspired by the N-Queens problem and aims to showcase various strategies to find solutions.

### License:

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it according to the terms of the license.

### Feedback and Contributions:

Feedback and contributions are welcome! If you encounter issues or have suggestions for improvements, please open an issue or submit a pull request. Let's collaborate to make this N-Queens problem solver even better!
