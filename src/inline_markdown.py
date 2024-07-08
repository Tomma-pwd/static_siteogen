from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for text_node in old_nodes:
        if text_node.text_type != text_type_text:
            new_nodes.append(text_node)
            continue
        if text_node.text_type == text_type_text:
            split_text_list = text_node.text.split(delimiter)
            if not len(split_text_list)%2:
                raise Exception(f"Odd amount of delimiter '{delimiter}' in text: amount = {text_node.text.count(delimiter)}")
            for i in range(len(split_text_list)):
                if split_text_list[i] != '':
                    if i%2:
                        new_nodes.append(TextNode(split_text_list[i], text_type))
                    else:
                        new_nodes.append(TextNode(split_text_list[i], text_type_text))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        image_tuple = extract_markdown_images(node.text)
        if len(image_tuple) == 0:
            new_nodes.append(node)
        else:
            for image in image_tuple:
                split_nodes_text = node.text.split(f"![{image[0]}]({image[1]})")
                if len(split_nodes_text) != 2:
                    raise ValueError("Invalid markdown, image section not closed")
                if split_nodes_text[0] != '':
                    new_nodes.append(TextNode(split_nodes_text[0], text_type_text))
                new_nodes.append(TextNode(image[0], text_type_image, url = image[1]))
                if split_nodes_text[1] != '':
                    new_nodes.append(TextNode(split_nodes_text[0], text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        link_tuple = extract_markdown_links(node.text)
        if len(link_tuple) == 0:
            new_nodes.append(node)
        else:
            for link in link_tuple:
                split_nodes_text = node.text.split(f"![{link[0]}]({link[1]})")
                if len(split_nodes_text) != 2:
                    raise ValueError("Invalid markdown, link section not closed")
                if split_nodes_text[0] != '':
                    new_nodes.append(TextNode(split_nodes_text[0], text_type_text))
                new_nodes.append(TextNode(link[0], text_type_image, url = link[1]))
                if split_nodes_text[1] != '':
                    new_nodes.append(TextNode(split_nodes_text[1], text_type_text))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes