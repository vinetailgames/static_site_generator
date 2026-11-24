from textnode import TextNode, TextType

def text_to_textnodes(text: str) -> list[TextNode]:
    """
    Convert a string of text into a list of TextNode objects.
    """
    return [TextNode(text, TextType.TEXT)]