# Huarongdao Puzzle Solver
A Huarongdao puzzle solver utilizing A* and DFS algorithms.

To run the solver, execute the following command in the terminal: 
```python3 hrd.py <input_file> <DFS_output_file> <A*_output_file>```


## Input Format
The input file is a plain text file containing an initial Huarongdao puzzle configuration. The example below demonstrates the content of the input file. It consists of 20 digits arranged in 5 rows and 4 columns, representing the initial puzzle configuration. Empty squares are represented by 0. Single pieces are represented by 7. The 2x2 piece is represented by 1. The 1x2 pieces are represented by a randomly assigned number from the set {2, 3, 4, 5, 6}.
```
2113
2113
4665
4775
7007
```

## Output Format
The two output files store the DFS and A* solutions for the provided input file.

The example below shows the content of an output file. The first line displays the cost of the solution. Following that, the sequence of states from the initial configuration to the goal state is printed. An empty line separates two consecutive states. Empty squares are represented by 0. Single pieces are represented by 4. The 2x2 piece is represented by 1. Horizontal 1x2 pieces are represented by 2. Vertical 1x2 pieces are represented by 3. Due to space limitations, only the beginning of the output file is shown below.

Cost of the solution: 116
```
3113
3113
3223
3443
```
