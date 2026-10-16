from textnode import TextNode, TextType

def main():
    example_textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(example_textnode)

main()