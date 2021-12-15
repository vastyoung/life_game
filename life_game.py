import sys
from time import sleep


def init_frame(row, col):
    frame = []
    for _ in range(row):
        frame.append(["0" for _ in range(col)])
    return frame


def next_frame(cur_frame):
    new_frame = []
    for row in cur_frame:
        new_frame.append([str(int(i) + 1) for i in row])
    return new_frame


def print_frame(frame):
    row_num = len(frame)
    print("\033[{}A".format(row_num + 1))
    for row in frame:
        print(" ".join(row))


def main():
    if len(sys.argv) != 3:
        print("usage: {} <row> <col>, such as: {} 10 8".format(sys.argv[0], sys.argv[0]))
        sys.exit(1)

    row, col = [int(arg) for arg in sys.argv[1:]]
    frame = init_frame(row, col)
    while frame:
        print_frame(frame)
        frame = next_frame(frame)
        sleep(1)


if __name__ == '__main__':
    main()
