import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is a sample text."
        expected_nodes = [TextNode(text, TextType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_empty_string(self):
        text = ""
        expected_nodes = [TextNode(text, TextType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_special_characters(self):
        text = "This is a sample text with special characters: !@#$%^&*()"
        expected_nodes = [TextNode(text, TextType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_multiline_string(self):
        text = "This is a sample text.\nIt has multiple lines."
        expected_nodes = [TextNode(text, TextType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected_nodes)

    def test_unicode_characters(self):
        text = "This is a sample text with unicode characters: 😊🚀"
        expected_nodes = [TextNode(text, TextType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected_nodes)