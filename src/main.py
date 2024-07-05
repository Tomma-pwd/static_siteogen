from textnode import TextNode
from HTMLNode import HTMLNode
def main():
    node = TextNode("This is a text node", "bold", "https://boot.dev")
    print(repr(node))
    HTMLNode1 = HTMLNode("tag", "value", children = None, props = {"href": "https://www.google.com", "target": "_blank"})
    print(HTMLNode1.props_to_html())
    
main()