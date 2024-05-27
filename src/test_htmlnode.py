import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_parent_node_without_tag(self):
        message = "Creating a ParentNode without a tag should raise a ValueError"
        with self.assertRaises(ValueError, msg=message):
            ParentNode(tag=None, children=[LeafNode("span", "test")])

    def test_parent_node_without_children(self):
        message = "Creating a ParentNode without children should raise a ValueError"
        with self.assertRaises(ValueError, msg=message):
            ParentNode(tag="div", children=[])

    def test_parent_node_with_children(self):
        node = ParentNode(
            tag="div",
            children=[
                LeafNode("span", "First child"),
                LeafNode(None, "Just text"),
                LeafNode("a", "Link", {"href": "https://example.com"}),
            ],
        )
        expected = '<div><span>First child</span>Just text<a href="https://example.com">Link</a></div>'
        message = "to_html should render a ParentNode with its children correctly"
        self.assertEqual(node.to_html(), expected, message)

    def test_nested_parent_node(self):
        node = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="p",
                    children=[
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode("span", "Another child"),
            ],
        )
        expected = "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><span>Another child</span></div>"
        message = "to_html should render nested ParentNode objects correctly"
        self.assertEqual(node.to_html(), expected, message)


if __name__ == "__main__":
    unittest.main()
