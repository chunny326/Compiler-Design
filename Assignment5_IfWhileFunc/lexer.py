from tokens import Token, TokenType

WHITESPACE = ' \t'
DIGITS     = '0123456789'

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()
        self.line_count = 1
        self.offset_count = 0
        self.prev_token = ''
        self.scope_level = 0
        self.inside_func = ''

    def advance(self):
        try:
            self.cur_char = next(self.text)
        except StopIteration:
            self.cur_char = None

    def gen_tokens(self, sym_table):
        while self.cur_char != None:
            if self.cur_char in WHITESPACE:
                self.advance()
            elif self.cur_char == '.' or self.cur_char in DIGITS:
                self.prev_token = 'number'
                yield self.gen_num()
            elif self.cur_char.isalpha():
                # leading character is a letter, so this is an identifier or keyword
                yield self.gen_alpha(sym_table)
            elif self.cur_char == '\n':
                self.advance()
                self.line_count = self.line_count + 1
                self.prev_token = 'newline'
                yield Token(TokenType.NEWLINE)
            elif self.cur_char == '+':
                self.advance()
                self.prev_token = '+'
                yield Token(TokenType.PLUS)
            elif self.cur_char == '-':
                self.advance()
                self.prev_token = '-'
                yield Token(TokenType.MINUS)
            elif self.cur_char == '*':
                self.advance()
                self.prev_token = '*'
                yield Token(TokenType.MUL)
            elif self.cur_char == '/':
                self.advance()
                self.prev_token = '/'
                yield Token(TokenType.DIV)
            elif self.cur_char == '^':
                self.advance()
                self.prev_token = '^'
                yield Token(TokenType.POW)
            elif self.cur_char == '_':
                self.advance()
                self.prev_token = '_'
                print("ERROR Line ", self.line_count, ": Invalid token: ", self.prev_token,  sep = "")
                yield Token(TokenType.UNDERSCORE)
            elif self.cur_char == '=':
                self.advance()
                self.prev_token = '='
                yield Token(TokenType.EQ)
            elif self.cur_char == '(':
                self.advance()
                self.prev_token = '('
                yield Token(TokenType.LPAREN)
            elif self.cur_char == ')':
                self.advance()
                self.prev_token = ')'
                yield Token(TokenType.RPAREN)
            elif self.cur_char == '{':
                self.advance()
                self.prev_token = '{'

                # new scope has been added
                self.scope_level += 1

                yield Token(TokenType.LBRACE)
            elif self.cur_char == '}':
                self.advance()
                self.prev_token = '}'
                
                # one level of scope has been closed
                self.scope_level -= 1
                if self.scope_level < 0:
                    print("ERROR Line ", self.line_count, ": } used without {",  sep = "")

                yield Token(TokenType.RBRACE)
            elif self.cur_char == '"':
                self.advance()
                self.prev_token = '"'
                print("ERROR Line ", self.line_count, ": Invalid token: ", self.prev_token,  sep = "")
                yield Token(TokenType.QUOTES)
            elif self.cur_char == ',':
                self.advance()
                self.prev_token = ','
                yield Token(TokenType.COMMA)
            elif self.cur_char == '!':
                self.advance()
                self.prev_token = '!'
                print("ERROR Line ", self.line_count, ": Invalid token: ", self.prev_token,  sep = "")
                yield Token(TokenType.EXCLAME)
            elif self.cur_char == '\\':
                self.advance()
                self.prev_token = '\\'
                print("ERROR Line ", self.line_count, ": Invalid token: ", self.prev_token,  sep = "")
                yield Token(TokenType.BACKSLASH)
            elif self.cur_char == ';':
                self.advance()
                self.prev_token = ';'
                print("ERROR Line ", self.line_count, ": Invalid token: ", self.prev_token,  sep = "")
                yield Token(TokenType.SEMICOLON)
            else:
                self.line_count = self.line_count + 1
                print("ERROR Line ", self.line_count, ": Invalid token: ", self.prev_token,  sep = "")
                while (self.cur_char != '\n'):
                    self.advance()
                self.advance()
        
        # check if number of { } match at the end of processing the file
        if self.scope_level != 0:
            print("ERROR: Number of opening { and closing } are not equal",  sep = "")

        yield Token(TokenType.EOF)

    def gen_alpha(self, sym_table):
        alpha_str = self.cur_char
        self.advance()
        
        # keep reading and appending until no longer reading alphanumeric character
        while True:
            if self.cur_char != None and (self.cur_char.isalnum() or self.cur_char == '_'):
                alpha_str += self.cur_char
                self.advance()
            else:
                break

        # check if value is a keyword or identifier
        keyword = Token.checkIfKeyword(alpha_str)

        if keyword == None:
            # found an Identifier, check if variable has a type, is a function, or is being redeclared
            if self.prev_token == 'num':
                # check if not already in symbol table OR
                # variable is in symbol table, check if variable being declared in new scope
                if alpha_str not in sym_table or self.inside_func != '':
                    sym_table[alpha_str] = [[('num', self.offset_count * 8, self.scope_level, self.line_count)]]
                    self.offset_count += 1
                elif self.scope_level == len(sym_table[alpha_str]):
                    sym_table[alpha_str].append([('num', self.offset_count * 8, self.scope_level, self.line_count)])
                    self.offset_count += 1
                # reject if being declared again
                else:
                    print("ERROR Line ", self.line_count, ": Symbol table - Redeclaration of: ", alpha_str, sep = "")
            elif self.prev_token == 'flum':
                # check if already in symbol table
                if alpha_str not in sym_table or self.inside_func != '':
                    sym_table[alpha_str] = [('flum', self.offset_count * 8, self.scope_level, self.line_count)]
                    self.offset_count += 1
                elif self.scope_level == len(sym_table[alpha_str]):
                    sym_table[alpha_str].append([('flum', self.offset_count * 8, self.scope_level, self.line_count)])
                    self.offset_count += 1
                else:
                    print("ERROR Line ", self.line_count, ": Symbol table - Redeclaration of: ", alpha_str, sep = "")
            elif self.prev_token == 'function':
                # check if not already in symbol table
                if alpha_str not in sym_table:
                    self.inside_func = alpha_str
                    sym_table[alpha_str] = [('function', self.line_count)]
                # reject if function being declared again
                else:
                    print("ERROR Line ", self.line_count, ": Symbol table - Redeclaration of: ", alpha_str, sep = "")
                return Token(TokenType.FUNCNAME, alpha_str)
            # function is being called
            elif alpha_str in sym_table and sym_table[alpha_str][0][0] == 'function':
                return Token(TokenType.FUNCNAME, alpha_str)
            else:
                # variable is not preceded by a type
                # check if variable already in symbol table to see if this is valid
                if alpha_str not in sym_table:
                    print("ERROR Line ", self.line_count, ": Variable never declared: ", alpha_str, sep = "")
            self.prev_token = 'var'
            return Token(TokenType.IDENTIFIER, alpha_str, self.scope_level)
        else:
            self.prev_token = keyword.value
            # function scope is now ended because nothing can occur after gift
            if keyword == 'gift':
                self.inside_func = ''
            return Token(keyword)
        
    def gen_num(self):
        dec_point_count = 0
        number_str = self.cur_char
        self.advance()

        if self.cur_char == None:
            pass
        elif self.cur_char.isalpha():
            self.prev_token = '.'
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
            self.prev_token = 'flum'
            return Token(TokenType.FLOAT, float(number_str))
        
        # else return an int
        self.prev_token = 'num'
        return Token(TokenType.NUMBER, int(number_str))