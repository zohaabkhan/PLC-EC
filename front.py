import re


class lex:
    # Token row
    lin_num = 1
    def tokenize(self, code):
        rules = [
            ('AND',r'and'),
            ('OR',r'or'),
            ('NAH',r'nah'),
            ('TRU',r'Tru'),
            ('FALSE',r'False'),
            ('IMPORT',r'import'),
            ('FROM',r'from'),
            ('CLASS',r'class'),
            ('DEF',r'def'),
            ('IF',r'if'),
            ('IFEL',r'ifel'),
            ('ELSE',r'else'),
            ('FOR',r'for'),
            ('WHILE',r'while'),
            ('RETURN',r'return'),
            ('TRY',r'try'),
            ('EXCEPT',r'except'),
            ('FLOAT',r'\d(\d)*\.\d(\d)*'),
            ('INT',r'\d(\d)*'),
            ('STRING',r'\"[a-zA-Z]\w*\"'),
            ('CHAR',r'\'[a-zA-Z]\''),
            ('BOOL',r'bool'),
            ('GLOBAL',r'global'),
            ('NONLOCAL',r'nonlocal'),
            ('PRINT',r'print'),
            #bool
            ('GREATER',r'>'),
            ('GREATER_EQUAL',r'>='),
            ('LESS',r'<'),
            ('LESS_EQUAL',r'<='),
            ('EQUAL_TO',r'=='),
            ('DOESNT_EQUAL',r'!='),
            ('EQUAL',r'='),
            ('PLUS_EQUAL',r'\+='),
            ('MINUS_EQUAL',r'-='),
            ('TIMES_EQUAL',r'\*='),
            ('PLUS',r'\+'),
            ('MINUS',r'\+'),
            ('TIMES',r'\*'),
            ('DIV',r'\/'),
            ('ID',r'[a-zA-Z]\w*'),
            #('FLOAT',r'\d(\d)*\.\d(\d)*'),
            ('NEWLINE', r'\n'),
            ('SKIP', r'[ \t]+'),        # SPACE and TABS
            ('LEFT_PAREN', r'\('),
            ('RIGHT_PAREN', r'\)'),
            #('QUOTE', r'\"'),
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        lin_start = 0

        # Lists of output for the program
        token = []
        lexeme = []
        row = []
        column = []

        # It analyzes the code to find the lexemes and their respective Tokens
        for i in re.finditer(tokens_join, code):
            token_type = i.lastgroup
            token_lexeme = i.group(token_type)

            if token_type == 'NEWLINE':
                lin_start = i.end()
                self.lin_num += 1
                token.append(token_type)
            elif token_type == 'SKIP':
                continue
            else:
                    col = i.start() - lin_start
                    column.append(col)
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    row.append(self.lin_num)
                    # To print information about a Token
                    
        print(token)
        return token
