def unique_sequence(line, limit: int):
    st = start = current_max_len = 0
    position = {}
    position[line[0]] = 0

    for i in range(len(line)):
        if line[i] not in position:
            position[line[i]] = i
        else:
            if position[line[i]] >= st:
                current_len = i - st
                if current_max_len < current_len <= limit:
                    current_max_len = current_len
                    start = st

                if current_max_len == limit:
                    return line[start: start + current_max_len], start + current_max_len

                st = position[line[i]] + 1

            position[line[i]] = i

        if current_max_len < i - st <= limit:
            current_max_len = i - st
            start = st

    return line[start: start + current_max_len], start + current_max_len
