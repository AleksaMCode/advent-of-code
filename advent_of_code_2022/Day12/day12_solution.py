from collections import deque

matrix = {}
starts = []
start = end = (0, 0)


def build_matrix(file_name):
    global start, end
    with open(file_name) as file:
        for j, line in enumerate(file):
            for i, value in enumerate(line.strip()):
                matrix[(i, j)] = value

                match value:
                    case 'S':
                        start = (i, j)
                        starts.append(start)
                    case 'E':
                        end = (i, j)
                    case 'a':
                        starts.append((i, j))

    matrix[start] = 'a'
    matrix[end] = 'z'


def solution(second=False):
    visited = {}
    bfs = deque([(x, 0) for x in starts]) if second else deque([(start, 0)])

    while bfs:
        pos, val = bfs.popleft()
        if pos in visited:
            continue

        visited[pos] = val

        for adj in (0, 1), (1, 0), (-1, 0), (0, -1):
            adj_pos = (pos[0] + adj[0], pos[1] + adj[1])
            if adj_pos not in matrix:
                continue
            elif ord(matrix[adj_pos]) - 1 <= ord(matrix[pos]):
                bfs.append((adj_pos, val + 1))

    return visited[end]
