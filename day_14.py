import numpy as np
import matplotlib.pyplot as plt

map_ = []
for row in range(200):
    map_.append([0 for i in range(100)])

with open('data/day_14ex.txt') as handle:
    lines = handle.readlines()
    lines = [line[:-1] for line in lines]

with open('data/day_14.txt') as handle:
    lines = handle.readlines()
    lines = [line[:-1] for line in lines]


def generate_line(start, end):
    """ generate line of number between 2 points """

    # ascend flow
    if start < end: 
        line = list(range(start, end + 1))
    # descend
    else:
        line = list(range(start, end - 1, -1))

    return line

def generate_wall(lines):
    wall_coords = []

    # generate walls
    for line in lines:
        str_vertexes = (line.split(' -> '))
        vertexes = [vertex.split(',') for vertex in str_vertexes]
        vertexes = [(int(vertex[0]), int(vertex[1])) for vertex in vertexes]
        
        # processes every edge in vertexes
        for i in range(len(vertexes) - 1):
            vertex_a = vertexes[i]
            vertex_b = vertexes[i+1]

            vert_a_col, vert_a_row = vertex_a
            vert_b_col, vert_b_row = vertex_b

            # generate row coords
            if vert_a_col == vert_b_col:
                row_coords = generate_line(vert_a_row, vert_b_row)
                edge_coords = [(vert_a_col, row) for row in row_coords]
                wall_coords = wall_coords + edge_coords

            # generate col coords
            else:
                col_coords = generate_line(vert_a_col, vert_b_col)
                edge_coords = [(col, vert_a_row) for col in col_coords]
                wall_coords = wall_coords + edge_coords

    wall_coords = list(set(wall_coords))

    return wall_coords


# draw visual
def draw(step):
    canvas = np.zeros((200, 100), dtype='uint8')
    for coord in wall_coords:
        c = coord[0] - 450
        r = coord[1]
        canvas[r, c] = 5

    for coord in sand_coords:
        if (0 <= coord[1] <= 199) and (0 <= coord[0]-450 <= 99):
            c = coord[0] - 450
            r = coord[1]
            canvas[r, c] = 1

    plt.imsave(f'./day14_{step}.png', canvas)


### sand simulation
wall_coords = generate_wall(lines)
sand_coords = []
VOID = max([wall[1] for wall in wall_coords])  # 176
GROUND = VOID + 1
END = (500, 0)
POURING = True
steps = 0

while POURING is True:
    unit_done = False
    pos = (500, 0)  # start position

    if pos in sand_coords:
        print('complete!')
        break

    if steps % 2000 == 0:
        draw(steps)

    # sand unit pour
    while unit_done is False:

        # checks!
        down = (pos[0], pos[1] + 1)
        downleft = (pos[0] - 1, pos[1] + 1)
        downright = (pos[0] + 1, pos[1] + 1)

        if (down not in wall_coords) and (down not in sand_coords):
            # check if ground level reached
            if down[1] == GROUND:
                sand_coords.append(down)
                unit_done = True
            else:
                pos = down
        elif (downleft not in wall_coords) and (downleft not in sand_coords):
            # check if ground level reached
            if downleft[1] == GROUND:
                sand_coords.append(downleft)
                unit_done = True
            else:
                pos = downleft
        elif (downright not in wall_coords) and (downright not in sand_coords):
            # check if ground level reached
            if downright[1] == GROUND:
                sand_coords.append(downright)
                unit_done = True
            else:
                pos = downright
        else:
            unit_done = True
            sand_coords.append(pos)
    
    steps += 1

print('done')
