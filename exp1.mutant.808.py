from collections import defaultdict

# ---------------------------
# WeightedGraph Class
# ---------------------------
class WeightedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph
        self.edges = []  # List to store the edges (u, v, weight)

    def add_edge(self, u, v, weight):
        """Add a single edge to the graph."""
        if (u, v, weight) not in self.edges:
            self.edges.append((u, v, weight))
            self.adj_list[u].append((v, weight))

    def add_multiple_edges(self, edges):
        """Add multiple edges at once."""
        for u, v, weight in edges:
            self.add_edge(u, v, weight)

    def get_edges(self):
        """Return all edges in the graph."""
        return self.edges

    def print_edges(self):
        """Print the edges of the graph."""
        print("Edges in the graph:")
        for u, v, weight in self.edges:
            print(f"{u} -> {v} (Weight: {weight})")

    def print_adj_list(self):
        """Print the adjacency list of the graph."""
        print("Adjacency List of the graph:")
        for u in self.adj_list:
            print(f"{u} -> {self.adj_list[u]}")

    def is_cyclic_directed(self):
        """Detect if there is a cycle in a directed graph using DFS."""
        visited = [False] * self.vertices
        rec_stack = [False] * self.vertices

        def dfs(v):
            visited[v] = True
            rec_stack[v] = True
            for neighbor, _ in self.adj_list[v]:
                if not visited[neighbor] and dfs(neighbor):
                    return True
                elif rec_stack[neighbor]:
                    return True
            rec_stack[v] = False
            return False

        for node in range(self.vertices):
            if not visited[node]:
                if dfs(node):
                    return True
        return False

    def is_cyclic_undirected(self):
        """Detect if there is a cycle in an undirected graph using DFS."""
        visited = [False] * self.vertices

        def dfs(v, parent):
            visited[v] = True
            for neighbor, _ in self.adj_list[v]:
                if not visited[neighbor]:
                    if dfs(neighbor, v):
                        return True
                elif parent != neighbor:
                    return True
            return False

        for node in range(self.vertices):
            if not visited[node]:
                if dfs(node, -1):
                    return True
        return False

    def is_negative_cycle(self):
        """Detect if there is a negative cycle using Bellman-Ford."""
        dist = [float("inf")] * self.vertices
        dist[0] = 0  # Start from node 0

        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        for u, v, weight in self.edges:
            if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                return True  # Negative cycle detected
        return False

    def reset_graph(self):
        """Reset the graph to its empty state."""
        self.edges = []  # Clear all edges
        self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex

    def union(self, parent, u, v):
        """Union-find helper function."""
        root_u = self.find_parent(parent, u)
        root_v = self.find_parent(parent, v)
        if root_u != root_v:
            parent[root_u] = root_v

    def find_parent(self, parent, v):
        """Find the root of the node using path compression."""
        if parent[v] == -1:
            return v
        parent[v] = self.find_parent(parent, parent[v])
        return parent[v]

    def is_cyclic_undirected_union_find(self):
        """Detect cycles in an undirected graph using Union-Find."""
        parent = [-1] * self.vertices

        for u, v, _ in self.edges:
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x == y:
                return True
            self.union(parent, x, y)
        return False

    # ---------------------------
    # Helper functions for testing
    # ---------------------------

    def reset_graph_helper(self):
        """Reset the graph to an empty state for testing."""
        self.edges = []
        self.adj_list = defaultdict(list)

    def get_edges_helper(self):
        """Return all edges for testing."""
        return None

    def add_multiple_edges_helper(self, edges):
        """Add multiple edges for testing."""
        for edge in edges:
            self.add_edge(*edge)

# ---------------------------
# Helper Class for Cycle Test Results
# ---------------------------
class CycleDetectionResults:
    def __init__(self):
        self.directed_cycle_detected = False
        self.undirected_cycle_detected = False
        self.negative_cycle_detected = False

# ---------------------------
# Additional Functionalities
# ---------------------------

