from tokens import TokenType
from nodes import *
from interpreter import Interpreter
from vals import *

checking_num = False   # distinguish between NUM and IDENTIFIER lines

class Parser: 
    def __init__(self, tokens, file):
        self.f = file
        self.tokens = iter(tokens)
        self.advance()
        self.offset_count = 0
        self.identifier_count = 0

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.cur_token = next(self.tokens)
        except StopIteration:
            self.cur_token = None
    
    def parse(self):
        if self.cur_token == None:
            return None

        interpreter = Interpreter(self.f)
        
        while self.cur_token.type != TokenType.EOF:
            result = self.expr()
            interpreter.visit(result)

        if self.cur_token.type != TokenType.EOF:
            self.raise_error()
        
        return self.cur_token

    def expr(self):
        global checking_num
        if checking_num == False and self.cur_token.type == TokenType.IDENTIFIER and self.identifier_count == 0:
            var_name = self.cur_token
            var_node = IdentifierNode(self.cur_token)
            self.advance()
            self.identifier_count += 1

            if self.cur_token.type != TokenType.EQ:
                self.raise_error()
            
            self.advance()
            expr = self.expr()

            if self.cur_token.type != TokenType.SEMICOLON:
                self.raise_error()

            self.advance()
            self.identifier_count = 0
            return VarAssignNode(var_node, expr)

        if self.cur_token.type == TokenType.NUM:
            keyword_name = self.cur_token
            self.advance()

            if self.cur_token.type != TokenType.IDENTIFIER:
                self.raise_error()

            var_name = self.cur_token
            var_node = IdentifierNode(self.cur_token)
            self.advance()   

            if self.cur_token.type != TokenType.EQ:
                self.raise_error()

            self.advance()
            checking_num = True
            expr = self.expr()

            if self.cur_token.type != TokenType.SEMICOLON:
                self.raise_error()

            self.advance()
            global offsets
            offsets[var_name.value] = (self.offset_count * 8)
            self.offset_count += 1
            checking_num = False
            return VarDeclAssignNode(keyword_name, var_node, expr)

        if self.cur_token.type == TokenType.WRITE:
            func_name = self.cur_token
            self.advance()
            
            if self.cur_token.type != TokenType.IDENTIFIER:
                self.raise_error()
            
            var_name = self.cur_token
            var_node = IdentifierNode(self.cur_token)
            self.advance()

            if self.cur_token.type != TokenType.SEMICOLON:
                self.raise_error()
            
            self.advance()

            return WriteNode(func_name, var_node)

        result = self.term()

        while self.cur_token != None and self.cur_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.cur_token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif self.cur_token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.factor()

        while self.cur_token != None and self.cur_token.type in (TokenType.MUL, TokenType.DIV):
            if self.cur_token.type == TokenType.MUL:
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif self.cur_token.type == TokenType.DIV:
                self.advance()
                result = DivideNode(result, self.factor())

        return result

    def factor(self):
        token = self.cur_token

        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()

            if self.cur_token.type != TokenType.RPAREN:
                self.raise_error()

            self.advance()
            return result

        elif token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)

        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            return IdentifierNode(token.value)

        elif token.type == TokenType.PLUS:
            self.advance()
            return PlusNode(self.factor())

        elif token.type == TokenType.MINUS:
            self.advance()
            return MinusNode(self.factor())

        self.raise_error()
            