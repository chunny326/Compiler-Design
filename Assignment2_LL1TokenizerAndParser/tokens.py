from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    IDENTIFIER = 0
    NUMBER     = 1
    PLUS       = 2
    MINUS      = 3
    MUL        = 4
    DIV        = 5
    POW        = 6
    EQ         = 7
    LPAREN     = 8
    RPAREN     = 9
    SEMICOLON  = 10
    EOF        = 11
    NEWLINE    = 12
    EMPTY      = 13

    # keywords
    NUM        = 14
    WRITE      = 15

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")

    def checkIfKeyword(tokenText):
        for kind in TokenType:
            # 14 and 15 below will change as more keywords are added
            if kind.name.lower() == tokenText and kind.value >= 14 and kind.value <= 15:
                return kind
        return None
