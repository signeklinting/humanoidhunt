# Solution to Puzzle 3 of the Humanoid Hunt
# Created by Signe Klinting
# 2021-01-09

from collections import defaultdict


neurons = [line.strip() for line in open("input.txt", "r+").readlines()]


# directions
directions = {
    "R": (1, 0), 
    "L": (-1, 0),
    "D": (0, 1),
    "U": (0, -1), 
    (1, 0): "R",
    (-1, 0): "L",
    (0, 1): "D",
    (0, -1): "U",
}


# Converting the directions in the strands to coordinates
M = defaultdict(list)
for neuron in neurons:
    try:
        start, strand = neuron.split(" ")
        start = tuple(int(i) for i in start.split(","))
        coord = start
        for move in strand.split(","):
            if move in directions:
                move_coord = (coord[0] + directions[move][0], coord[1] + directions[move][1])
                coord = move_coord
                M[start].append(move_coord)
            else:
                M[start].append(move)
                break
    except ValueError:
        start = tuple(int(i) for i in neuron.split(","))
        M[start]


# Making a graph of the neural network (bi-directional)
N = defaultdict(set)
coords = set()

for start, strand in M.items():    
    coords.add(start)
    for i, p in enumerate(strand):
        if p != "X":
            coords.add(p)
            if i == 0:
                N[p].add(start)
                N[p].add(strand[i + 1])
            elif i == len(strand) - 1:
                N[p].add(strand[i - 1])
            else:
                N[p].add(strand[i - 1])
                if strand[i + 1] != "X":
                    N[p].add(strand[i + 1])
    try:
        N[start].add(strand[0])
    except:
        N[start]


# Adding adjancent neurons to graph
for c in coords:
    if isinstance(c, tuple):
        for move in ["R", "L", "U", "D"]:
            adjacent = (c[0] + directions[move][0], c[1] + directions[move][1])
            if adjacent in coords:
                N[c].add(adjacent)


# Doing a breadth first search to find shortest way to the finish area
queue = [["S"]]
visited = {"S"}

while queue:
    path = queue.pop()
    current_coord = path[-1]
    new_coords = N[current_coord]
    
    for new_coord in new_coords:
        if new_coord == "F":
            complete_path = path
            break
        elif new_coord not in visited:
            visited.add(new_coord)
            queue.insert(0, path + [new_coord])
    else:
        continue
    break

# Start and finish points of the path
print(len(complete_path))
print(complete_path[1], complete_path[-1])

# Converting coordinates to directions
prev_coord = complete_path[1]
for coord in complete_path[2:]:
    step = (coord[0] - prev_coord[0], coord[1] - prev_coord[1])
    prev_coord = coord
    print(directions[step], end="")