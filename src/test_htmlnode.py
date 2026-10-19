import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_with_one_attribute(self):
        node = HTMLNode("img", None, None, {"alt": "Mountain"})
        self.assertEqual(node.props_to_html(), ' alt="Mountain"')

    def test_constructor_stores_values(self):
        child = HTMLNode("em", "Node")
        props = {"class": "message"}
        node = HTMLNode("p", None, [child], props)
        self.assertEqual(node.tag, "p")
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [child])
        self.assertEqual(node.props, props)

    def test_None(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

if __name__ == "__main__":
    unittest.main()