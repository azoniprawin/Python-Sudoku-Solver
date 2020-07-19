# Python Sudoku Solver
The backtracking approach is used to find a solution to any solvable sudoku board or writing programs that solve any 9x9 sudoku puzzles for you.
- Just put 2D List into **solve** method
- Call **display_board** method to see result
#### Video Link:
https://youtu.be/iCcR-y7rv7Y

### Example:
```
board = [
    [2,0,0,3,0,0,0,0,0],
    [8,0,4,0,6,2,0,0,3],
    [0,1,3,8,0,0,2,0,0],
    [0,0,0,0,2,0,3,9,0],
    [5,0,7,0,0,0,6,2,1],
    [0,3,2,0,0,6,0,0,0],
    [0,2,0,0,0,9,1,4,0],
    [6,0,1,2,5,0,8,0,9],
    [0,0,0,0,0,1,0,0,2]
]

solve(board)
display_board(board)

-------------------------
| 2 7 6 | 3 1 4 | 9 5 8 |
| 8 5 4 | 9 6 2 | 7 1 3 |
| 9 1 3 | 8 7 5 | 2 6 4 |
-------------------------
| 4 6 8 | 1 2 7 | 3 9 5 |
| 5 9 7 | 4 3 8 | 6 2 1 |
| 1 3 2 | 5 9 6 | 4 8 7 |
-------------------------
| 3 2 5 | 7 8 9 | 1 4 6 |
| 6 4 1 | 2 5 3 | 8 7 9 |
| 7 8 9 | 6 4 1 | 5 3 2 |
------------------------- 
```
