from graph_struct import Graph
from detect_negative_cycle import detect_negative_cycle


# Implémentation de l'algorithme de Ford-Fulkerson pour le problème du flot maximum.
def ford_fulkerson(graph):
    if detect_negative_cycle(graph):
        raise ValueError("Le graphe contient un cycle négatif, l'algorithme de Ford-Fulkerson ne peut pas être appliqué.")
    
    max_flow = 0
    while True:
        # Recherche d'un chemin augmentant avec une capacité résiduelle positive
        path, flow = bfs(graph)
        if flow == 0:
            break  # Aucun chemin augmentant trouvé, on a atteint le flot maximum
        max_flow += flow
        # Mise à jour des capacités résiduelles le long du chemin trouvé
        for u, v in path:
            for edge in graph.adj[u]:
                if edge.dest == v:
                    edge.cap -= flow
                    break
            for edge in graph.adj[v]:
                if edge.dest == u:
                    edge.cap += flow
                    break

    return max_flow

def bfs(graph):
    from collections import deque
    queue = deque([graph.source])
    parent = {graph.source: None}
    flow = {graph.source: float('inf')}

    while queue:
        u = queue.popleft()
        for edge in graph.adj[u]:
            if edge.cap > 0 and edge.dest not in parent:
                parent[edge.dest] = u
                flow[edge.dest] = min(flow[u], edge.cap)
                if edge.dest == graph.sink:
                    return reconstruct_path(parent, graph.sink), flow[graph.sink]
                queue.append(edge.dest)

    return [], 0

def reconstruct_path(parent, sink):
    path = []
    while parent[sink] is not None:
        path.append((parent[sink], sink))
        sink = parent[sink]
    path.reverse()
    return path

if __name__ == "__main__":
    from graph_struct import load_graph_from_file
    graph, s, t = load_graph_from_file('data/graph_classic.txt')
    max_flow = ford_fulkerson(graph)
    print("Flot maximum pour le graph classic :", max_flow)

    graph, s, t = load_graph_from_file('data/graph_cycle_negatif.txt')
    try:
        max_flow = ford_fulkerson(graph)
        print("Flot maximum pour le graph cycle_negatif :", max_flow)
    except ValueError as e:
        print(e)

    graph, s, t = load_graph_from_file('data/graph_data.txt')
    try:
        max_flow = ford_fulkerson(graph)
        print("Flot maximum pour le graph data :", max_flow)
        from graph_to_dot import graph_to_dot
        graph_to_dot(graph, "output/graphe_res.dot", show_capacity=True, show_zero=True)
    except ValueError as e:
        print(e)