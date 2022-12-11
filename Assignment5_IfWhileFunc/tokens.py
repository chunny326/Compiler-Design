from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    IDENTIFIER = 'name'
    NUMBER     = 'number'
    FLOAT      = 'number'
    PLUS       = '+'
    MINUS      = '-'
    UMINUS     = '-u'
    MUL        = '*'
    DIV        = '/'
    POW        = '^'
    UNDERSCORE = '_'
    EQ         = '='
    LPAREN     = '('
    RPAREN     = ')'
    LBRACE     = '{'
    RBRACE     = '}'
    SEMICOLON  = ';'
    QUOTES     = '"'
    EOF        = 'f'
    NEWLINE    = 'eof'
    EMPTY      = ' '
    DECIMAL    = '.'
    COMMA      = ','
    EXCLAME    = '!'
    BACKSLASH  = '\\'

    # keywords
    NUM        = 'num'
    PRINT      = 'print'
    FLUM       = 'flum'
    IF         = 'if'
    WHILE      = 'while'
    FUNCTION   = 'function'
    PARAM1     = 'param1'
    PARAM2     = 'param2'
    PARAM3     = 'param3'
    GIFT       = 'gift'

@dataclass
class Token:
    type: TokenType
    value: any = None
    scope: int = 0

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "") + self.scope

    def checkIfKeyword(tokenText):
        for kind in TokenType:
            if kind.name.lower() == tokenText and kind.value in ['num', 'print', 'flum', 'if', 'while', 'function', 'param1', 'param2', 'param3', 'gift']: 
                return kind
        return None
