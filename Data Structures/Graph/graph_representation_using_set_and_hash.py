from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(set)

    def add_edge(self, source, destination):
        # add edge from source to destination and then vice verse
        self.graph[source].add(destination)
        self.graph[destination].add(source)

    def search_edge(self, source, destination):
        # an edge exists if destination exists in graph[source] and source exists in graph[destination]
        if source not in self.graph:
            print(f"Source {source} is not present in graph")
            return

        if destination not in self.graph:
            print(f"Destination {destination} is not present in graph")
            return

        return destination in self.graph[source] and source in self.graph[destination]

    def print_graph(self):
        for i, adjlist in sorted(self.graph.items()):
            print(f"Vertex {i} : {sorted(adjlist)}")


def main():
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print_graph()
    print(graph.search_edge(2, 1))
    print(graph.search_edge(0, 3))


if __name__ == "__main__":
    main()
