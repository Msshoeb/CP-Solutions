class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    def bellman_ford(self, source):
        dist = [float("inf")] * self.V
        dist[source] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains a negative weight cycle")
                return

        for i in range(self.V):
            print(f"Shortest distance from source to vertex {i}: {dist[i]}")


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, -3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    source_vertex = 0
    g.bellman_ford(source_vertex)
