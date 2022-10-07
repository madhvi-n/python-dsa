"""
Using Adjacency List
"""


class AdjacencyNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices

    def add_edge(self, source, destination):
        node = AdjacencyNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        # Adding the source node to the destination as it's an undirected graph
        node = AdjacencyNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self):
        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            node = self.graph[i]
            while node:
                print(" -> {}".format(node.vertex), end="")
                node = node.next
            print(" -> None \n")


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


if __name__ == "__main__":
    main()
