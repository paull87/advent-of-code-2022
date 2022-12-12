
FILE_NAME = 'input.txt'


WIDTH = 1000
HEIGHT = 1000
SLACK_ALLOWED = 9


class Board:

    def __init__(self, width, height, tail_length):
        self._width = width
        self._height = height
        self.h_pos = [int(width / 2), int(height / 2)]
        self.tails = [self.h_pos[:] for _ in range(tail_length)]
        self.t_pos_hist = [tuple(self.h_pos[:])]
        self.h_pos_hist = [tuple(self.h_pos[:])]

    def create_board(self):
        board = [['.' for _ in range(self._width)] for _ in range(self._height)]
        return board

    def show_board(self):
        print(self.tails)
        show_board = self.create_board()
        for pos in self.h_pos_hist:
            show_board[pos[1]][pos[0]] = 'h'
        for pos in self.t_pos_hist:
            show_board[pos[1]][pos[0]] = 't'

        for i, t in enumerate(self.tails):
            show_board[self.tails[i][1]][self.tails[i][0]] = str(i)
        show_board[self.h_pos[1]][self.h_pos[0]] = 'H'
        for row in show_board:
            print(''.join(row))

    def check_tail(self):
        for i, tail in enumerate(self.tails):

            leading = self.h_pos if i == 0 else self.tails[i-1]
            following = self.tails[i]

            diff = (
                leading[0] - following[0],
                leading[1] - following[1],
            )

            if abs(diff[0]) > 1 and not diff[1]:  # horizontal
                xv = 1 if diff[0] > 0 else -1
                self.tails[i][0] += xv
            elif abs(diff[1]) > 1 and not diff[0]:  # vertical
                yv = 1 if diff[1] > 0 else -1
                self.tails[i][1] += yv
            elif (abs(diff[1]) > 1 and abs(diff[0]) > 0) or (abs(diff[0]) > 1 and abs(diff[1]) > 0):
                xv = 1 if diff[0] > 0 else -1
                self.tails[i][0] += xv
                yv = 1 if diff[1] > 0 else -1
                self.tails[i][1] += yv

        self.t_pos_hist.append(tuple(self.tails[-1]))

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

    board = Board(WIDTH, HEIGHT, SLACK_ALLOWED)

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
