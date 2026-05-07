from graph_struct import Graph
from detect_negative_cycle import detect_negative_cycle
from graph_struct import load_graph_from_file
from min_cost_flow import ford_fulkerson as min_cost_flow
from Dijkstra_min_cost_flow import ford_fulkerson as min_cost_flow_dijkstra
from graph_to_dot import graph_to_dot
from copy import deepcopy


if __name__ == "__main__":
    graph, s, t = load_graph_from_file('data/graph_classic.txt')
    # graph, s, t = load_graph_from_file('data/graph_cycle_negatif.txt')
    # graph, s, t = load_graph_from_file('data/graph_data.txt')

    graph1 = deepcopy(graph)
    graph2 = deepcopy(graph)
    res1 = min_cost_flow(graph1)
    res2 = min_cost_flow_dijkstra(graph2)
    print("Résultat de l'algorithme de Ford-Fulkerson :", res1)
    print("Résultat de l'algorithme de Dijkstra :", res2)
    assert res1 == res2, "Les résultats des deux algorithmes ne sont pas les mêmes"
    assert graph1 == graph2, "Les graphes résiduels des deux algorithmes ne sont pas les mêmes"
    
    graph_to_dot(graph1, "output/graph_res_min_cost_flow.dot", show_capacity=True, show_zero=True)
    graph_to_dot(graph2, "output/graph_res_min_cost_flow_dijkstra.dot", show_capacity=True, show_zero=True)