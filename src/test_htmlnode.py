import unittest

from HTMLNode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_allNone(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)

    def test_eq(self):
        node1 = HTMLNode(tag = "tag", value = "value", children = None, props = None)
        node2 = HTMLNode(tag = "tag", value = "value", children = None, props = None)
        self.assertEqual(node1, node2)

    def test_tag_not_qual(self):
        node1 = HTMLNode(tag = "tag1", value = "value", children = None, props = None)
        node2 = HTMLNode(tag = "tag2", value = "value", children = None, props = None)
        self.assertNotEqual(node1, node2)
    
    def test_props_to_html(self):
        node1 = HTMLNode("tag", "value", children = None, props = {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()