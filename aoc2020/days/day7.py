from typing import List, Optional, Tuple, Dict

from pprint import pprint
from collections import namedtuple
import re
import networkx as nx
import matplotlib.pyplot as plt

BagDesc = namedtuple('BagDesc', ['name', 'holds'])


def parseLine(line: str) -> BagDesc:
    pattern = '^(.*) contain no other bags.$'
    match = re.search(pattern, line)
    if match:
        name = match.group(1).replace('bags', '').strip()
        return BagDesc(name=name, holds=[])

    pattern = '^(.*) contain (.*).$'
    match = re.search(pattern, line)
    name = match.group(1).replace('bags', '').strip()  # type: ignore
    holdsPart = match.group(2).split(', ')  # type: ignore
    holdsPattern = '^(\d) (.*) bags?'
    return BagDesc(
        name=name,
        holds=[
            re.search(holdsPattern, part).group(2, 1)  # type: ignore
            for part in holdsPart
        ])


def subBagCount(graphEdges: Dict[Tuple[str, str], int],
                parentNode: str) -> int:
    count = 0
    for rootEdges in [(key, value) for key, value in graphEdges.items()
                      if key[0] == parentNode]:
        count += (1 + subBagCount(graphEdges, rootEdges[0][1])) * rootEdges[1]
    return count


class Solution:
    input: List[BagDesc]
    bagGraph: nx.DiGraph

    def __init__(self, input: List[str]):
        self.input = [parseLine(x) for x in input]
        # self.bagGraph.add_nodes_from([name for name, holds in self.input])
        self.bagGraph = nx.DiGraph()
        edges = [(name, hold, int(amount)) for name, holds in self.input
                 if len(holds) > 0 for hold, amount in holds]
        self.bagGraph.add_weighted_edges_from(edges)

        # pprint(self.input)
        # pprint(edges)
        pos = nx.spring_layout(self.bagGraph)
        nx.draw_networkx(self.bagGraph, pos, with_labels=True)
        labels = nx.get_edge_attributes(self.bagGraph, 'weight')
        nx.draw_networkx_edge_labels(self.bagGraph, pos, edge_labels=labels)
        # plt.show()

    def part1(self) -> int:
        return len(
            set([
                node[0] for node in nx.edge_dfs(
                    self.bagGraph, 'shiny gold', orientation='reverse')
            ]))

    def part2(self) -> int:
        labels = nx.get_edge_attributes(self.bagGraph, 'weight')
        res = subBagCount(labels, 'shiny gold')
        return res
        # pprint(subGraph)