class GraphRenderer:
    def __init__(self, graph):
        """Initialize the renderer for visualizing the graph."""
        self.graph = graph

    def render_edges(self):
        """Render the edges of the graph."""
        print("\nRendering edges of the graph:")
        for u, v, weight in self.graph.get_edges():
            print(f"{u} -> {v} (Weight: {weight})")

    def render_adj_list(self):
        """Render the adjacency list of the graph."""
        print("\nRendering adjacency list:")
        self.graph.print_adj_list()

    def render_summary(self):
        """Render a summary of the graph."""
        print("\nGraph summary:")
        print(f"Total vertices: {self.graph.vertices}")
        print(f"Total edges: {len(self.graph.get_edges())}")
        print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}")
        print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}")
        print(f"Has negative cycle: {self.graph.is_negative_cycle()}")

class WeightedGraphVisualization:
    def __init__(self, graph):
        """Initialize the visualization of weighted graph."""
        self.graph = graph

    def visualize(self):
        """Visualize the graph with weighted edges."""
        print("\nVisualizing the graph:")
        for u, v, weight in self.graph.get_edges():
            print(f"Edge from {u} to {v} with weight {weight}")

# ---------------------------
# Main Program
# ---------------------------

class WeightedGraphHandler:
    def __init__(self, vertices):
        """Initialize the graph handler."""
        self.graph = WeightedGraph(vertices)
        self.renderer = GraphRenderer(self.graph)
        self.visualizer = WeightedGraphVisualization(self.graph)

    def add_edges(self, edges):
        """Add edges to the graph."""
        for edge in edges:
            self.graph.add_edge(*edge)

    def render_graph(self):
        """Render the graph using the renderer."""
        self.renderer.render_edges()
        self.renderer.render_adj_list()

    def visualize_graph(self):
        """Visualize the graph using the visualizer."""
        self.visualizer.visualize()

    def cycle_detection_summary(self):
        """Print the cycle detection summary."""
        print("\nCycle detection summary:")
        print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}")
        print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}")
        print(f"Negative cycle detected: {self.graph.is_negative_cycle()}")

# ---------------------------
# Extended Graph Operations
# ---------------------------

class GraphCycleAnalysis:
    def __init__(self, graph):
        """Initialize cycle analysis on the graph."""
        self.graph = graph
        self.results = CycleDetectionResults()

    def analyze_cycles(self):
        """Analyze different types of cycles in the graph."""
        self.results.directed_cycle_detected = self.graph.is_cyclic_directed()
        self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected()
        self.results.negative_cycle_detected = self.graph.is_negative_cycle()

    def print_analysis(self):
        """Print the analysis results."""
        print(f"Directed cycle detected: {self.results.directed_cycle_detected}")
        print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}")
        print(f"Negative cycle detected: {self.results.negative_cycle_detected}")

# ---------------------------
# Main Function
# ---------------------------

if __name__ == "__main__":
    # Create a graph with 4 vertices (0, 1, 2, 3)
    graph_handler = WeightedGraphHandler(4)

    # Add some sample edges (u, v, weight)
    edges = [
        (0, 1, 10),  # Edge from 0 to 1 with weight 10
        (1, 2, 20),  # Edge from 1 to 2 with weight 20
        (2, 3, 30),  # Edge from 2 to 3 with weight 30
        (3, 0, 40),  # Edge from 3 to 0 with weight 40 (creates a directed cycle: 0 -> 1 -> 2 -> 3 -> 0)
        (0, 2, 50)  # Edge from 0 to 2 with weight 50
    ]

    # Add edges to the graph
    graph_handler.add_edges(edges)

    # Render the graph's edges and adjacency list
    graph_handler.render_graph()

    # Visualize the graph
    graph_handler.visualize_graph()

    # Detect and print the cycle results
    graph_handler.cycle_detection_summary()

    # Analyze cycles in detail
    cycle_analysis = GraphCycleAnalysis(graph_handler.graph)
    cycle_analysis.analyze_cycles()
    cycle_analysis.print_analysis()
