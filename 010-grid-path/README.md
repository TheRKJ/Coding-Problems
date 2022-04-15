A new neurone path has generated in my mind. For that reason, I have decided that we will solve two tasks in the gridpath problem.

## Task-1:

Here we want to count all the possible paths from starting cell to ending cell of a [m x n] grid with the constraints that from each cell you can either move only to right or down.

**For example:**  
let grid
| | | |
| :---: | :---: | :---: |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Then number of possible paths: 6


## Task-2:

Here we want to print all the possible paths from starting cell to ending cell of a [m x n] grid with the constraints that from each cell you can either move only to right or down.

**For example:**  
let grid
| | | |
| :---: | :---: | :---: |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Then the possible paths are:  
[1, 2, 3, 6, 9]  
[1, 2, 5, 6, 9]  
[1, 2, 5, 8, 9]  
[1, 4, 5, 6, 9]  
[1, 4, 5, 8, 9]  
[1, 4, 7, 8, 9]