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
    NUM        = 20
    PRINT      = 21
    FLUM       = 22

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")

    def checkIfKeyword(tokenText):
        for kind in TokenType:
            # 20-22 will change as more keywords are added
            if kind.name.lower() == tokenText and (kind.value >= 20 and kind.value <= 22):
                return kind
        return None
