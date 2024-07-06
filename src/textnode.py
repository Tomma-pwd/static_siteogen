from HTMLNode import LeafNode

class TextNode:
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url 
    
    def __repr__(self):
        display_text = "TextNode("
        display_text = display_text + "'" + self.text + "'"
        display_text = display_text + ", '" + self.text_type + "'"
        if self.text != None:
            display_text = display_text + ", '" + self.url + "'"
        display_text = display_text + ")"
        return display_text

    def text_node_to_html_node(text_node):
        if text_node is TextNode:
            if text_node.text_type == TextNode.text_type_text:
                return LeafNode(None, value = text_node.text)
            if text_node.text_type == TextNode.text_type_bold:
                return LeafNode(tag = "b", value = text_node.text)
            if text_node.text_type == TextNode.text_type_italic:
                return LeafNode(tag = "i", value = text_node.text)
            if text_node.text_type == TextNode.text_type_code:
                return LeafNode(tag = "code", value = text_node.text)
            if text_node.text_type == TextNode.text_type_link:
                return LeafNode(tag = "a", value = text_node.text, prop = {"href":text_node.url})
            if text_node.text_type == TextNode.text_type_image:
                return LeafNode(tag = "img", value = "", prop = {"src":text_node.url, "alt":text_node.text})
            raise ValueError(f"Not supported text_type: {text_node.text_type}")
        else:
            raise TypeError("text_node is not of type TextNode")
    
