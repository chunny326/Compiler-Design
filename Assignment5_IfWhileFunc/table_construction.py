from copy import deepcopy

def union(first, add_this):
    n = len(first)
    if len(add_this) != 0:
        for i in add_this:
            if i not in first:
                first.append(i)
    return len(first) != n

def find_first(grammar):
    # first set initialized for nonterminals and terminals
    first = {i: [] for i in grammar.nonterminals}
    first.update((i, [i]) for i in grammar.terminals)

    while True:
        updated = False
        
        # FIRST set
        for nt in grammar.rules:
            for expression in grammar.rules[nt]:
                if 'eps' not in expression and 'eof' not in expression:
                    if 'eps' in first[expression[0]]:
                        rhs = deepcopy(first[expression[0]].remove('eps'))
                    else:
                        rhs = deepcopy(first[expression[0]])

                    i = 0
                    k = len(expression)

                    while ('eps' in first[expression[i]] and i <= k - 1):
                        union(rhs, expression[i + 1].remove('eps'))
                        i = i + 1

                if i == len(expression) - 1 and 'eps' in first[expression[-1]]:
                    if 'eps' not in rhs:
                        rhs.append('eps')
                
                updated |= union(first[nt], rhs)
                
        if not updated:
            return first

def find_follow(grammar, _first):
    first = deepcopy(_first)
    follow = {i: [] for i in grammar.nonterminals}

    follow['Goal'].append('eof')
    
    while True:
        updated = False
        
        # FOLLOW set
        for nt in grammar.rules:
            for expression in grammar.rules[nt]:
                trailer = deepcopy(follow[nt])

                i = len(expression) - 1
                while i >= 0:
                    if expression[i] in grammar.nonterminals:
                        updated |= union(follow[expression[i]], trailer)

                        if 'eps' in first[expression[i]]:
                            first[expression[i]].remove('eps')
                            union(trailer, first[expression[i]])
                            first[expression[i]].append('eps')
                        else:
                            trailer = first[expression[i]]
                    else:
                        trailer = first[expression[i]]

                    i = i - 1

        if not updated:
            return follow

def find_first_plus(first, follow, grammar):
    # FIRST+ set
    first_plus = []
    for nt in grammar.rules:
        for expression in grammar.rules[nt]:
            if 'eps' not in first[expression[0]]:
                first_plus.append(first[expression[0]])
            else:
                temp = deepcopy(first)
                union(temp[expression[0]], follow[nt])
                first_plus.append(temp[expression[0]])
    return first_plus

def construct_table(first_plus, grammar):
    table = {}
    terminals = deepcopy(grammar.terminals)
    terminals.remove('eps')
    nonterminals = deepcopy(grammar.nonterminals)

    for nt in nonterminals:
        for t in terminals:
            table[(nt, t)] = -1
    
    i = 0
    for nt in grammar.rules:
        for expression in grammar.rules[nt]:
            for w in first_plus[i]:
                if w in terminals:
                    if table[(nt, w)] != -1:
                        print("ERROR! Updating LL1 table that already has value at (", nt, ", ", w, ").\n")
                    else:
                        table[(nt, w)] = i

            if 'eof' in first_plus[i]:
                table[(nt, 'eof')] = i
            
            i = i + 1
    return table
