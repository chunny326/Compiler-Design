class Grammar:
    # take variable number of grammar rules, produce tuple of all rules
    def __init__(self, *rules):
        self.rules = tuple(self.combine(rule) for rule in rules)

    def __repr__(self):
        return (f"{self.rules}" if self.rules != None else "")

    def combine(self, rule):
        return tuple(rule.replace(' ', '').split('->'))

    @staticmethod
    def is_nonterminal(symbol):
        # alphanumeric, uppercase letters are nonterminals
        return symbol.isalpha() and symbol.isupper()
        
    @property
    def nonterminals(self):
        # set of nonterminals and associated rules
        return set(nt for nt, _ in self.rules)
        
    @property
    def terminals(self):
        # everything on rhs not in nonterminals is terminal
        t = set(
                symbol
                for _, rhs in self.rules
                for symbol in rhs
                if not self.is_nonterminal(symbol)
                )
        # add in eof because not included in grammar
        t.add('eof')
        return t
