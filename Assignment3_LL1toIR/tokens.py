from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    IDENTIFIER = 'name'
    NUMBER     = 'num'
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
    WRITE      = 21

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")

    def checkIfKeyword(tokenText):
        for kind in TokenType:
            # 20 and 21 below will change as more keywords are added
            if kind.name.lower() == tokenText and (kind.value == 20 or kind.value == 21):
                return kind
        return None
