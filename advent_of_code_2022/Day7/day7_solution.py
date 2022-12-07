from collections import defaultdict


def traversal(file_name):
    dirs = defaultdict(int)
    path = []
    with open(file_name) as file:
        for line in file:
            match line.strip().split():
                case ['$', 'cd', new_dir]:
                    if new_dir == '..':
                        path.pop()
                    else:
                        path.append(new_dir)
                case [size, _] if size.isdigit():
                    for i in range(1, len(path) + 1):
                        dirs['/'.join(path[:i])] += int(size)

        return sum(x for x in dirs.values() if x <= 100_000), \
               min(x for x in dirs.values() if x >= dirs['/'] - (70_000_000 - 30_000_000))
