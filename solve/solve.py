def solve(n, repeats):

    count = 0
    step = 0

    for i in range(n):

        if i == 0:
            count += repeats
            step += 1
        elif i > 0:
            step = step * 10 + 1
            count = count + (repeats * step)

    return count

