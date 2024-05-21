import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        message = "The TextNode instances with identical attributes should be equal"
        self.assertEqual(node, node2, message)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text", "italic", "https://www.boot.dev")
        message = "The TextNode instances with different attributes should not be equal"
        self.assertNotEqual(node, node2, message)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is another text node", "bold", "https://www.boot.dev")
        message = "The TextNode instances with different text should not be equal"
        self.assertNotEqual(node, node2, message)

    def test_style_not_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "italic", "https://www.boot.dev")
        message = "The TextNode instances with different styles should not be equal"
        self.assertNotEqual(node, node2, message)

    def test_url_none_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        message = "The TextNode instances with None URLs should be equal"
        self.assertEqual(node, node2, message)

    def test_url_none_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        message = (
            "The TextNode instance with None URL should not be equal to one with a URL"
        )
        self.assertNotEqual(node, node2, message)


if __name__ == "__main__":
    unittest.main()
