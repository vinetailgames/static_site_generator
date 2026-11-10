import re

def extract_markdown_images(text):
    """
    Extracts all image URLs from the given markdown text.

    Args:
        text (str): The markdown text to extract image URLs from.

    Returns:
        list: A list of image URLs found in the markdown text.
    """
    # Regular expression pattern to match markdown image syntax ![alt text](image_url)
    pattern = r'!\[.*?\]\((.*?)\)'
    
    # Find all matches in the text
    image_urls = re.findall(pattern, text)
    
    return image_urls

def extract_markdown_links(text):
    """
    Extracts all link URLs from the given markdown text.

    Args:
        text (str): The markdown text to extract link URLs from.

    Returns:
        list: A list of link URLs found in the markdown text.
    """
    # Regular expression pattern to match markdown link syntax [link text](link_url)
    pattern = r'\[.*?\]\((.*?)\)'
    
    # Find all matches in the text
    link_urls = re.findall(pattern, text)
    
    return link_urls