from graph_struct import Graph
from detect_negative_cycle import detect_negative_cycle

# implémentation de l'algorithme de Edmonds-Karp pour le problème du flot maximum.


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

if __name__ == "__main__":
    from graph_struct import load_graph_from_file
    # graph, s, t = load_graph_from_file('data/graph_classic.txt')
    # graph, s, t = load_graph_from_file('data/graph_cycle_negatif.txt')
    # graph, s, t = load_graph_from_file('data/graph_data.txt')
    graph, s, t = load_graph_from_file('data/test2.txt')

    try:
        max_flow = ford_fulkerson(graph)
        print("Flot maximum pour le graph test :", max_flow)
        from graph_to_dot import graph_to_dot
        graph_to_dot(graph, "output/graphe_res.dot", show_capacity=True, show_zero=True)
    except ValueError as e: 
        print(e)

