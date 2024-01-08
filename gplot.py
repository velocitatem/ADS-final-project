def plot_tree(node, G=None, parent=None):
    if G is None:
        G = nx.DiGraph()
    G.add_node(node.value)
    if parent is not None:
        G.add_edge(parent, node.value)
    for child in node.children:
        plot_tree(child, G, node.value)
    return G


# Plot the tree
def plot_optimal_paths(paths, G): # DFS
    for path in paths:
        for i in range(len(path) - 1):
            if G.has_edge(path[i], path[i+1]):
                G.edges[path[i], path[i+1]]['color'] = 'red'
    edges = G.edges(data=True)
    edge_colors = [edge[2]['color'] if 'color' in edge[2] else 'black' for edge in edges]
    pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot', args="-Grankdir=TB")  # Use Graphviz to layout the graph top-down
    nx.draw(G, pos, with_labels=True, edge_color=edge_colors)
    plt.show()

    G = plot_tree(root)
    plot_optimal_paths(paths, G)
