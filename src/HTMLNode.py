class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children # A list of HTMLNode objects representing the children of this node
        self.props = props # A dictionary of key-value pairs representing the attributes of the HTML tag. 

    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        display_text = ""
        if self.props != None:
            for k, v in self.props.items():
                display_text = display_text + f' {k}="{v}"'
        return display_text
    
    def __repr__(self):
        return f'HTMLNode(tag = "{self.tag}", value = "{self.value}", children = "{self.children}", props = "{self.props}")'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("HTMLNode.LeafNode can not be empty")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"