import heapq
from prettytable import PrettyTable

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    def dijkstra(self, start):
        dist = [float("inf")] * self.V
        dist[start] = 0
        visited = [False] * self.V

        heap = [(0, start)]

        while heap:
            d, u = heapq.heappop(heap)

            if visited[u]:
                continue
            visited[u] = True

            for v, w in self.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

        return dist


if __name__ == "__main__":
    # test case
    graph = Graph(6)
    graph.add_edge(0, 1, 7)
    graph.add_edge(0, 2, 9)
    graph.add_edge(0, 5, 14)
    graph.add_edge(1, 2, 10)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 11)
    graph.add_edge(2, 5, 2)
    graph.add_edge(3, 4, 6)
    graph.add_edge(4, 5, 9)

    start = 0
    distances = graph.dijkstra(start)

    table = PrettyTable()
    table.field_names = ["Vertex", "Distance from Start"]

    for i, d in enumerate(distances):
        table.add_row([i, d if d != float("inf") else "∞"])

    print(table)
