import unittest
from inline_markdown import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ],
        new_nodes,
    )

def test_split_links(self):
    node = TextNode(
        "This is text with a [link](https://example.com) and another [second link](https://example.org)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://example.org"),
        ],
        new_nodes,
    )

def test_split_images_with_non_text_node(self):
    nodes = [
        TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
        TextNode("This is a bold node.", TextType.BOLD),
    ]
    new_nodes = split_nodes_image(nodes)
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("This is a bold node.", TextType.BOLD),
        ],
        new_nodes,
    )

def test_split_links_with_non_text_node(self):
    nodes = [
        TextNode("This is text with a [link](https://example.com)", TextType.TEXT),
        TextNode("This is a bold node.", TextType.BOLD),
    ]
    new_nodes = split_nodes_link(nodes)
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode("This is a bold node.", TextType.BOLD),
        ],
        new_nodes,
    )

def test_split_images_with_odd_delimiter_count_error(self):
    node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png", TextType.TEXT)
    with self.assertRaises(Exception):
        split_nodes_image([node])

def test_split_links_with_odd_delimiter_count_error(self):
    node = TextNode("This is text with a [link](https://example.com", TextType.TEXT)
    with self.assertRaises(Exception):
        split_nodes_link([node])

def test_split_images_with_empty_image_text(self):
    node = TextNode("This is text with an ![](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ],
        new_nodes,
    )

def test_split_links_with_empty_link_text(self):
    node = TextNode("This is text with a [](https://example.com)", TextType.TEXT)
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
        [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("", TextType.LINK, "https://example.com"),
        ],
        new_nodes,
    )
