from textnode import TextNode
from HTMLNode import HTMLNode, LeafNode, ParentNode

from inline_markdown import split_nodes_delimiter
def main():
    node = TextNode("This is a text node", "bold", "https://boot.dev")
    print(repr(node))
    HTMLNode1 = HTMLNode("p", "value", children = None, props = {"href": "https://www.google.com", "target": "_blank"})
    print(HTMLNode1.props_to_html())
    print(repr(HTMLNode1))

    LeafNode1 = LeafNode("p", "value", props = {"href": "https://www.google.com", "target": "_blank"})
    print(LeafNode1.to_html())
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    print(node.to_html())
    print("============================")
    node = TextNode("This is text with a `code block` word", TextNode.text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", TextNode.text_type_code)
    for obj in new_nodes:
        print(obj)
main()