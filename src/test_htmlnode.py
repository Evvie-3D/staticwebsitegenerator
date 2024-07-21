import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_node(self):
        node = HTMLNode()
        node2 = HTMLNode("p", "Test")
        node3 = HTMLNode("p", "Test", None, {"href": "https://www.google.com"})

        print(node)
        print(node2)
        print(node3)

if __name__ == "__main__":
    unittest.main()