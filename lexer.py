from tok import Token, TokenType

# Keywords dictionary
KEYWORDS = {
    'fn': TokenType.FUNCTION,
    'let': TokenType.LET,
    'true': TokenType.TRUE,
    'false': TokenType.FALSE,
    'if': TokenType.IF,
    'else': TokenType.ELSE,
    'return': TokenType.RETURN
}

def lookup_ident(literal: str) -> TokenType:
    """
    Check if the literal is a keyword, otherwise return IDENT
    """
    return KEYWORDS.get(literal, TokenType.IDENT)
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
        Read and return a complete identifier
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

    def next_token(self) -> Token:
        """
        Determine and return the next token
        """
        self.skip_whitespace()

        if self.ch is None:
            return Token(TokenType.EOF, "")

        token = None
        # Single character tokens
        token_map = {
            '=': self._handle_equal,
            '+': lambda: Token(TokenType.PLUS, self.ch),
            '-': lambda: Token(TokenType.MINUS, self.ch),
            '!': self._handle_bang,
            '/': lambda: Token(TokenType.SLASH, self.ch),
            '*': lambda: Token(TokenType.ASTERISK, self.ch),
            '<': lambda: Token(TokenType.LT, self.ch),
            '>': lambda: Token(TokenType.GT, self.ch),
            ';': lambda: Token(TokenType.SEMICOLON, self.ch),
            ',': lambda: Token(TokenType.COMMA, self.ch),
            '{': lambda: Token(TokenType.LBRACE, self.ch),
            '}': lambda: Token(TokenType.RBRACE, self.ch),
            '(': lambda: Token(TokenType.LPAREN, self.ch),
            ')': lambda: Token(TokenType.RPAREN, self.ch)
        }

        if self.ch in token_map:
            token = token_map[self.ch]()
        elif self._is_letter(self.ch):
            # Handle identifiers and keywords
            literal = self.read_identifier()
            return Token(lookup_ident(literal), literal)
        elif self._is_digit(self.ch):
            # Handle numbers
            literal = self.read_number()
            return Token(TokenType.INT, literal)
        else:
            token = Token(TokenType.ILLEGAL, self.ch)

        self.read_char()
        return token

    def _handle_equal(self) -> Token:
        """
        Handle both single '=' and '==' tokens
        """
        if self.peek_char() == '=':
            ch = self.ch
            self.read_char()
            literal = ch + self.ch
            return Token(TokenType.EQ, literal)
        return Token(TokenType.ASSIGN, self.ch)

    def _handle_bang(self) -> Token:
        """
        Handle both single '!' and '!=' tokens
        """
        if self.peek_char() == '=':
            ch = self.ch
            self.read_char()
            literal = ch + self.ch
            return Token(TokenType.NOT_EQ, literal)
        return Token(TokenType.BANG, self.ch)

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
    # Test the lexer
    input_code = '''
    let add = fn(x, y) { 
        return x + y; 
    }; 
    add(5, 10);
    '''
    lexer = Lexer(input_code)
    
    while True:
        token = lexer.next_token()
        print(token)
        if token.type == TokenType.EOF:
            break

if __name__ == "__main__":
    main()