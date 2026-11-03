import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("This is a text node with **bold** text.", TextType.TEXT),
            TextNode("This is another text node.", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0], TextNode("This is a text node with ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(" text.", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("This is another text node.", TextType.TEXT))

    def test_delimiter_at_start(self):
        old_nodes = [
            TextNode("**bold** text.", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_nodes[1], TextNode(" text.", TextType.TEXT))

    def test_delimiter_at_end(self):
        old_nodes = [
            TextNode("This is a text node with **bold**", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("This is a text node with ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold", TextType.BOLD))

    def test_non_text_node(self):
        old_nodes = [
            TextNode("This is a text node with **bold** text.", TextType.TEXT),
            TextNode("This is a bold node.", TextType.BOLD)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0], TextNode("This is a text node with ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(" text.", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("This is a bold node.", TextType.BOLD))

    def test_odd_delimiter_count_error(self):
        old_nodes = [
            TextNode("This is a text node with **bold", TextType.TEXT)
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes, delimiter, text_type)
