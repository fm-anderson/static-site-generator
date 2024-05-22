import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            value=None,
            children=None,
            props={"href": "https://www.google.com", "target": "_blank"},
        )
        expected = 'href="https://www.google.com" target="_blank"'
        message = "props_to_html should format attributes correctly"
        self.assertEqual(node.props_to_html(), expected, message)

    def test_no_attributes_props(self):
        node = HTMLNode(tag="p", value="Hello, World!", children=None, props=None)
        expected = ""
        message = (
            "props_to_html should return an empty string when there are no attributes"
        )
        self.assertEqual(node.props_to_html(), expected, message)

    def test_repr(self):
        node = HTMLNode(
            tag="div", value=None, children=[], props={"class": "container"}
        )
        expected = "HTMLNode(tag: div, value: None, children: [], props: {'class': 'container'})"
        message = "repr should correctly represent the HTMLNode object"
        self.assertEqual(repr(node), expected, message)


class TestLeafNode(unittest.TestCase):
    def test_leaf_node_without_value(self):
        message = "Creating a LeafNode without a value should raise a ValueError"
        with self.assertRaises(ValueError, msg=message):
            LeafNode(tag="p", value=None)

    def test_leaf_node_with_no_tag(self):
        node = LeafNode(tag=None, value="Just text")
        expected = "Just text"
        message = "to_html should return raw text when there is no tag"
        self.assertEqual(node.to_html(), expected, message)

    def test_leaf_node_with_tag_and_no_props(self):
        node = LeafNode(tag="p", value="This is a paragraph.")
        expected = "<p>This is a paragraph.</p>"
        message = (
            "to_html should render an HTML tag with value when there are no properties"
        )
        self.assertEqual(node.to_html(), expected, message)

    def test_leaf_node_with_tag_and_props(self):
        node = LeafNode(
            tag="a", value="Click me!", props={"href": "https://www.google.com"}
        )
        expected = '<a href="https://www.google.com">Click me!</a>'
        message = "to_html should render an HTML tag with value and properties"
        self.assertEqual(node.to_html(), expected, message)


if __name__ == "__main__":
    unittest.main()
