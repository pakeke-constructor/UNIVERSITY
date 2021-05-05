"""A program to read a grid of weights from a file and compute the 
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards. 
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""
INFINITY = float('inf')  

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    # **** Your code goes here. It must compute a value 'best', which is
    # the minimum cost from the top of the grid to the bottom.
    
    cache = [[0]*n_cols for _ in range(n_rows)]
    # cache[ row ][ col ]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            weight = grid[row][col]
            if row != 0:
                weight += min((cache[row-1][col+x]) for x in range(-1,2) if (0 <= col+x < n_cols))
            cache[row][col] = weight
    return min(cache[-1])



def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))



print(file_cost("sm.txt"))
print(file_cost("t.txt"))
