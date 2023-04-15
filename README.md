# Huarongdao-Solver
Solver for Huarongdao puzzle using A* and DFS

Run terminal the follwoing command
python3 hrd.py  <input file>  <DFS output file>  <A* output file> 

Input Format
The input to your program is a plain text file that stores an initial Hua Rong Dao puzzle configuration. See below for an example of the input file content. It contains 20 digits arranged in 5 rows and 4 digits per row, representing the initial configuration of the puzzle. The empty squares are denoted by 0. The single pieces are denoted by 7. The 2x2 piece is denoted by 1. The 5 1x2 pieces are denoted by one of {2, 3, 4, 5, 6}, but the numbers are assigned at random.

2113

2113

4665

4775

7007
 

Output Format
The two output files should store the DFS and A* solution for the input file provided.

See below for an example of the content of the output file. On the first line, print the cost of the solution. Next, print the sequence of states from the initial configuration to a goal state. Two consecutive states are separated by an empty line. The empty squares are denoted by 0. The single pieces are denoted by 4. The 2x2 piece is denoted by 1. The horizontal 1x2 pieces are denoted by 2. The vertical 1x2 pieces are denoted by 3.  Due to limited space, we only show the beginning of the output file below. 

Cost of the solution: 116

3113

3113

3223

3443


