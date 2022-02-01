import os
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Settings')
    parser.add_argument('From', metavar='<from>', type=int, help='Starting point')
    parser.add_argument('To', metavar='<to>', type=int, help='Ending point')
    parser.add_argument('Step', metavar='<step>', type=int, help='Step')

    args = parser.parse_args()

    numFrom = args.From
    numTo = args.To
    numStep = args.Step

    if numFrom > numTo:
        print("Starting point must be less than ending!")
        sys.exit()

    filename = f'nums_{numFrom}_{numTo}_{numStep}.txt'

    if not os.path.exists('./lists'):
        os.makedirs('./lists')

    with open(f'lists/{filename}', 'w') as outfile:
        for i in range(numFrom, numTo + 1, numStep):
            outfile.write(str(i) + '\n')
        

    print(f'List successfully created under lists/{filename}')


if __name__ == "__main__":
    main()