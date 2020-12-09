from typing import List, Optional, Tuple

from pprint import pprint
from collections import namedtuple
import re
import networkx as nx
import matplotlib.pyplot as plt

BagDesc = namedtuple('BagDesc', ['name', 'holds'])


def parseLine(line: str) -> BagDesc:
    pattern = '^(.*) contain no other bags.$'
    firstMatch = re.search(pattern, line)
    if firstMatch:
        name = firstMatch.group(1).replace('bags', '').strip()
        return BagDesc(name=name, holds=[])

    pattern = '^(.*) contain (.*).$'
    secondMatch = re.search(pattern, line)
    name = secondMatch.group(1).replace('bags', '').strip()
    holdsPart = secondMatch.group(2).split(', ')
    holdsPattern = '^(\d) (.*) bags?'
    return BagDesc(name=name,
                   holds=[
                       re.search(holdsPattern, part).group(2, 1)
                       for part in holdsPart
                   ])


class Solution:
    input: List[BagDesc]
    bagGraph = nx.DiGraph()

    def __init__(self, input: List[str]):
        self.input = [parseLine(x) for x in input]
        # pprint(self.input)
        self.bagGraph.add_nodes_from([name for name, holds in self.input])

        edges = [(name, hold) for name, holds in self.input if len(holds) > 0
                 for hold, amount in holds]
        # pprint(edges)
        self.bagGraph.add_edges_from(edges)
        # nx.draw(G, with_labels=True)
        # plt.show()

        # pprint(list(nx.edge_dfs(G,'shiny gold',orientation='reverse')))

    def part1(self) -> int:
        return len(
            set([
                node[0] for node in nx.edge_dfs(
                    self.bagGraph, 'shiny gold', orientation='reverse')
            ]))
