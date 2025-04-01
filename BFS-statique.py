from collections import deque

# Algorithme de recherche en largeur (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)  # Pour afficher le nœud en cours de visite

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Exemple de graphe représenté sous forme de liste d'adjacence
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Appel de la fonction BFS avec le nœud de départ 'A'
print("Parcours en largeur à partir du nœud 'A' :")
bfs(graph, 'A')

