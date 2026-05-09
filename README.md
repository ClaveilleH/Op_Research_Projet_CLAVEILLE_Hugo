# Op_Research_Projet_CLAVEILLE_Hugo

Projet de recherche operationnelle sur les problemes de flot dans les graphes.

Le depot contient une implementation maison, sans bibliotheque de flot externe, des algorithmes suivants :

- flot maximum et coupe minimale avec Ford-Fulkerson / Edmonds-Karp ;
- flot de cout minimum par chemins augmentants successifs ;
- recherche de plus court chemin dans le graphe residuel avec Bellman-Ford ;
- variante comparee dans `Dijkstra_min_cost_flow.py` ;
- detection de cycles de cout negatif ;
- export des graphes residuels au format DOT pour visualisation avec Graphviz.

## Structure du projet

```text
.
├── data/                      # Graphes de test
├── output/                    # Fichiers DOT generes
├── output/img/                # Images generees depuis les DOT
├── rapport/                   # Rapport LaTeX
├── src/
│   ├── graph_struct.py        # Structure de graphe residuel
│   ├── max_flow.py            # Flot max et min cut
│   ├── min_cost_flow.py       # Flot de cout minimum
│   ├── Dijkstra_min_cost_flow.py
│   ├── detect_negative_cycle.py
│   ├── graph_to_dot.py        # Export DOT
│   └── test.py                # Exemple d'execution
├── affiche.sh                 # Conversion DOT -> JPG et ouverture de l'image
└── consignes.txt              # Enonce et objectifs du projet
```

## Prerequis

- Python 3.10 ou plus recent ;
- Graphviz, uniquement pour generer les images des graphes.

Installation de Graphviz sous Linux :

```bash
sudo apt install graphviz
```

Le code Python n'utilise pas de dependance externe.

## Format des fichiers de graphe

Les graphes sont stockes dans `data/`.

La premiere ligne de chaque fichier contient :

```text
n m s t
```

avec :

- `n` : nombre de sommets ;
- `m` : nombre d'arcs ;
- `s` : sommet source ;
- `t` : sommet puits.

Chaque ligne suivante decrit un arc :

```text
u v capacite cout
```

Exemple :

```text
6 9 0 5
0 1 16 2
0 2 13 4
1 3 12 2
3 5 20 1
```

Lors du chargement avec `load_graph_from_file`, chaque arc direct est ajoute avec un arc retour de capacite initiale nulle et de cout oppose, ce qui permet de travailler directement sur le graphe residuel.

## Execution

Depuis la racine du projet :

```bash
python3 src/max_flow.py
```

Calcule un flot maximum et une coupe minimale sur le graphe choisi dans le bloc `if __name__ == "__main__"` de `src/max_flow.py`.

```bash
python3 src/min_cost_flow.py
```

Calcule un flot de cout minimum par chemins augmentants successifs.

```bash
python3 src/detect_negative_cycle.py
```

Teste la detection de cycles de cout negatif et genere un graphe normalise dans `output/normalized_graph.dot`.

```bash
python3 src/test.py
```

Compare les resultats de `min_cost_flow.py` et `Dijkstra_min_cost_flow.py`.
Sur l'exemple courant, les deux variantes renvoient :

```text
(23, 174)
```

correspondant au couple `(flot maximum, cout total)`.

## Visualisation des graphes

Les scripts peuvent generer des fichiers DOT dans `output/`.
Pour convertir un fichier DOT en image JPG :

```bash
./affiche.sh graphe_res
```

La commande lit :

```text
output/graphe_res.dot
```

et genere :

```text
output/img/graphe_res.jpg
```

Il est aussi possible d'utiliser Graphviz directement :

```bash
dot -Tjpg output/graphe_res.dot -o output/img/graphe_res.jpg
```

## Rapport

Le rapport LaTeX est dans `rapport/`.

Compilation :

```bash
cd rapport
make
```

Le PDF genere est `rapport/rapport.pdf`.

## Notes

- Les arcs retour du graphe residuel sont marques par l'attribut `retour=True`.
- Dans les exports DOT, les arcs retour peuvent etre affiches en bleu avec l'option `show_return=True`.
- Les scripts sont configures avec des fichiers de test directement dans leurs blocs `__main__`. Pour tester un autre graphe, modifier la ligne `load_graph_from_file(...)` correspondante.
- Certains tests de flot de cout minimum affichent des messages de detection de cycle negatif dans le graphe residuel. Le resultat final de comparaison reste verifie dans `src/test.py` par des assertions.
