from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    IDENTIFIER = 'name'
    NUMBER     = 'num'
    PLUS       = '+'
    MINUS      = '-'
    MUL        = '*'
    DIV        = '/'
    POW        = '^'
    EQ         = '='
    LPAREN     = '('
    RPAREN     = ')'
    SEMICOLON  = ';'
    EOF        = 'f'
    NEWLINE    = 'eof'
    EMPTY      = ' '
    DECIMAL    = '.'

    # keywords
    NUM        = 15
    WRITE      = 16

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")

    def checkIfKeyword(tokenText):
        for kind in TokenType:
            # 14 and 15 below will change as more keywords are added
            if kind.name.lower() == tokenText and (kind.value == 15 or kind.value == 16):
                return kind
        return None
