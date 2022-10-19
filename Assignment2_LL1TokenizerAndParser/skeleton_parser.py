def skeleton_parser(table, grammar):
    word = next_word()
    stack = []
    stack.append('eof')
    stack.append('^')

    focus = stack.pop()

    while True:
        if focus == 'eof' and word == 'eof':
            print("Valid")
            break
        elif focus in grammar.terminals or focus == 'eof':
            if focus == word:
                stack.pop()
                word = next_word()
            else:
                print("Invalid")
        # focus is a nonterminal
        else:
            if table[(focus, word)] != -1:
                stack.pop()
                for stuff in stuff:
                    if beta != '!':
                        stack.append(beta)
            else:
                print("Invalid expanding focus")
            focus = stack.pop()