class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self. children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        output = ""
        if self.props == None:
            return output
        for key, value in self.props.items():
            output = output + f" {key}=\"{value}\""
        return output
    
    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value == None:
            raise ValueError("LeafNode requires a value")
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode requires a value")
        elif self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
