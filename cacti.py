def cacti_number(func):
    def wrapper(plot):
        
        rows = len(plot)
        cols = len(plot[0])
        count = 0

       plots
        for i in range(rows):nano
            for j in range(cols):
                if plot[i][j] == 0 and not is_adjacent_cactus(plot, i, j):
                    count += 1

        return count

    return wrapper

def is_adjacent_cactus(plot, row, col):
    rows = len(plot)
    cols = len(plot[0])

    # Check horizontally and vertically for adjacent cacti
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        r = row + dr
        c = col + dc
        if 0 <= r < rows and 0 <= c < cols and plot[r][c] == 1:
            return True

    return False

