from textnode import TextNode
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for text_node in old_nodes:
        if text_node.text_type != TextNode.text_type_text:
            new_nodes.append(text_node)
            break
        if text_node.text_type == TextNode.text_type_text:
            split_text_list = text_node.text.split(delimiter)
            if not len(split_text_list)%2 or len(split_text_list) < 3:
                raise Exception(f"Odd amount of delimiter '{delimiter}' in text: amount = {text_node.text.count(delimiter)}")
            for i in range(len(split_text_list)):
                if i%2:
                    new_nodes.append(TextNode(split_text_list[i], text_type))
                else:
                    new_nodes.append(TextNode(split_text_list[i], TextNode.text_type_text))
            break
    return new_nodes