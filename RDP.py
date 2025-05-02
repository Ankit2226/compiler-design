class RecursiveDescentParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def match(self, expected_token):
        if self.current_token() == expected_token:
            self.pos += 1
        else:
            raise SyntaxError(f"Expected {expected_token} but got {self.current_token()}")

    def parse_expression(self):
        result = self.parse_term()
        while self.current_token() in ('+', '-'):
            op = self.current_token()
            self.match(op)
            right = self.parse_term()
            if op == '+':
                result += right
            elif op == '-':
                result -= right
        return result

    def parse_term(self):
        token = self.current_token()
        if token is not None and token.isdigit():
            self.match(token)
            return int(token)
        else:
            raise SyntaxError(f"Expected number but got {token}")



def read_expression_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()



def tokenize(expr):
    return expr.split()


if __name__ == "__main__":
    file_path = 'input.txt'
    expr = read_expression_from_file(file_path)
    tokens = tokenize(expr)

    parser = RecursiveDescentParser(tokens)
    try:
        result = parser.parse_expression()
        print(f"Result of '{expr}' is: {result}")
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
