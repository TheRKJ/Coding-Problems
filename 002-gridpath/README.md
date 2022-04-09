Here we want to count all the possible paths from starting cell to ending cell of a [m x n] grid with the constraints that from each cell you can either move only to right or down.

For example:
let grid = [[1,2,3],
            [4,5,6],
            [7,8,9]]
Then number of possible paths: 6
[1, 2, 3, 6, 9]
[1, 2, 5, 6, 9]
[1, 2, 5, 8, 9]
[1, 4, 5, 6, 9]
[1, 4, 5, 8, 9]
[1, 4, 7, 8, 9]