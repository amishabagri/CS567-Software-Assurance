import pytest
from unittest.mock import patch
from exp1 import WeightedGraph
from collections import defaultdict

@pytest.fixture
def graph():
    """Fixture to set up the graph for testing."""
    graph = WeightedGraph(4)  # Create a graph with 4 vertices (0, 1, 2, 3)
    edges = [
        (0, 1, 10),
        (1, 2, 20),
        (2, 3, 30),
        (3, 0, 40),
        (0, 2, 50)
    ]
    graph.add_multiple_edges(edges)  # Add multiple edges
    return graph

def test_add_edge(graph):
    """Test adding a single edge to the graph."""
    graph.add_edge(1, 3, 60)
    edges = graph.get_edges()
    assert (1, 3, 60) in edges, "Edge was not added correctly."

def test_print_edges(graph):
    """Test that the graph edges are printed correctly (side effect)."""
    with patch("builtins.print") as mocked_print:
        graph.print_edges()
        mocked_print.assert_any_call("Edges in the graph:")
        mocked_print.assert_any_call("0 -> 1 (Weight: 10)")
        mocked_print.assert_any_call("1 -> 2 (Weight: 20)")

def test_print_adj_list(graph):
    """Test that the adjacency list is printed correctly (side effect)."""
    with patch("builtins.print") as mocked_print:
        graph.print_adj_list()
        mocked_print.assert_any_call("0 -> [(1, 10), (2, 50)]")
        mocked_print.assert_any_call("1 -> [(2, 20)]")
        mocked_print.assert_any_call("2 -> [(3, 30)]")
        mocked_print.assert_any_call("3 -> [(0, 40)]")

def test_cycle_detection_directed(graph):
    """Test directed cycle detection in the graph."""
    assert graph.is_cyclic_directed(), "Directed cycle not detected."

def test_cycle_detection_undirected(graph):
    """Test undirected cycle detection in the graph."""
    assert graph.is_cyclic_undirected(), "Undirected cycle not detected."

def test_negative_cycle_detection(graph):
    """Test negative cycle detection using Bellman-Ford."""
    assert not graph.is_negative_cycle(), "Negative cycle incorrectly detected."

def test_reset_graph(graph):
    """Test resetting the graph to an empty state."""
    graph.add_edge(0, 1, 10)
    graph.add_edge(1, 2, 20)
    graph.reset_graph()  # Reset the graph

    # Assert adjacency list and edges are reset
    assert graph.get_edges() == []
    assert graph.adj_list == {0: [], 1: [], 2: [], 3: []}

def test_add_multiple_edges(graph):
    """Test adding multiple edges at once."""
    graph.reset_graph()
    new_edges = [
        (0, 1, 10),
        (1, 2, 20)
    ]
    graph.add_multiple_edges(new_edges)
    edges = graph.get_edges()
    assert (0, 1, 10) in edges, "Edge (0, 1) was not added correctly."
    assert (1, 2, 20) in edges, "Edge (1, 2) was not added correctly."

def test_union_find(graph):
    """Test the union-find helper functions."""
    parent = [-1, -1, -1, -1]
    graph.union(parent, 0, 1)
    graph.union(parent, 1, 2)
    graph.union(parent, 2, 3)
    assert graph.find_parent(parent, 0) == graph.find_parent(parent, 3), "Union-find did not work correctly."

def test_union_find_edge_case(graph):
    """Test union-find when trying to union already connected nodes."""
    parent = [-1, -1, -1, -1]
    graph.union(parent, 0, 1)
    graph.union(parent, 1, 2)
    # Union of already connected nodes should not cause recursion errors
    graph.union(parent, 0, 2)
    assert graph.find_parent(parent, 0) == graph.find_parent(parent, 2), "Union-find failed when trying to union already connected nodes."

def test_add_multiple_edges_edge_case(graph):
    """Test adding multiple edges, including duplicates and invalid edges."""
    graph.reset_graph()  # Reset graph before adding new edges
    new_edges = [
        (0, 1, 10),
        (1, 2, 20),
        (0, 1, 10)  # Duplicate edge
    ]
    graph.add_multiple_edges(new_edges)
    edges = graph.get_edges()
    assert edges.count((0, 1, 10)) == 1, "Duplicate edge added."

def test_reset_graph_helper(graph):
    """Test resetting the graph using the helper method."""
    graph.add_edge(0, 1, 10)
    graph.add_edge(1, 2, 20)

    # Use the helper method to reset the graph
    graph.reset_graph_helper()

    # Assert the graph is reset (no edges, empty adjacency list)
    assert graph.get_edges_helper() == [], "Edges were not reset correctly."
    assert graph.adj_list == defaultdict(list), "Adjacency list was not reset correctly."

def test_get_edges_helper(graph):
    """Test getting edges using the helper method."""
    graph.add_edge(0, 1, 10)
    graph.add_edge(1, 2, 20)

    edges = graph.get_edges_helper()

    # Check if the edges are returned correctly
    assert (0, 1, 10) in edges, "Edge (0, 1) was not returned correctly."
    assert (1, 2, 20) in edges, "Edge (1, 2) was not returned correctly."

