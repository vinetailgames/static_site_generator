from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADER = "header"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block: str) -> BlockType:
    if markdown_block.startswith("#"):
        return BlockType.HEADER
    elif markdown_block.startswith("```"):
        return BlockType.CODE
    elif markdown_block.startswith(">"):
        return BlockType.QUOTE
    elif markdown_block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif markdown_block[0].isdigit() and markdown_block[1] == ".":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH