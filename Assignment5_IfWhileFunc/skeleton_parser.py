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

        # count up for each index with rhs the same
        # e.g. Base->num and Base->name are indices 21: 0 and 22: 1
        self.rules_lut_class = { 
                           0: 0, 1: 0, 2: 1, 3: 2,
                           4: 3, 5: 4, 6: 5, 7: 6,
                           8: 7, 9: 0, 10: 0, 11: 1,
                           12: 0, 13: 1, 14: 0, 15: 1,
                           16: 0, 17: 1, 18: 0, 19: 0,
                           20: 1, 21: 0, 22: 0, 23: 1,
                           24: 2, 25: 0, 26: 0, 27: 1,
                           28: 2, 29: 0, 30: 0, 31: 1,
                           32: 0, 33: 1, 34: 2, 35: 3,
                           36: 4, 37: 5, 38: 0, 39: 1,
                           40: 2, 41: 3, 42: 0, 43: 1
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

            # check for blank line
            if word.type.value == 'eof':
                count = count + 1
                self.parse_results.append("Valid")
                # print("Line", count, "is valid\n")
                self.advance()
                continue

            stack = []
            stack.append('eof')
            stack.append('Goal')

            focus = stack[-1]

            while True:
                # check for specific types to match with production names
                if word.type.name in ['NUM', 'FLUM']:
                    word_type = 'dtype'
                elif word.type.name in ['IDENTIFIER']:
                    word_type = 'name'
                elif word.type.name in ['PRINT', 'IF', 'WHILE', 'FUNCTION', 'GIFT']:
                    word_type = word.type.name.lower()
                elif word.type.name in ['PARAM1', 'PARAM2', 'PARAM3']:
                    word_type = 'param'
                else:
                    word_type = word.type.value

                # line is parsed correctly or reached end of file
                if focus == 'eof' and (word_type == 'eof' or word_type == 'f'):
                    count = count + 1
                    self.parse_results.append("Valid")
                    # print("Line", count, "is valid")
                    self.advance()
                    word = self.cur_token
                    break

                elif focus in grammar.terminals or focus == 'eof':
                    if focus == word_type:
                        stack.pop()
                        self.advance()
                        word = self.cur_token
                    else:
                        count = count + 1
                        self.parse_results.append("Invalid")
                        print("ERROR Line ", count, ": Line not supported by language grammar", sep = "")

                        # give up on this line, parse the next line
                        while (self.cur_token.type.value != 'eof'):
                            self.advance()
                        self.advance()
                        word = self.cur_token
                        break

                # focus is a nonterminal
                else:
                    # made it to the end of the file
                    if word_type == 'f':
                        if len(stack) != 0:
                            stack.pop()
                            focus = stack[-1]
                        continue
                    
                    if (focus, word_type) in table.keys() and \
                          table[(focus, word_type)] != -1:
                        stack.pop()

                        if self.book_set == True:
                            for i in grammar.rules[focus][self.rules_lut_book[table[(focus, word_type)]]][::-1]:
                                if i != 'eps':
                                    stack.append(i)
                        else:
                            for i in grammar.rules[focus][self.rules_lut_class[table[(focus, word_type)]]][::-1]:
                                if i != 'eps':
                                    stack.append(i)
                    else:
                        count = count + 1
                        self.parse_results.append("Invalid")
                        print("ERROR Line ", count, ": Line not supported by language grammar", sep = "")
                        
                        # give up on this line, parse the next line
                        while (self.cur_token.type.value != 'eof'):
                            self.advance()
                        self.advance()
                        word = self.cur_token
                        break
                    
                focus = stack[-1]

        return self.parse_results

