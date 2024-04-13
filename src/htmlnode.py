

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        string = ""
        if self.props == None:
            return string
        for prop in self.props.items():
            string += f' {prop[0]}="{prop[1]}" '
        return string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, Children: {self.children}, {self.props})"