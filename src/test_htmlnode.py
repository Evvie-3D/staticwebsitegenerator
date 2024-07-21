import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_node(self):
        node = HTMLNode()
        node2 = HTMLNode("p", "Test")
        node3 = HTMLNode("p", "Test", None, {"href": "https://www.google.com"})

        print(node)
        print(node2)
        print(node3)
    
    def test_leaf(self):
        node = LeafNode("p", "Test")
        node2 = LeafNode("a", "Test", {"href": "https://www.google.com"})

        print(node.to_html())
        print(node2.to_html())

if __name__ == "__main__":
    unittest.main()