def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    strip_markdown = [block.strip() for block in split_markdown]
    block = []
    for block_string in strip_markdown:
        if block_string:
            block.append(block_string)
    return block