from pprint import pprint


def print_frame(frame):
    for row in frame:
        print(" ".join(row))


def main():
    frame = []
    for _ in range(10):
        row_list = []
        for _ in range(10) :
            row_list.append("0")
        frame.append(row_list)

    print_frame(frame)


if __name__ =="__main__":
    main()