import argparse
from sys import argv

from typing import List
from typing import Optional

from tap import Tap

class AocArgs(Tap):
    day : int
    file : Optional[str] = None

    def configure(self):
        self.add_argument('day')

    def process_args(self):
        if self.file == None:
            self.file = f'data/day{self.day}'

def main():
    print('main')
    args = AocArgs().parse_args()
    
if __name__ == "__main__":
    main()