
def row_decoder(row: str):
    # convert F = 0, B = 1 to binary string
    bin_row = row.replace('F', '0').replace('B', '1')
    return int(bin_row, 2)


def col_decoder(col: str):
    # convert L = 0, R = 1 to binary string
    bin_col = col.replace('L', '0').replace('R', '1')
    return int(bin_col, 2)


def seat_id(row: int, col: int):
    return row * 8 + col


def decode(seat: str):
    row = row_decoder(seat[:7])
    col = col_decoder(seat[-3:])
    id = seat_id(row, col)

    return (row, col, id)


def load_file(file: str):
    # just load all the lines
    with open(file, 'r') as reader:
        lines = [line.strip() for line in reader]

    return lines


def day_five_part_one():
    lines = load_file('5.in')
    # get the highest ID
    passes = sorted(map(lambda x: decode(x), lines),
                    key=lambda x: x[2], reverse=True)
    print('largest id:', passes[0])


def day_five_part_two():
    lines = load_file('5.in')
    # get the highest ID
    passes = sorted(map(lambda x: decode(x), lines), key=lambda x: x[2])
    idx = 0

    while idx + 1 < len(passes):
        if (passes[idx][2] + 1 != passes[idx + 1][2]):
            print('missing seat:', passes[idx][2] + 1)
            break
        idx += 1


day_five_part_one()
day_five_part_two()
