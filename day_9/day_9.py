
FILE_NAME = 'sample_2.txt'


WIDTH = 26
HEIGHT = 21
SLACK_ALLOWED = 9


class Board:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.t_pos = [11, 15] #[int(width / 2), int(height / 2)]
        self.h_pos = [11, 15] #[int(width / 2), int(height / 2)]
        self.t_pos_hist = [tuple(self.t_pos[:])]
        self.h_pos_hist = [tuple(self.h_pos[:])]

    def create_board(self):
        board = [['.' for _ in range(self._width)] for _ in range(self._height)]
        return board

    def show_board(self):
        show_board = self.create_board()
        for pos in self.h_pos_hist:
            show_board[pos[1]][pos[0]] = 'h'
        for pos in self.t_pos_hist:
            show_board[pos[1]][pos[0]] = 't'

        show_board[self.t_pos[1]][self.t_pos[0]] = 'T'
        show_board[self.h_pos[1]][self.h_pos[0]] = 'H'
        for row in show_board:
            print(''.join(row))

    def check_tail(self):
        diff = (
            self.h_pos[0] - self.t_pos[0],
            self.h_pos[1] - self.t_pos[1],
        )
        if abs(diff[0]) > SLACK_ALLOWED or abs(diff[1]) > SLACK_ALLOWED:
            self.move_tail()

    def move_tail(self):
        self.t_pos = self.h_pos_hist[-1]
        self.t_pos_hist.append(self.t_pos[:])

    def move_head(self, x, y):
        for x_move in range(0, abs(x)):
            self.h_pos[1] += int(x / abs(x))
            self.check_tail()
            self.h_pos_hist.append(tuple(self.h_pos[:]))
        for y_move in range(0, abs(y)):
            self.h_pos[0] += int(y / abs(y))
            self.check_tail()
            self.h_pos_hist.append(tuple(self.h_pos[:]))


def parse_move(move_string):
    direction, spaces = move_string.split()
    if direction == 'U':
        return 0, -int(spaces)
    if direction == 'D':
        return 0, int(spaces)
    if direction == 'L':
        return -int(spaces), 0
    if direction == 'R':
        return int(spaces), 0


def create_board():
    board = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    return board


def main():

    board = Board(WIDTH, HEIGHT)

    # print('>>>>Start')
    # board.show_board()

    with open(FILE_NAME) as file:
        for rec in file.readlines():
            rec = rec.strip()
            # print(f'__{rec}__')
            y, x = parse_move(rec)
            board.move_head(x, y)
            # board.show_board()

    print('>>>>After')
    board.show_board()

    print(f"Number of Tail touches: {len(set(board.t_pos_hist))}")



if __name__ == '__main__':
    main()
