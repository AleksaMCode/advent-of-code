cycle = 0
X = 1
cycles = (20, 60, 100, 140, 180, 220)
CRT_WIDTH = 40


def tick(signal_strength, ticks=1):
    global cycle
    for _ in range(ticks):
        if cycle % CRT_WIDTH in range(X - 1, X + 2):
            print('██', end='')
        else:
            print('░░', end='')

        cycle += 1
        if cycle in cycles:
            signal_strength += cycle * X

        if cycle % CRT_WIDTH == 0:
            print()

    return signal_strength


def start_cpu(file_name):
    global X
    signal_strength = 0
    with open(file_name) as file:
        for line in file:
            match line.split():
                case ['addx', val]:
                    signal_strength = tick(signal_strength, 2)
                    X += int(val)
                case ['noop']:
                    signal_strength = tick(signal_strength)

    return signal_strength
