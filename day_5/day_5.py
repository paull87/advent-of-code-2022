
FILE_NAME = 'input.txt'


def parse_positions(strings_input):
    cleansed = [x for x in strings_input.split('\n') if x != ''][::-1]
    pos = 1
    starting_blocks = []
    while pos <= len(cleansed[0]):
        current_block = []
        for line in cleansed:
            if len(line) < pos:
                break
            block = line[pos]
            if block == ' ':
                break
            current_block.append(line[pos])
        starting_blocks.append(current_block)
        pos += 4

    return starting_blocks


def parse_move(move_string):
    move_split = move_string.split()
    moves = int(move_split[1])
    from_block = int(move_split[3]) - 1
    to_block = int(move_split[5]) - 1
    return moves, from_block, to_block


def move_block(blocks, from_block, to_block):
    block = blocks[from_block].pop()
    blocks[to_block].append(block)


def process_move(blocks, moves, from_block, to_block):
    for _ in range(moves):
        move_block(blocks, from_block, to_block)


def main(starting_pos):

    blocks = parse_positions(starting_pos)

    print('>>>>Start')
    for b in blocks:
        print(b)

    with open(FILE_NAME) as file:
        for rec in file.readlines():
            rec = rec.strip()
            moves, from_block, to_block = parse_move(rec)
            process_move(blocks, moves, from_block, to_block)

    print('>>>>After')
    for b in blocks:
        print(b)

    print(f'>>>>Outcome: {"".join([x[-1] for x in blocks])}')


if __name__ == '__main__':
    start = """
            [C]         [N] [R]
[J] [T]     [H]         [P] [L]
[F] [S] [T] [B]         [M] [D]
[C] [L] [J] [Z] [S]     [L] [B]
[N] [Q] [G] [J] [J]     [F] [F] [R]
[D] [V] [B] [L] [B] [Q] [D] [M] [T]
[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
[W] [P] [P] [D] [G] [P] [B] [P] [V]"""

    main(start)

