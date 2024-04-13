import unittest

from htmlnode import (
    HTMLNode,
    LeafNode
)

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello world", None, {"class": "greeting"})
        self.assertEqual(node.props_to_html(), ' class="greeting"')

    def test_repr(self):
        node_child = HTMLNode("p", "Greeting from Earth")
        node = HTMLNode("div", "Hello world", {node_child}, {"class": "greeting"})
        self.assertEqual("HTMLNode(div, Hello world, Children: {HTMLNode(p, Greeting from Earth, Children: None, None)}, {'class': 'greeting'})", repr(node))

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual("<p>This is a paragraph of text.</p>", node.to_html())

    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', node.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()