import re


def load_file(file: str):
    tiles = {}

    # just load all the lines
    with open(file, 'r') as reader:
        tile = 0
        buff = []
        for line in reader:
            clean = line.strip()
            if clean == '':
                tiles[tile] = buff
                buff = []
                continue

            m = re.match(r'Tile (\d+):', clean)
            if m:
                tile = int(m.group(1))
            else:
                buff.append(clean)
    return tiles


class Tile:
    def __init__(self, number, tile):
        self.neighbors = {}
        self.number = number
        top = tile[0]
        bottom = tile[-1]
        left = ''.join([t[0] for t in tile])
        right = ''.join([t[-1] for t in tile])
        self.edges = [top, bottom, left, right, top[::-1],
                      bottom[::-1], left[::-1], right[::-1]]


def day_twenty_part_one(file: str):
    tiles = load_file(file)
    formatted = {}
    edge_map = {}
    for tile in tiles:
        formatted[tile] = Tile(tile, tiles[tile])
        for edge in formatted[tile].edges:
            if edge not in edge_map:
                edge_map[edge] = set([tile])
            else:
                edge_map[edge].add(tile)

    for tile in formatted:
        # lets assume unique match
        for i, edge in enumerate(formatted[tile].edges):
            if len(edge_map[edge]) > 1:
                formatted[tile].neighbors[i] = list(
                    edge_map[edge].difference(set([edge])))[0]

    product = 1
    # the corner pieces would only have 2 possible neighbors
    # the rest would have 3 or more! <-- since image can be flipped, * 2
    for tile in formatted:
        if (len(formatted[tile].neighbors) == 4):
            product *= tile
            print(f'tile {tile}: {formatted[tile].neighbors}')

    # build the table using any one tile
    print(product)


day_twenty_part_one('20-example.in')
day_twenty_part_one('20.in')
# day_twenty_part_one('19.in')
