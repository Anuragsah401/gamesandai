import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges along with weights
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('C', 'D', 3),
    ('C', 'E', 9),
    ('D', 'E', 7)
]

G.add_weighted_edges_from(edges)

# Apply Dijkstra's algorithm to find the shortest path from A to E
shortest_path = nx.dijkstra_path(G, source='A', target='E', weight='weight')
path_length = nx.dijkstra_path_length(G, source='A', target='E', weight='weight')

# Visualize the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=12, font_weight='bold', edge_color='gray')

# Highlight the shortest path
edges_in_path = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=3)

# Show the weights on edges
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title(f"Shortest Path from A to E: {shortest_path} (Length: {path_length})")
plt.show()

# Print the shortest path and its length
print(f"Shortest path from A to E: {shortest_path}")
print(f"Path length: {path_length}")
