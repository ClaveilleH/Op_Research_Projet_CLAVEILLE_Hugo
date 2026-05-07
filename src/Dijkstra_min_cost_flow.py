from graph_struct import Graph
from detect_negative_cycle import detect_negative_cycle

# implémentation de l'algorithme de Edmonds-Karp pour le problème du flot maximum.
# edmonds-karp est une amélioration de l'algorithme de Ford-Fulkerson qui utilise une recherche en largeur (BFS) 
# pour trouver les chemins augmentants, garantissant ainsi une complexité polynomiale de O(V * E^2) dans le pire des cas

def ford_fulkerson(graph):
    # if detect_negative_cycle(graph):
    #     raise ValueError("Le graphe contient un cycle négatif, ce qui rend le problème du flot maximum indéfini.")
    
    max_flow = 0
    total_cost = 0
    path, flow, cost = shortest_path(graph)
    while flow > 0:
        max_flow += flow
        total_cost += flow * cost
        for u, v in path:
            edge = graph.get_edge(u, v)
            edge.cap -= flow
            rev_edge = graph.get_edge(v, u)
            rev_edge.cap += flow

        path, flow, cost = shortest_path(graph)
    
    if detect_negative_cycle(graph):
        print("Cycle négatif détecté dans le graphe résiduel après l'algorithme de Ford-Fulkerson")

    return max_flow, total_cost

def shortest_path(graph):
    """
    On utilise l'algorithme de Bellman-Ford pour trouver le chemin de coût minimum dans le graphe résiduel.
    """

    # Initialisation des distances
    dist = {i: float('inf') for i in range(graph.n)}
    dist[graph.source] = 0
    visited = {i: None for i in range(graph.n)}

    # Relaxation des arêtes V-1 fois
    for _ in range(graph.n - 1):
        for sommet in range(graph.n):
            for edge in graph.adj[sommet]:
                if edge.cap > 0:
                    new_dist = dist[edge.origin] + edge.cost
                    if dist[edge.origin] != float('inf') and dist[edge.dest] > new_dist:
                        dist[edge.dest] = new_dist
                        visited[edge.dest] = edge.origin
    
    #Vérification de la présence d'un cycle négatif
    for sommet in range(graph.n):
        for edge in graph.adj[sommet]:
            if dist[edge.origin] != float('inf') and dist[edge.dest] > dist[edge.origin] + edge.cost:
                print("Cycle négatif détecté dans le graphe résiduel")

    if dist[graph.sink] == float('inf'):
        return [], 0, 0  # pas de chemin augmentant

    path = reconstruct_path(visited, graph.sink)

    flow = float('inf')
    for u, v in path:
        edge = graph.get_edge(u, v)
        flow = min(flow, edge.cap)

    return path, flow, dist[graph.sink]    


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
    graph, s, t = load_graph_from_file('data/test3.txt')

    try:
        max_flow, total_cost = ford_fulkerson(graph)
        print("Flot maximum pour le graph test :", max_flow)
        print("Coût total pour le graph test :", total_cost)
        from graph_to_dot import graph_to_dot
        # graph_to_dot(graph, "output/graphe_res.dot", show_capacity=True, show_zero=True)
        graph_to_dot(graph, "output/graphe_res.dot", show_return=True, show_zero=True)
        graph_to_dot(graph, "output/graphe_res.dot", show_return=False, show_zero=True)
    except ValueError as e: 
        print(e)

