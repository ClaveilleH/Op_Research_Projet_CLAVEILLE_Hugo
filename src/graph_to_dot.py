from pathlib import Path

def graph_to_dot(graph, filename, show_capacity=True, show_zero=False, show_return=False):
    source = graph.source
    sink = graph.sink
    lines = ["digraph G {", "  rankdir=LR;",
             '  node [shape=circle, width=0.65, height=0.65, fixedsize=true];',
             f'  {source} [penwidth=3, color="black", label="s ({source})"];',
             f'  {sink} [shape=doublecircle, label="tt ({sink})"];' 
    ]
    for u in range(graph.n):
        for e in graph.adj[u]:
            if e.cap == 0 and not show_zero:
                continue
            if e.retour and not show_return:
                continue
            label = []
            if show_capacity:
                label.append(f"{e.cap}")
            lbl = "\n".join(label)
            lbl = f"<{e.cap}|<font color='red'>{e.cost}</font>>"
            color = "blue" if e.retour else "black"
            lines.append(f'  {u} -> {e.dest} [label={lbl}, shape=box, color="{color}"];')
            # lines.append(f'  {u} -> {e.dest} [label="{lbl}"];')
    lines.append("}")
    Path(filename).write_text("\n".join(lines), encoding="utf-8")

# Exemple d'utilisation :
# graph_to_dot(g, "output/graphe.dot")
if __name__ == "__main__":
    from graph_struct import load_graph_from_file
    graph, s, t = load_graph_from_file('data/graph_classic.txt')
    graph, s, t = load_graph_from_file('data/graph_cycle_negatif.txt')
    graph, s, t = load_graph_from_file('data/graph_data.txt')
    graph_to_dot(graph, "output/graphe.dot")

    graph, s, t = load_graph_from_file('data/test.txt')
    graph_to_dot(graph, "output/graphe_test.dot")

    graph, s, t = load_graph_from_file('data/test2.txt')
    graph_to_dot(graph, "output/graphe_test2.dot")

    graph, s, t = load_graph_from_file('data/test3.txt')
    graph_to_dot(graph, "output/graphe_test3.dot")

# dot -Tjpg output/graphe.dot -o output/img/graphe.jpg && xdg-open output/img/graphe.jpg