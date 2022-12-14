lines = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2'  # hit count 9
]

lines = [  # ex2
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20'
]

with open('data/day_9.txt') as handle:
    lines = [line[:-1] for line in handle.readlines()]

def offside(row, col, tail):
    """ 
    get head border, returns True if tail out of range
    123
    894
    765
    """
    adjacent_position = [
        [row+1, col-1],
        [row+1, col],
        [row+1, col+1],
        [row, col+1],
        [row-1, col+1],
        [row-1, col],
        [row-1, col-1],
        [row, col-1],
        [row, col]
    ]
    
    if tail not in adjacent_position:
        return True
    
    return False

def next_position(h_row, h_col, t_row, t_col):

    if h_row == t_row or h_col == t_col:  # common row/col flow
        if h_row > t_row:  # up
            return [t_row + 1, t_col]

        elif h_col > t_col:  # right
            return [t_row, t_col + 1]

        elif h_row < t_row:  # down
            return [t_row - 1, t_col]

        else:  # left
            return [t_row, t_col -1]
    # diagonal flow
    else:
        if h_row > t_row and h_col > t_col:  # top right
            return [t_row + 1, t_col + 1]

        elif h_row < t_row and h_col > t_col:  # bottom right
            return [t_row - 1, t_col + 1]

        elif h_row < t_row and h_col < t_col:  # bottom left
            return [t_row - 1, t_col - 1]

        else:  # top left
            return [t_row + 1, t_col - 1]


def process_node(new_head, tail):
    # for node in nodes
    if offside(*new_head, tail):
        tail = next_position(*new_head, *tail)
        # tail_visits.append(tuple(tail))
    
    return tail

#--------------------------program-------------------------#
head = [0, 0]
tails = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tail_visits = []

for line in lines:
    # origin [row, col] - start: bottom-left
    direction, amount = line.split()
    amount = int(amount)
    
    if direction == 'R':
        for i in range(amount):

            new_head = [head[0], head[1] + 1]

            for pid in range(9, 0, -1):
                if pid == 9:
                    tails[pid-1] = process_node(new_head, tails[pid-1])
                else:
                    tails[pid-1] = process_node(tails[pid], tails[pid-1])

                # add tail visited
                if pid == 1:
                    tail_visits.append(tuple(tails[pid-1]))

            head = new_head
    
    elif direction == 'L':
        for i in range(amount):
            new_head = [head[0], head[1] - 1]
            
            for pid in range(9, 0, -1):
                if pid == 9:
                    tails[pid-1] = process_node(new_head, tails[pid-1])
                else:
                    tails[pid-1] = process_node(tails[pid], tails[pid-1])
                
                # add tail visited
                if pid == 1:
                    tail_visits.append(tuple(tails[pid-1]))

            head = new_head

    elif direction == 'U':
        for i in range(amount):
            new_head = [head[0] + 1, head[1]]
            
            for pid in range(9, 0, -1):
                if pid == 9:
                    tails[pid-1] = process_node(new_head, tails[pid-1])
                else:
                    tails[pid-1] = process_node(tails[pid], tails[pid-1])
                
                # add tail visited
                if pid == 1:
                    tail_visits.append(tuple(tails[pid-1]))

            head = new_head

    else:  # 'D'
        for i in range(amount):
            new_head = [head[0] - 1, head[1]]
            
            for pid in range(9, 0, -1):
                if pid == 9:
                    tails[pid-1] = process_node(new_head, tails[pid-1])
                else:
                    tails[pid-1] = process_node(tails[pid], tails[pid-1])
                
                # add tail visited
                if pid == 1:
                    tail_visits.append(tuple(tails[pid-1]))

            head = new_head

print('done')
print(len(set(tail_visits)))