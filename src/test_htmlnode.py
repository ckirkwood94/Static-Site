import unittest

from htmlnode import (
    HTMLNode
)

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello world", None, {"class": "greeting"})
        self.assertEqual(node.props_to_html(), ' class="greeting" ')

    def test_repr(self):
        node_child = HTMLNode("p", "Greeting from Earth")
        node = HTMLNode("div", "Hello world", {node_child}, {"class": "greeting"})
        self.assertEqual("HTMLNode(div, Hello world, Children: {HTMLNode(p, Greeting from Earth, Children: None, None)}, {'class': 'greeting'})", repr(node))

if __name__ == "__main__":
    unittest.main()