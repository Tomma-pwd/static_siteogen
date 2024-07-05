class TextNode:
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
    
