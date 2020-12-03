import argparse
from sys import argv
from tap import Tap

from days import daySelector

from typing import List, Optional

class AocArgs(Tap):
    day: int
    file: Optional[str] = None

    def configure(self):
        self.add_argument('day')

    def process_args(self):
        if self.file == None:
            self.file = f'data/day{self.day}'


def main():
    args = AocArgs().parse_args()
    try:
        with open(args.file) as file:
            daySelector(args.day,file.read())

    except KeyError as e:
        print(f'Day{e} solution not implemented yet')


if __name__ == "__main__":
    main()
