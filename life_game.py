from random import random
import sys
from time import sleep

import numpy as np

SAMPLE_1 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

glider_gun = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

SAMPLE_2 = np.zeros((50, 70))
SAMPLE_2[1:10, 1:37] = glider_gun


def random_gen(rate):
    return int(random() <= rate)


def init_frame(row, col, func):
    frame = []
    for _ in range(row):
        frame.append([int(func()) for _ in range(col)])
    return frame


def next_frame(cur_frame):
    row_num = len(cur_frame)
    col_num = len(cur_frame[0])
    new_frame = init_frame(row_num, col_num, func=lambda: 0)
    for i in range(row_num):
        for j in range(col_num):
            pos = [
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1)
            ]
            ij_value = cur_frame[i][j]
            value_list = [get_value_by_pos(cur_frame, p) for p in pos]
            alive_count = len([i for i in value_list if i == 1])
            if ij_value == 1 and alive_count < 2:
                ij_value = 0
            elif ij_value == 1 and alive_count in [2, 3]:
                ij_value = 1
            elif ij_value == 1 and alive_count > 3:
                ij_value = 0
            elif ij_value == 0 and alive_count == 3:
                ij_value = 1
            new_frame[i][j] = ij_value
    return new_frame


def get_value_by_pos(frame, pos):
    i = pos[0]
    j = pos[1]
    row_num = len(frame)
    col_num = len(frame[0])
    if 0 <= i < row_num and 0 <= j < col_num:
        return frame[i][j]
    return 0


def print_frame(frame):
    row_num = len(frame)
    print("\033[{}A".format(row_num + 1))
    for row in frame:
        print("".join(["███" if i == 1 else "   " for i in row]))


def main():
    if len(sys.argv) != 4:
        print("usage: {} <row> <col>, such as: {} 10 8".format(sys.argv[0], sys.argv[0]))
        sys.exit(1)

    row, col = [int(arg) for arg in sys.argv[1:-1]]
    rate = float(sys.argv[-1])

    frame = init_frame(row, col, func=lambda: random_gen(rate))
    # frame = SAMPLE_2
    while True:
        print_frame(frame)
        frame = next_frame(frame)
        sleep(0.1)


if __name__ == '__main__':
    main()
