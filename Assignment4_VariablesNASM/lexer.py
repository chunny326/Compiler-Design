from tokens import Token, TokenType

WHITESPACE = ' \t'
DIGITS     = '0123456789'

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()
        self.line_count = 0

    def advance(self):
        try:
            self.cur_char = next(self.text)
        except StopIteration:
            self.cur_char = None

    def gen_tokens(self):
        while self.cur_char != None:
            if self.cur_char in WHITESPACE:
                self.advance()
            elif self.cur_char == '.' or self.cur_char in DIGITS:
                yield self.gen_num()
            elif self.cur_char.isalpha():
                # leading character is a letter, so this is an identifier or keyword
                yield self.gen_alpha()
            elif self.cur_char == '\n':
                self.advance()
                self.line_count = self.line_count + 1
                yield Token(TokenType.NEWLINE)
            elif self.cur_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.cur_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.cur_char == '*':
                self.advance()
                yield Token(TokenType.MUL)
            elif self.cur_char == '/':
                self.advance()
                yield Token(TokenType.DIV)
            elif self.cur_char == '^':
                self.advance()
                yield Token(TokenType.POW)
            elif self.cur_char == '_':
                self.advance()
                yield Token(TokenType.UNDERSCORE)
            elif self.cur_char == '=':
                self.advance()
                yield Token(TokenType.EQ)
            elif self.cur_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.cur_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            elif self.cur_char == '"':
                self.advance()
                yield Token(TokenType.QUOTES)
            elif self.cur_char == ',':
                self.advance()
                yield Token(TokenType.COMMA)
            elif self.cur_char == '!':
                self.advance()
                yield Token(TokenType.EXCLAME)
            elif self.cur_char == '\\':
                self.advance()
                yield Token(TokenType.BACKSLASH)
            elif self.cur_char == ';':
                self.advance()
                yield Token(TokenType.SEMICOLON)
            else:
                self.line_count = self.line_count + 1
                print("Illegal character found: ", self.cur_char)
                print("Line ", self.line_count, " is invalid\n")
                while (self.cur_char != '\n'):
                    self.advance()
                self.advance()
        
        yield Token(TokenType.EOF)

    def gen_alpha(self):
        alpha_str = self.cur_char
        self.advance()
        
        # keep reading and appending until no longer reading alphanumeric character
        while True:
            if self.cur_char != None and (self.cur_char.isalnum() or self.cur_char == '_'):
                alpha_str += self.cur_char
                self.advance()
            else:
                break

        keyword = Token.checkIfKeyword(alpha_str)
        if keyword == None:
            # found an Identifier
            return Token(TokenType.IDENTIFIER, alpha_str)
        else:
            # found a keyword
            return Token(keyword)
        
    def gen_num(self):
        dec_point_count = 0
        number_str = self.cur_char
        self.advance()

        if self.cur_char == None:
            pass
        elif self.cur_char.isalpha():
            return(Token(TokenType.DECIMAL))

        while self.cur_char != None and (self.cur_char == '.' or self.cur_char in DIGITS):
            if self.cur_char == '.':
                dec_point_count += 1
                if dec_point_count > 1:
                    break

            number_str += self.cur_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        # return a floating point (flum) number
        if '.' in number_str:
            return Token(TokenType.FLOAT, float(number_str))
        
        # else return an int
        return Token(TokenType.NUMBER, int(number_str))