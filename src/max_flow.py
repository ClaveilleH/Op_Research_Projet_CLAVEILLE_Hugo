from graph_struct import Graph
from detect_negative_cycle import detect_negative_cycle

# implémentation de l'algorithme de Edmonds-Karp pour le problème du flot maximum & min cut.
# edmonds-karp est une amélioration de l'algorithme de Ford-Fulkerson qui utilise une recherche en largeur (BFS) 
# pour trouver les chemins augmentants, garantissant ainsi une complexité polynomiale de O(V * E^2) dans le pire des cas

def ford_fulkerson(graph):
    max_flow = 0
    path, flow = bfs(graph)
    while flow > 0:
        max_flow += flow
        for u, v in path:
            edge = graph.get_edge(u, v)
            edge.cap -= flow
            rev_edge = graph.get_edge(v, u)
            rev_edge.cap += flow

        path, flow = bfs(graph)
    return max_flow

def bfs(graph):
    queue = [graph.source]
    visited = {graph.source: None}
    flow = {graph.source: float('inf')}
    while queue:
        u = queue.pop(0)
        for edge in graph.adj[u]:
            if edge.cap > 0 and edge.dest not in visited:
                visited[edge.dest] = u
                flow[edge.dest] = min(flow[u], edge.cap)
                if edge.dest == graph.sink:
                    return reconstruct_path(visited, graph.sink), flow[graph.sink]
                queue.append(edge.dest)
    return [], 0

def reconstruct_path(visited, sink):
    path = []
    while visited[sink] is not None:
        path.append((visited[sink], sink))
        sink = visited[sink]
    path.reverse()
    return path

def min_cut(graph):
    # Après l'exécution de Ford-Fulkerson, on peut trouver le min cut en effectuant un BFS 
    # à partir de la source dans le graphe résiduel. 
    # Les sommets atteignables depuis la source forment un côté du cut, et les autres sommets forment l'autre côté.
    source_reachable = set()
    sink_reachable = set()
    queue = [graph.source]
    sommets = set(range(graph.n))
    while queue:
        u = queue.pop(0)
        source_reachable.add(u)
        for edge in graph.adj[u]:
            if edge.cap > 0 and edge.dest not in source_reachable:
                queue.append(edge.dest)
    sink_reachable = sommets - source_reachable
    return source_reachable, sink_reachable


def max_flow_min_cut(graph):
    max_flow = ford_fulkerson(graph)
    source_reachable, sink_reachable = min_cut(graph)
    assert source_reachable.isdisjoint(sink_reachable), "Les ensembles de sommets atteignables et non atteignables ne sont pas disjoints"
    assert source_reachable.union(sink_reachable) == set(range(graph.n)), "L'union des ensembles de sommets atteignables et non atteignables ne couvre pas tous les sommets"
    return max_flow, source_reachable, sink_reachable

if __name__ == "__main__":
    from graph_struct import load_graph_from_file
    # graph, s, t = load_graph_from_file('data/graph_classic.txt')
    # graph, s, t = load_graph_from_file('data/graph_cycle_negatif.txt')
    # graph, s, t = load_graph_from_file('data/graph_data.txt')
    graph, s, t = load_graph_from_file('data/test2.txt')

    try:
        max_flow, cut_edges, others = max_flow_min_cut(graph)
        print("Flot maximum pour le graph test :", max_flow)
        print("Cut edges (from reachable to non-reachable):", cut_edges)
        print("Cut edges (from non-reachable to reachable):", others)
        print("Flot maximum pour le graph test :", max_flow)
        from graph_to_dot import graph_to_dot
        # graph_to_dot(graph, "output/graphe_res.dot", show_capacity=True, show_zero=True)
        graph_to_dot(graph, "output/graphe_res.dot", show_return=True, show_zero=True)
    except ValueError as e: 
        print(e)


