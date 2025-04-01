from collections import deque

def create_graph():
    graph = {}
    while True:
        node = input("Entrez le nom du nœud (ou 'q' pour quitter) : ")
        if node.lower() == 'q':
            break

        neighbors = input(f"Entrez les nœuds voisins de '{node}' séparés par des espaces : ").split()
        graph[node] = neighbors
    return graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node) 

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("Création du graphe :")

user_graph = create_graph()

print("Graphe saisi :", user_graph)

start_node = input("Entrez le nœud de départ pour la recherche en largeur : ")

if start_node in user_graph:
    print("Parcours en largeur à partir du nœud :", start_node)
    bfs(user_graph, start_node)
else:
    print("Le nœud de départ n'existe pas dans le graphe.")
