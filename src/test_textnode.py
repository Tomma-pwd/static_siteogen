import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)

    def test_eq_none(self):
        node1 = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", "not none!")
        self.assertNotEqual(node1, node2)
    
    def test_text_not_eq(self):
        node1 = TextNode("This is a text node1", "bold", "")
        node2 = TextNode("This is a text node2", "bold", "")
        self.assertNotEqual(node1, node2)

    def test_text_not_eq(self):
        node1 = TextNode("This is a text node", "not bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()