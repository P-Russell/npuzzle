import argparse


def main():
    parser = argparse.ArgumentParser(usage='file OR ')

    parser.add_argument('file', type=str, help='Name of file that contains puzzle to be solved')
    parser.add_argument('-s', '--solvable', action='store_true', default=True,
                        help='Forces generation of solvable puzzle')
    args = parser.parse_args()



if __name__ == '__main__':
    main()