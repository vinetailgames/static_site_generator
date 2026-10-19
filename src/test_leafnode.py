import unittest
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_props_with_one_attribute(self):
        node = LeafNode("img", None, {"alt": "Mountain"})
        self.assertEqual(node.props_to_html(), ' alt="Mountain"')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_constructor_stores_values(self):
        props = {"class": "message"}
        node = LeafNode("p", "Hello, world!", props)
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.props, props)

    def test_leaf_to_html_props(self):
        props = {"class": "message"}
        node = LeafNode("p", "Hello, world!", props)
        self.assertEqual(node.to_html(), "<p class=\"message\">Hello, world!</p>")

    def test_props_None(self):
        node = LeafNode("p", "Hello, world!")
        self.assertIsNone(node.props)

if __name__ == "__main__":
    unittest.main()