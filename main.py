from data_point import DataPoint
import sys

from graph import Graph

# read the header and ignore it
sys.stdin.readline()


def next_sample():
    return DataPoint.from_str(sys.stdin.readline())


graph = Graph(next_sample)
graph.start()
