from graph_struct import Graph


def detect_negative_cycle(graph):
    """
    Detecte la presence d'un cycle negatif dans le graphe en utilisant l'algorithme de Bellman-Ford.
    Retourne True si un cycle negatif est detecte, sinon False.
    """

    # Initialisation des distances
    dist = {i: float('inf') for i in range(graph.n)}
    dist[graph.source] = 0

    # Relaxation des arêtes V-1 fois
    for _ in range(graph.n - 1):
        for sommet in range(graph.n):
            for edge in graph.adj[sommet]:
                if dist[edge.origin] != float('inf') and dist[edge.dest] > dist[edge.origin] + edge.cost:
                    dist[edge.dest] = dist[edge.origin] + edge.cost

    # Vérification de la présence d'un cycle négatif
    for sommet in range(graph.n):
        for edge in graph.adj[sommet]:
            if dist[edge.origin] != float('inf') and dist[edge.dest] > dist[edge.origin] + edge.cost:
                return True

    return False

if __name__ == "__main__":
    from graph_struct import load_graph_from_file
    graph, s, t = load_graph_from_file('data/graph_classic.txt')
    cycle_negatif = detect_negative_cycle(graph)
    print("Resultat de Bellman-Ford pour le graph classic :", cycle_negatif)

    graph, s, t = load_graph_from_file('data/graph_cycle_negatif.txt')
    cycle_negatif = detect_negative_cycle(graph)
    print("Resultat de Bellman-Ford pour le graph cycle_negatif :", cycle_negatif)

    graph, s, t = load_graph_from_file('data/graph_data.txt')
    cycle_negatif = detect_negative_cycle(graph)
    print("Resultat de Bellman-Ford pour le graph data :", cycle_negatif)