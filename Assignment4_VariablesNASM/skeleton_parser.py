class Parser: 
    def __init__(self, tokens, book_set = True):
        self.tokens = iter(tokens)
        self.book_set = book_set
        self.parse_results = []

        # grammar rule corresponding to table
        # needed because container is dictionary of lists of lists
        self.rules_lut_book = { 
                           0: 0, 1: 0, 2: 0, 3: 1,
                           4: 2, 5: 0, 6: 0, 7: 1,
                           8: 2, 9: 0, 10: 1, 11: 2
                         }

        self.rules_lut_class = { 
                           0: 0, 1: 0, 2: 0, 3: 1,
                           4: 2, 5: 0, 6: 0, 7: 1,
                           8: 2, 9: 0, 10: 0, 11: 1,
                           12: 0, 13: 1, 14: 2, 15: 3,
                           16: 0, 17: 1
                         }
        
    def advance(self):
        try:
            self.cur_token = next(self.tokens)
        except StopIteration:
            self.cur_token = None

    def skeleton_parser(self, table, grammar):
        self.advance()
        count = 0

        # parse file until done
        while self.cur_token != None:
            word = self.cur_token
            stack = []
            stack.append('eof')
            stack.append('Goal')

            focus = stack[-1]

            while True:
                # line is parsed correctly or reached end of file
                if focus == 'eof' and (word.type.value == 'eof' or word.type.value == 'f'):
                    count = count + 1
                    self.parse_results.append("Valid")
                    # print("Line", count, "is valid\n")
                    self.advance()
                    word = self.cur_token
                    break

                elif focus in grammar.terminals or focus == 'eof':
                    if focus == word.type.value:
                        stack.pop()
                        self.advance()
                        word = self.cur_token
                    else:
                        count = count + 1
                        self.parse_results.append("Invalid")
                        # print("Line", count, "is invalid\n")

                        # give up on this line, parse the next line
                        while (self.cur_token.type.value != 'eof'):
                            self.advance()
                        self.advance()
                        word = self.cur_token
                        break

                # focus is a nonterminal
                else:
                    # made it to the end of the file
                    if word.type.value == 'f':
                        if len(stack) != 0:
                            stack.pop()
                            focus = stack[-1]
                        continue
                    if (focus, word.type.value) in table.keys() and \
                          table[(focus, word.type.value)] != -1:
                        stack.pop()

                        if self.book_set == True:
                            for i in grammar.rules[focus][self.rules_lut_book[table[(focus, word.type.value)]]][::-1]:
                                if i != 'eps':
                                    stack.append(i)
                        else:
                            for i in grammar.rules[focus][self.rules_lut_class[table[(focus, word.type.value)]]][::-1]:
                                if i != 'eps':
                                    stack.append(i)
                    else:
                        count = count + 1
                        self.parse_results.append("Invalid")
                        # print("Invalid expanding focus - Line ", count, " is invalid\n")
                        
                        # give up on this line, parse the next line
                        while (self.cur_token.type.value != 'eof'):
                            self.advance()
                        self.advance()
                        word = self.cur_token
                        break
                    
                focus = stack[-1]

        return self.parse_results

