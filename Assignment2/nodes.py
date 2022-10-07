from dataclasses import dataclass

@dataclass
class NumberNode:
    value: any

    def __repr__(self):
        return f"{self.value}"

@dataclass
class IdentifierNode:
    value: any

    def __repr__(self):
        return f"{self.value}"

@dataclass
class AddNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1}+{self.node2})"

@dataclass
class SubtractNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1}-{self.node2})"

@dataclass
class MultiplyNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1}*{self.node2})"

@dataclass
class DivideNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1}/{self.node2})"

@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"

@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"

@dataclass
class VarDeclAssignNode:
    node1: any
    node2: any
    node3: any

    def __repr__(self):
        return f"({self.node1} {self.node2}={self.node3})"

@dataclass
class VarAssignNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1}={self.node2})"

@dataclass
class WriteNode:
    node1: any
    node2: any

    def __repr__(self):
        return f"({self.node1} {self.node2})"