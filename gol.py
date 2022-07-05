from random import choice, random, randrange


GENERATION_COUNT = 4
POPULATION_THRESHOLD = .45
CELL_ALIVE = 1
CELL_DEAD = 0

CONSTRUCTS = {"blinker":  [[0, 1, 0], \
                           [0, 1, 0], \
                           [0, 1, 0]],

                "glider": [[0, 1, 0], \
                           [0, 0, 1], \
                           [1, 1, 1]]}
CONSTRUCT_COUNT = 4

SCREEN_WIDTH = 250
SCREEN_HEIGHT = 112

def populate_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col] = CELL_ALIVE if random() < POPULATION_THRESHOLD else CELL_DEAD

def copy_grid_to(grid, new_grid):
    for row in range(SCREEN_HEIGHT):
        for col in range(SCREEN_WIDTH):
            new_grid[row][col] = grid[row][col]

def update_grid_to(grid, new_grid):
    for row in range(SCREEN_HEIGHT):
        for col in range(SCREEN_WIDTH):
            total = grid[row][(col - 1) % SCREEN_WIDTH] + \
                    grid[row][(col + 1) % SCREEN_WIDTH] + \
                    grid[(row - 1) % SCREEN_HEIGHT][col] + \
                    grid[(row + 1) % SCREEN_HEIGHT][col] + \
                    grid[(row - 1) % SCREEN_HEIGHT][(col - 1) % SCREEN_WIDTH] + \
                    grid[(row - 1) % SCREEN_HEIGHT][(col + 1) % SCREEN_WIDTH] + \
                    grid[(row + 1) % SCREEN_HEIGHT][(col - 1) % SCREEN_WIDTH] + \
                    grid[(row + 1) % SCREEN_HEIGHT][(col + 1) % SCREEN_WIDTH]

            if grid[row][col] == CELL_ALIVE:
                if total < 2 or total > 3:
                    new_grid[row][col] = CELL_DEAD
            elif total == 3:
                    new_grid[row][col] = CELL_ALIVE

def add_construct_to(construct_type, row_pos, col_pos, grid):
    construct = CONSTRUCTS[construct_type]
    for row in range(len(construct)):
        for col in range(len(construct[row])):
            grid[(row_pos + row) % SCREEN_HEIGHT][(col_pos + col) % SCREEN_WIDTH] = construct[row][col]

def populate_with_constructs(grid):
    for _ in range(CONSTRUCT_COUNT):
        construct = choice(list(CONSTRUCTS.keys()))
        add_construct_to(construct, randrange(SCREEN_HEIGHT + 1), randrange(SCREEN_WIDTH + 1), grid)

def game_of_life(grid, grid_copy):
    copy_grid_to(grid, grid_copy)
    update_grid_to(grid, grid_copy)
    copy_grid_to(grid_copy, grid)

def setup(grid):
    populate_grid(grid)
    populate_with_constructs(grid)

def game():
    grid = [[None for x in range(SCREEN_WIDTH)] for y in range(SCREEN_HEIGHT)]
    grid_copy = [[None for x in range(SCREEN_WIDTH)] for y in range(SCREEN_HEIGHT)]

    setup(grid)
    for _ in range(GENERATION_COUNT):
        game_of_life(grid, grid_copy)
