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
    # print("first: ", first)

    while True:
        updated = False
        
        # FIRST set
        for nt, expression in grammar.rules:
            if '!' not in expression and 'eof' not in expression:
                if '!' in first[expression[0]]:
                    rhs = deepcopy(first[expression[0]].remove('!'))
                else:
                    rhs = deepcopy(first[expression[0]])

                i = 0
                k = len(expression)

                while ('!' in expression[i] and i <= k - 1):
                    union(rhs, expression[i + 1].remove('!'))
                    i = i + 1

            if i == len(expression) - 1 and '!' in first[expression[-1]]:
                if '!' not in rhs:
                    rhs.append('!')
            
            updated |= union(first[nt], rhs)
                
        if not updated:
            return first

def find_follow(grammar, _first):
    first = deepcopy(_first)
    follow = {i: [] for i in grammar.nonterminals}
    # print("\nfollow: ", follow)

    follow['^'] = 'f'
    
    while True:
        updated = False
        
        # FOLLOW set
        for nt, expression in grammar.rules:
            trailer = deepcopy(follow[nt])

            i = len(expression) - 1
            while i >= 0:
                if expression[i] in grammar.nonterminals:
                    updated |= union(follow[expression[i]], trailer)

                    if '!' in first[expression[i]]:
                        first[expression[i]].remove('!')
                        union(trailer, first[expression[i]])
                        first[expression[i]].append('!')
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
    for nt, expression in grammar.rules:
        if '!' not in first[expression[0]]:
            first_plus.append(first[expression[0]])
        else:
            temp = deepcopy(first)
            union(temp[expression[0]], follow[nt])
            first_plus.append(temp[expression[0]])
    return first_plus

def construct_table(first_plus, grammar):
    for nt in grammar.nonterminals:
        for t in grammar.terminals:
            pass
