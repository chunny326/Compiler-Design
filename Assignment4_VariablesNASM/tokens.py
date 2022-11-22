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

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")

    def checkIfKeyword(tokenText):
        for kind in TokenType:
            if kind.name.lower() == tokenText and kind.value in ['num', 'print', 'flum']:
                return kind
        return None
