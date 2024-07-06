from textnode import TextNode
from HTMLNode import HTMLNode, LeafNode
def main():
    node = TextNode("This is a text node", "bold", "https://boot.dev")
    print(repr(node))
    HTMLNode1 = HTMLNode("p", "value", children = None, props = {"href": "https://www.google.com", "target": "_blank"})
    print(HTMLNode1.props_to_html())
    print(repr(HTMLNode1))
    LeafNode1 = LeafNode("p", "value", props = {"href": "https://www.google.com", "target": "_blank"})
    print(LeafNode1.to_html())
main()