from typing import List, Optional

from tap import Tap

from dayselector import daySelector


class AocArgs(Tap):
    day: int
    file: Optional[str] = None

    def configure(self) -> None:
        self.add_argument('day', help='which day [1-24]')
        self.add_argument('-f',
                          '--file',
                          help='input file, defaults to data/day<day>.txt')

    def process_args(self) -> None:
        if self.file == None:
            self.file = f'data/day{self.day}.txt'


def main() -> None:
    args = AocArgs().parse_args()
    try:
        with open(args.file) as file:  # type: ignore
            daySelector(args.day, file.read())

    except KeyError as e:
        print(f'Day{e} solution not implemented yet')


if __name__ == "__main__":
    main()
