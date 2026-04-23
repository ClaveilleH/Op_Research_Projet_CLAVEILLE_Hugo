from dataclasses import dataclass

@dataclass
class Edge:
    """
    Represente une arête dans un graphe, avec une capacité et un coût associés.
    """
    retour : bool = False
    origin: int
    dest: int
    cap: int
    cost: int

class Graph:
    def __init__(self, n, source=0, sink=None):
        self.source = source
        self.sink = sink if sink is not None else n - 1 # par defaut, on considère que le puits est le dernier sommet
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, _origin, _dest, cap, cost=0):
        fwd = Edge(origin=_origin, dest=_dest, cap=cap, cost=cost)
        rev = Edge(origin=_dest, dest=_origin, cap=0, cost=-cost, retour=True)
        self.adj[_origin].append(fwd)
        self.adj[_dest].append(rev)
    
    def add_arc(self, _origin, _dest, cap, cost=0):
        fwd = Edge(origin=_origin, dest=_dest, cap=cap, cost=cost)
        self.adj[_origin].append(fwd)

    def get_edge(self, u, v):
        for edge in self.adj[u]:
            if edge.dest == v:
                return edge
        return None


def load_graph_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    # on filtre les lignes vides et les commentaires
    lines = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
    # on lit les paramètres du graphe
    n, m, s, t = map(int, lines[0].split())
    graph = Graph(n, source=s, sink=t)
    for line in lines[1:]:
        u, v, cap, cost = map(int, line.split())
        # graph.add_arc(u, v, cap, cost)
        graph.add_edge(u, v, cap, cost)
    return graph, s, t


if __name__ == "__main__":
    graph, s, t = load_graph_from_file('data/graph_classic.txt')
    graph, s, t = load_graph_from_file('data/graph_cycle_negatif.txt')
    graph, s, t = load_graph_from_file('data/graph_data.txt')
    print(graph.adj)