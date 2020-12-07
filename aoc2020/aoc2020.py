from typing import List, Optional

from tap import Tap

from dayselector import daySelector


class AocArgs(Tap):
    day: Optional[int] = None
    file: Optional[str] = None

    def configure(self) -> None:
        self.add_argument('-d', '--day', help='which day [1-24]')
        self.add_argument('-f',
                          '--file',
                          help='input file, defaults to data/day<day>.txt')

    def process_args(self) -> None:
        if self.day != None and self.file == None:
            self.file = f'data/day{self.day}.txt'


def run(day: int, fileName: str) -> int:
    with open(fileName) as file:
        daySelector(day, file.read())
    return 1


def main() -> None:
    args = AocArgs().parse_args()
    try:
        if args.day == None:
            [run(x, f'data/day{x}.txt') for x in range(1, 32)]
        try:
            run(args.day, args.file)  # type: ignore
        except FileNotFoundError as e:
            print(e)

    except KeyError as e:
        print(f'{e} solution not implemented yet')
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    main()
