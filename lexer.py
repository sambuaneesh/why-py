from tok import Token, TokenType

# Keywords dictionary with esoteric mappings
KEYWORDS = {
    'rune': TokenType.FUNCTION,
    'manifest': TokenType.LET,
    'verity': TokenType.TRUE,
    'fallacy': TokenType.FALSE,
    'whence': TokenType.IF,
    'elsewise': TokenType.ELSE,
    'yield': TokenType.RETURN
}

# Operator mappings for string literals
OPERATORS = {
    'with': TokenType.ASSIGN,
    'augments': TokenType.PLUS,
    'diminishes': TokenType.MINUS,
    'negate': TokenType.BANG,
    'conjoins': TokenType.ASTERISK,
    'divide': TokenType.SLASH,
    'descends': TokenType.LT,
    'ascends': TokenType.GT,
    'mirrors': TokenType.EQ,
    'diverges': TokenType.NOT_EQ,
    'knot': TokenType.COMMA,
    'seal': TokenType.SEMICOLON,
    'unfold': TokenType.LBRACE,
    'fold': TokenType.RBRACE
}

def lookup_ident(literal: str) -> TokenType:
    """
    Check if the literal is a keyword or operator, otherwise return IDENT
    """
    if literal in KEYWORDS:
        return KEYWORDS[literal]
    if literal in OPERATORS:
        return OPERATORS[literal]
    return TokenType.IDENT

class Lexer:
    def __init__(self, input: str):
        self.input = input
        self.position = 0  # current position in input (points to current char)
        self.read_position = 0  # current reading position in input (after current char)
        self.ch = None  # current char under examination
        self.read_char()

    def read_char(self):
        """
        Read the next character in the input
        """
        if self.read_position >= len(self.input):
            self.ch = None  # Use None instead of 0 in Python
        else:
            self.ch = self.input[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def peek_char(self) -> str:
        """
        Look at the next character without advancing
        """
        if self.read_position >= len(self.input):
            return None
        return self.input[self.read_position]

    def skip_whitespace(self):
        """
        Skip over whitespace characters
        """
        while self.ch in [' ', '\t', '\n', '\r']:
            self.read_char()

    def read_identifier(self) -> str:
        """
        Read and return a complete identifier or keyword
        """
        position = self.position
        while self._is_letter(self.ch):
            self.read_char()
        return self.input[position:self.position]

    def read_number(self) -> str:
        """
        Read and return a complete number
        """
        position = self.position
        while self._is_digit(self.ch):
            self.read_char()
        return self.input[position:self.position]

    def read_string(self) -> str:
        """
        Read and return a complete string literal
        """
        position = self.position + 1  # start after the opening quote
        self.read_char()  # move past the opening quote
        
        while self.ch != '"' and self.ch is not None:
            self.read_char()
        
        if self.ch == '"':
            result = self.input[position:self.position]
            self.read_char()  # move past the closing quote
            return result
        return ""

    def next_token(self) -> Token:
        """
        Determine and return the next token
        """
        self.skip_whitespace()

        if self.ch is None:
            return Token(TokenType.EOF, "")

        token = None
        # Handle string literals
        if self.ch == '"':
            literal = self.read_string()
            return Token(TokenType.STRING, literal)
        # Handle parentheses as they remain unchanged
        elif self.ch == '(':
            token = Token(TokenType.LPAREN, self.ch)
        elif self.ch == ')':
            token = Token(TokenType.RPAREN, self.ch)
        elif self._is_letter(self.ch):
            # Handle identifiers, keywords, and word operators
            literal = self.read_identifier()
            token_type = lookup_ident(literal)
            return Token(token_type, literal)
        elif self._is_digit(self.ch):
            # Handle numbers
            literal = self.read_number()
            return Token(TokenType.INT, literal)
        else:
            token = Token(TokenType.ILLEGAL, self.ch)

        if token is None:
            token = Token(TokenType.ILLEGAL, self.ch)

        self.read_char()
        return token

    @staticmethod
    def _is_letter(ch: str) -> bool:
        """
        Check if the character is a valid letter
        """
        return ch is not None and (
            ('a' <= ch <= 'z') or 
            ('A' <= ch <= 'Z') or 
            ch == '_'
        )

    @staticmethod
    def _is_digit(ch: str) -> bool:
        """
        Check if the character is a digit
        """
        return ch is not None and '0' <= ch <= '9'

# Example usage
def main():
    # Test the lexer with esoteric syntax
    input_code = '''
    manifest add with rune(x knot y) unfold 
        yield x augments y seal 
    fold seal 
    add(5 knot 10) seal
    '''
    lexer = Lexer(input_code)
    
    while True:
        token = lexer.next_token()
        print(token)
        if token.type == TokenType.EOF:
            break

if __name__ == "__main__":
    main()