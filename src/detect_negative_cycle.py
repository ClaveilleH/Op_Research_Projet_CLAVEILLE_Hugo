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



def normalize_graph(graph):
    """
    Ajoute une constante à toutes les arêtes pour éliminer les poids négatifs.
    Attention : cela ne supprime pas un cycle négatif structurel, 
    mais rend les poids positifs.
    """
    min_weight = float('inf')

    # Trouver le plus petit poids d'arête
    for u in range(graph.n):
        for edge in graph.adj[u]:
            min_weight = min(min_weight, edge.cost)

    # Si déjà aucun poids négatif
    if min_weight >= 0:
        return graph

    # Constante pour rendre tous les poids positifs
    shift = -min_weight + 1

    for u in range(graph.n):
        for edge in graph.adj[u]:
            edge.cost += shift

    return graph


def detect_and_normalize(graph):
    """
    Détecte un cycle négatif et normalise le graphe si nécessaire.
    """
    has_neg_cycle = detect_negative_cycle(graph)

    if has_neg_cycle:
        print("⚠️ Cycle négatif détecté -> normalisation des poids")
        graph = normalize_graph(graph)
    else:
        print("✅ Aucun cycle négatif détecté")

    return has_neg_cycle, graph

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

    # Test de la normalisation 
    graph, s, t = load_graph_from_file('data/graph_cycle_negatif.txt')
    has_neg_cycle, normalized_graph = detect_and_normalize(graph)
    print("Après normalisation, cycle négatif détecté :", detect_negative_cycle(normalized_graph))
    from graph_to_dot import graph_to_dot
    graph_to_dot(normalized_graph, 'output/normalized_graph.dot')
