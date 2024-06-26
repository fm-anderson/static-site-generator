class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""

        attribute_list = []
        for key, value in self.props.items():
            attribute_list.append(f'{key}="{value}"')
        return " ".join(attribute_list)

    def __repr__(self):
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        if value is None and tag != "img":
            raise ValueError("Value is required for LeafNode")

    def to_html(self):
        if self.value is None and self.tag != "img":
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value

        props_html = self.props_to_html()
        if self.tag == "img":
            if props_html:
                return f"<{self.tag} {props_html}/>"
            else:
                return f"<{self.tag}/>"
        else:
            if props_html:
                return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("Tag is required for ParentNode")
        if not children:
            raise ValueError("Children are required for ParentNode")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")

        if not self.children:
            raise ValueError("ParentNode must have children")

        props_html = self.props_to_html()
        children_html = "".join(child.to_html() for child in self.children)
        if props_html:
            return f"<{self.tag} {props_html}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"


class TextNode:
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

    def __init__(self, text_type, text=None, url=None, alt=None):
        self.text_type = text_type
        self.text = text
        self.url = url
        self.alt = alt

    def text_node_to_html_node(text_node):
        if text_node.text_type == TextNode.TEXT:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == TextNode.BOLD:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == TextNode.ITALIC:
            return LeafNode("i", text_node.text)
        elif text_node.text_type == TextNode.CODE:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextNode.LINK:
            if not text_node.url:
                raise ValueError("URL is required for link type")
            return LeafNode("a", text_node.text, {"href": text_node.url})
        elif text_node.text_type == TextNode.IMAGE:
            if not text_node.url or not text_node.alt:
                raise ValueError("URL and alt text are required for image type")
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.alt})
        else:
            raise ValueError("Unsupported text node type")
