from nodes import * 
from file import File
from vals import *

class Interpreter:
    def __init__(self, file):
        self.f = file
        self.reg_list = ['rax', 'rcx']

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return (node.value)

    def visit_IdentifierNode(self, node):
        global offsets
        if (isinstance(node.value, str)):
            result = 'qword[rsp+' + str(offsets[node.value]) + ']'
        else:
            result = 'qword[rsp+' + str(offsets[node.value.value]) + ']'

        return result

    def visit_AddNode(self, node):
        self.f.addition(self.visit(node.node1), self.visit(node.node2))
        return 'rax'

    def visit_SubtractNode(self, node):
        self.f.subtraction(self.visit(node.node1), self.visit(node.node2))
        return 'rax'

    def visit_MultiplyNode(self, node):
        self.f.multiplication(self.visit(node.node1), self.visit(node.node2))
        return 'rax'

    def visit_DivideNode(self, node):
        self.f.division(self.visit(node.node1), self.visit(node.node2))
        return 'rax'

    def visit_PlusNode(self, node):
        return node.value

    def visit_MinusNode(self, node):
        return -node.node.value

    def visit_VarDeclAssignNode(self, node):
        val3 = self.visit(node.node3)
        val2 = self.visit(node.node2)
        if (isinstance(val3, int) == False):
            if (str(val3) not in self.reg_list):
                self.f.variable_assign_variable(val2, val3)
            else:
                self.f.variable_assign(val2, val3)
        else:
            self.f.variable_assign(val2, val3)

    def visit_VarAssignNode(self, node):
        val1 = self.visit(node.node1)
        val2 = self.visit(node.node2)
        if (isinstance(val2, int) == False):
            if (str(val2) not in self.reg_list):
                self.f.variable_assign_variable(val1, val2)
            else:
                self.f.variable_assign(val1, val2)
        else:
            self.f.variable_assign(val1, val2)

    def visit_WriteNode(self, node):
        self.f.print_console(self.visit(node.node2))
