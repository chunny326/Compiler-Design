class Grammar:
    # take variable number of grammar rules, produce tuple of all rules
    def __init__(self, *rules):
        self.rules = {}
        for rule in rules:
            if rule.split('->')[0] not in self.rules:
                self.rules[rule.split('->')[0]] = [rule.split('->')[1].split(' ')]
            else:
                self.rules[rule.split('->')[0]].append(rule.split('->')[1].split(' '))

        self.nonterminals = self.nonterms()
        self.terminals = self.terms()

    def __repr__(self):
        return (f"{self.rules}" if self.rules != None else "")
        
    def nonterms(self):
        # set of nonterminals and associated rules
        return list(self.rules.keys())
        
    def terms(self):
        # everything on rhs not in nonterminals is terminal
        terminals = ['eof']  # add in eof because not included in grammar
        for i in self.rules.values():
            for vals in i:
                for val in vals:
                    if val not in self.nonterminals and val not in terminals:
                        terminals.append(val)
        return terminals
