import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
