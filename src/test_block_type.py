import unittest
from block_type import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    def test_block_to_block_type_header(self):
        self.assertEqual(block_to_block_type("# This is a header"), BlockType.HEADER)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```python\nprint('Hello, World!')\n```"), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote."), BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("- This is an unordered list item."), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        self.assertEqual(block_to_block_type("1. This is an ordered list item."), BlockType.ORDERED_LIST)