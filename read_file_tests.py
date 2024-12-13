import unittest
import networkx as nx
import csv
from read_file import create_grapf_from_csv


class TestGraphCreation(unittest.TestCase):
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            create_grapf_from_csv("niema.csv")

    def test_empty_file(self):
        with self.assertRaises(ValueError):
            create_grapf_from_csv("empty.csv")

    def test_invalid_csv_format(self):
        with self.assertRaises(csv.Error):
            create_grapf_from_csv("invalid.csv")

    def test_graph_creation(self):
        graph = create_grapf_from_csv("dataset1000.csv")
        self.assertIsInstance(graph, nx.Graph)
        self.assertGreater(len(graph.nodes), 0)


if __name__ == "__main__":
    unittest.main()
