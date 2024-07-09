from collections import Counter
from functools import lru_cache
import argparse


@lru_cache()
def unique_characters(string):
    if type(string) != str:
        raise ValueError
    counter = Counter(string)
    unique = [amount for amount, value in counter.items() if value == 1]
    number_of_unique = len(unique)
    return number_of_unique


def count_from_file(file_path):
    with open(file_path) as file:
        line = file.readline().rstrip()
        result = unique_characters(line)
        return result


def main_CLI():
    parser = argparse.ArgumentParser(description='Counts the number of unique characters in a string')
    parser.add_argument('-s', '--string', type=str)
    parser.add_argument('-f', '--file', type=str)
    args = parser.parse_args()
    if args.file:
        print(count_from_file(args.file))
    else:
        print(unique_characters(args.string))


if __name__ == '__main__':
    main_CLI()
