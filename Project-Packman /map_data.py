map_data = [
    [4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [1, 7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 1],
    [1, 7, 4, 3, 7, 4, 3, 7, 4, 2, 2, 2, 2, 3, 7, 4, 3, 7, 4, 3, 7, 4, 3, 7, 4, 2, 2, 3, 7, 1],
    [1, 7, 1, 1, 7, 1, 1, 7, 5, 2, 2, 2, 2, 6, 7, 1, 1, 7, 1, 1, 7, 1, 1, 7, 1, 99, 99, 1, 7, 1],
    [1, 7, 1, 1, 7, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 5, 6, 7, 1, 1, 7, 5, 6, 7, 5, 2, 2, 6, 7, 1],
    [1, 7, 1, 1, 7, 7, 7, 7, 4, 2, 2, 2, 2, 3, 7, 7, 7, 7, 1, 1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1],
    [1, 7, 1, 1, 7, 4, 2, 2, 6, 99, 99, 99, 99, 5, 2, 2, 3, 7, 1, 1, 7, 7, 4, 3, 7, 4, 3, 7, 4, 6],
    [1, 7, 5, 6, 7, 5, 2, 2, 2, 2, 3, 4, 2, 2, 2, 2, 6, 7, 5, 6, 7, 7, 1, 1, 7, 5, 6, 7, 5, 3],
    [1, 8, 7, 7, 7, 7, 0, 0, 0, 0, 5, 6, 0, 0, 0, 0, 7, 7, 7, 7, 8, 7, 1, 1, 7, 7, 7, 7, 7, 1],
    [1, 7, 4, 2, 3, 7, 4, 3, 0, 0, 0, 0, 0, 4, 2, 3, 7, 4, 3, 7, 4, 3, 5, 6, 7, 4, 2, 3, 7, 1],
    [1, 7, 5, 2, 6, 7, 5, 6, 0, 4, 9, 9, 3, 5, 2, 6, 7, 5, 6, 7, 1, 1, 7, 7, 7, 5, 2, 6, 7, 1],
    [1, 7, 7, 7, 7, 7, 7, 7, 7, 1, 10, 11, 1, 7, 7, 7, 7, 7, 7, 7, 1, 1, 7, 7, 7, 8, 7, 7, 7, 1],
    [1, 7, 4, 3, 7, 4, 2, 3, 7, 5, 2, 2, 6, 7, 4, 3, 7, 4, 3, 7, 5, 6, 7, 4, 3, 7, 4, 2, 3, 1],
    [1, 7, 5, 6, 7, 5, 3, 1, 7, 7, 7, 7, 7, 7, 5, 6, 7, 5, 6, 7, 7, 7, 7, 5, 6, 7, 1, 99, 1, 1],
    [1, 7, 7, 7, 7, 7, 1, 1, 7, 4, 2, 2, 3, 7, 7, 7, 7, 7, 7, 7, 4, 3, 7, 7, 7, 7, 1, 99, 1, 1],
    [1, 7, 4, 2, 3, 7, 5, 6, 7, 5, 2, 2, 6, 7, 4, 2, 3, 7, 7, 4, 6, 1, 7, 7, 4, 2, 6, 99, 1, 1],
    [1, 7, 1, 99, 1, 7, 7, 7, 8, 7, 7, 7, 7, 7, 1, 99, 1, 7, 7, 1, 99, 1, 7, 7, 5, 2, 2, 2, 6, 1],
    [5, 2, 6, 99, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 99, 5, 2, 2, 6, 99, 5, 2, 2, 2, 2, 2, 2, 2, 6],
]

positions = [(x, y) for y in range(len(map_data)) for x in range(len(map_data[y])) if map_data[y][x] == 55]
print(positions)

