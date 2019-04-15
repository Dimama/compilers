class ParseTree:
    def __init__(self, value):
        self.value = value
        self.childs = []

    def add_child(self, child):
        self.childs.append(child)

    def __repr__(self):
        return f"{self.value} -> {[child.value for child in self.childs]}"

