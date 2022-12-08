from math import prod

grid = {}


def parse_input(file_name):
    with open(file_name) as file:
        for i, line in enumerate(file):
            for j, el in enumerate(line.strip()):
                grid[i, j] = el


def solution():
    visible = set()
    scenic_scores = []
    for pos in grid:
        scores = []
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            i, j = pos
            score = 0
            while (i, j) in grid:
                ii = i + di
                jj = j + dj

                if (ii, jj) not in grid:
                    visible.add(pos)
                    break
                elif grid[ii, jj] >= grid[pos]:
                    score += 1
                    break

                i = ii
                j = jj
                score += 1

            scores.append(score)

        scenic_scores.append(scores)

    return len(visible), max(prod(x) for x in scenic_scores)
