from typing import List, Optional, Callable, Dict
from enum import Enum, auto
from lexer import Lexer, Token, TokenType
from ast1 import (
    Program, 
    Statement, 
    Expression,
    LetStatement, 
    ReturnStatement,
    ExpressionStatement,
    Identifier, 
    IntegerLiteral,
    BooleanLiteral,
    PrefixExpression,
    InfixExpression,
    GroupedExpression,
    IfExpression, 
    BlockStatement, 
    FunctionLiteral, 
    CallExpression
)

# Precedence levels
class Precedence(Enum):
    LOWEST = auto()
    EQUALS = auto()      # ==
    LESSGREATER = auto() # > or <
    SUM = auto()         # +
    PRODUCT = auto()     # *
    PREFIX = auto()      # -X or !X
    CALL = auto()        # myFunction(X)

# Precedence mapping
PRECEDENCES = {
    TokenType.EQ: Precedence.EQUALS,
    TokenType.NOT_EQ: Precedence.EQUALS,
    TokenType.LT: Precedence.LESSGREATER,
    TokenType.GT: Precedence.LESSGREATER,
    TokenType.PLUS: Precedence.SUM,
    TokenType.MINUS: Precedence.SUM,
    TokenType.SLASH: Precedence.PRODUCT,
    TokenType.ASTERISK: Precedence.PRODUCT,
    TokenType.LPAREN: Precedence.CALL,
}

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        
        # Current and peek tokens
        self.cur_token = None
        self.peek_token = None
        
        # Errors list
        self.errors: List[str] = []
        
        # Prefix and infix parse function registries
        self.prefix_parse_fns: Dict[TokenType, Callable[[], Optional[Expression]]] = {}
        self.infix_parse_fns: Dict[TokenType, Callable[[Expression], Optional[Expression]]] = {}
        
        # Register prefix parse functions
        self._register_prefix_fns()
        
        # Register infix parse functions
        self._register_infix_fns()
        
        # Advance tokens twice to set both current and peek tokens
        self.next_token()
        self.next_token()
        
    def _register_prefix_fns(self):
        """Register prefix parse functions"""
        self.prefix_parse_fns = {
            TokenType.IDENT: self.parse_identifier,
            TokenType.INT: self.parse_integer_literal,
            TokenType.BANG: self.parse_prefix_expression,
            TokenType.MINUS: self.parse_prefix_expression,
            TokenType.TRUE: self.parse_boolean,
            TokenType.FALSE: self.parse_boolean,
            TokenType.LPAREN: self.parse_grouped_expression,
            TokenType.IF: self.parse_if_expression,
            TokenType.FUNCTION: self.parse_function_literal,
        }

    def _register_infix_fns(self):
        """Register infix parse functions"""
        self.infix_parse_fns = {
            TokenType.PLUS: self.parse_infix_expression,
            TokenType.MINUS: self.parse_infix_expression,
            TokenType.SLASH: self.parse_infix_expression,
            TokenType.ASTERISK: self.parse_infix_expression,
            TokenType.EQ: self.parse_infix_expression,
            TokenType.NOT_EQ: self.parse_infix_expression,
            TokenType.LT: self.parse_infix_expression,
            TokenType.GT: self.parse_infix_expression,
            TokenType.LPAREN: self.parse_call_expression,
        }

    def next_token(self):
        """Move to the next token, shifting current and peek tokens"""
        self.cur_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def cur_token_is(self, token_type: TokenType) -> bool:
        """Check if the current token is of the specified type"""
        return self.cur_token.type == token_type

    def peek_token_is(self, token_type: TokenType) -> bool:
        """Check if the peek token is of the specified type"""
        return self.peek_token.type == token_type

    def expect_peek(self, token_type: TokenType) -> bool:
        """
        Check if the next token is of the expected type.
        If so, advance to the next token. Otherwise, add an error.
        """
        if self.peek_token_is(token_type):
            self.next_token()
            return True
        else:
            self.peek_error(token_type)
            return False

    def peek_error(self, token_type: TokenType):
        """Add an error message about unexpected token type"""
        error_msg = (
            f"expected next token to be {token_type}, "
            f"got {self.peek_token.type} instead"
        )
        self.errors.append(error_msg)

    def peek_precedence(self) -> Precedence:
        """Get the precedence of the peek token"""
        return PRECEDENCES.get(self.peek_token.type, Precedence.LOWEST)

    def cur_precedence(self) -> Precedence:
        """Get the precedence of the current token"""
        return PRECEDENCES.get(self.cur_token.type, Precedence.LOWEST)

    def parse_program(self) -> Program:
        """Parse the entire program, collecting statements"""
        program = Program(statements=[])

        while not self.cur_token_is(TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                program.statements.append(stmt)
            self.next_token()

        return program

    def parse_statement(self) -> Optional[Statement]:
        """Determine and parse the type of statement"""
        if self.cur_token.type == TokenType.LET:
            return self.parse_let_statement()
        elif self.cur_token.type == TokenType.RETURN:
            return self.parse_return_statement()
        else:
            return self.parse_expression_statement()

    def parse_let_statement(self) -> Optional[LetStatement]:
        """Parse a let statement"""
        # Create the initial let statement with the LET token
        stmt = LetStatement(
            token=self.cur_token,
            name=None,
            value=None
        )

        # Expect an identifier after LET
        if not self.expect_peek(TokenType.IDENT):
            return None

        # Create the identifier
        stmt.name = Identifier(
            token=self.cur_token,
            value=self.cur_token.literal
        )

        # Expect an assignment token
        if not self.expect_peek(TokenType.ASSIGN):
            return None

        # Parse the value expression
        self.next_token()
        stmt.value = self.parse_expression(Precedence.LOWEST)

        # Optional semicolon
        if self.peek_token_is(TokenType.SEMICOLON):
            self.next_token()

        return stmt

    def parse_return_statement(self) -> Optional[ReturnStatement]:
        """Parse a return statement"""
        stmt = ReturnStatement(
            token=self.cur_token,
            return_value=None
        )

        # Move to the expression
        self.next_token()

        # Parse the return value expression
        stmt.return_value = self.parse_expression(Precedence.LOWEST)

        # Optional semicolon
        if self.peek_token_is(TokenType.SEMICOLON):
            self.next_token()

        return stmt

    def parse_expression_statement(self) -> Optional[ExpressionStatement]:
        """Parse an expression statement"""
        stmt = ExpressionStatement(
            token=self.cur_token,
            expression=None
        )

        # Parse the expression
        stmt.expression = self.parse_expression(Precedence.LOWEST)

        # Optional semicolon
        if self.peek_token_is(TokenType.SEMICOLON):
            self.next_token()

        return stmt

    def parse_expression(self, precedence: Precedence) -> Optional[Expression]:
        """Parse an expression with given precedence"""
        # Find the prefix parse function for the current token
        prefix_fn = self.prefix_parse_fns.get(self.cur_token.type)
        if not prefix_fn:
            self.no_prefix_parse_fn_error(self.cur_token.type)
            return None

        # Parse the left expression
        left_exp = prefix_fn()

        # Continue parsing infix expressions while precedence allows
        while (not self.peek_token_is(TokenType.SEMICOLON) and 
               precedence.value < self.peek_precedence().value):
            # Find the infix parse function for the peek token
            infix_fn = self.infix_parse_fns.get(self.peek_token.type)
            if not infix_fn:
                return left_exp

            # Move to the infix token
            self.next_token()

            # Parse the infix expression
            left_exp = infix_fn(left_exp)

        return left_exp

    def parse_identifier(self) -> Identifier:
        """Parse an identifier"""
        return Identifier(
            token=self.cur_token, 
            value=self.cur_token.literal
        )

    def parse_integer_literal(self) -> Optional[IntegerLiteral]:
        """Parse an integer literal"""
        try:
            value = int(self.cur_token.literal)
        except ValueError:
            error_msg = f"could not parse {self.cur_token.literal} as integer"
            self.errors.append(error_msg)
            return None

        return IntegerLiteral(
            token=self.cur_token,
            value=value
        )

    def parse_prefix_expression(self) -> Optional[PrefixExpression]:
        """Parse a prefix expression (!, -)"""
        expression = PrefixExpression(
            token=self.cur_token,
            operator=self.cur_token.literal,
            right=None
        )

        # Move to the right side of the expression
        self.next_token()

        # Parse the right side of the expression
        expression.right = self.parse_expression(Precedence.PREFIX)

        return expression

    def parse_infix_expression(self, left: Expression) -> Optional[InfixExpression]:
        """Parse an infix expression (+, -, *, /, ==, !=, <, >)"""
        expression = InfixExpression(
            token=self.cur_token,
            left=left,
            operator=self.cur_token.literal,
            right=None
        )

        # Get current precedence
        precedence = self.cur_precedence()

        # Move to the right side of the expression
        self.next_token()

        # Parse the right side of the expression
        expression.right = self.parse_expression(precedence)

        return expression

    def parse_boolean(self) -> BooleanLiteral:
        """Parse a boolean literal"""
        return BooleanLiteral(
            token=self.cur_token, 
            value=self.cur_token_is(TokenType.TRUE)
        )

    def no_prefix_parse_fn_error(self, token_type: TokenType):
        """Add an error for missing prefix parse function"""
        error_msg = f"no prefix parse function for {token_type} found"
        self.errors.append(error_msg)
        
    def parse_grouped_expression(self) -> Optional[Expression]:
        """Parse an expression within parentheses"""
        # Move past the left parenthesis
        self.next_token()

        # Parse the expression inside the parentheses
        exp = self.parse_expression(Precedence.LOWEST)

        # Expect a right parenthesis to close the grouped expression
        if not self.expect_peek(TokenType.RPAREN):
            return None

        return exp

    def parse_if_expression(self) -> Optional[IfExpression]:
        """Parse an if-else expression"""
        expression = IfExpression(
            token=self.cur_token,
            condition=None,
            consequence=None,
            alternative=None
        )

        # Expect a left parenthesis after 'if'
        if not self.expect_peek(TokenType.LPAREN):
            return None

        # Move to the condition
        self.next_token()
        expression.condition = self.parse_expression(Precedence.LOWEST)

        # Expect a right parenthesis after the condition
        if not self.expect_peek(TokenType.RPAREN):
            return None

        # Expect a left brace for the consequence block
        if not self.expect_peek(TokenType.LBRACE):
            return None

        # Parse the consequence block
        expression.consequence = self.parse_block_statement()

        # Optional else block
        if self.peek_token_is(TokenType.ELSE):
            self.next_token()

            # Expect a left brace for the alternative block
            if not self.expect_peek(TokenType.LBRACE):
                return None

            # Parse the alternative block
            expression.alternative = self.parse_block_statement()

        return expression

    def parse_block_statement(self) -> BlockStatement:
        """Parse a block of statements enclosed in braces"""
        block = BlockStatement(
            token=self.cur_token,
            statements=[]
        )

        # Move past the left brace
        self.next_token()

        # Parse statements until right brace or EOF
        while not self.cur_token_is(TokenType.RBRACE) and not self.cur_token_is(TokenType.EOF):
            stmt = self.parse_statement()
            if stmt:
                block.statements.append(stmt)
            self.next_token()

        return block

    def parse_function_literal(self) -> Optional[FunctionLiteral]:
        """Parse a function literal"""
        lit = FunctionLiteral(
            token=self.cur_token,
            parameters=[],
            body=None
        )

        # Expect a left parenthesis for parameters
        if not self.expect_peek(TokenType.LPAREN):
            return None

        # Parse function parameters
        lit.parameters = self.parse_function_parameters()

        # Expect a left brace for function body
        if not self.expect_peek(TokenType.LBRACE):
            return None

        # Parse function body
        lit.body = self.parse_block_statement()

        return lit

    def parse_function_parameters(self) -> Optional[List[Identifier]]:
        """Parse function parameters"""
        identifiers: List[Identifier] = []

        # If immediately followed by right parenthesis, return empty list
        if self.peek_token_is(TokenType.RPAREN):
            self.next_token()
            return identifiers

        # Move to the first parameter
        self.next_token()

        # Create the first parameter identifier
        ident = Identifier(
            token=self.cur_token,
            value=self.cur_token.literal
        )
        identifiers.append(ident)

        # Parse additional parameters separated by commas
        while self.peek_token_is(TokenType.COMMA):
            # Move past the comma
            self.next_token()
            # Move to the next parameter
            self.next_token()

            # Create the parameter identifier
            ident = Identifier(
                token=self.cur_token,
                value=self.cur_token.literal
            )
            identifiers.append(ident)

        # Expect a right parenthesis at the end
        if not self.expect_peek(TokenType.RPAREN):
            return None

        return identifiers

    def parse_call_expression(self, function: Expression) -> Optional[CallExpression]:
        """Parse a function call expression"""
        exp = CallExpression(
            token=self.cur_token,
            function=function,
            arguments=[]
        )
        
        # Parse call arguments
        exp.arguments = self.parse_call_arguments()
        
        return exp

    def parse_call_arguments(self) -> Optional[List[Expression]]:
        """Parse function call arguments"""
        args: List[Expression] = []

        # If immediately followed by right parenthesis, return empty list
        if self.peek_token_is(TokenType.RPAREN):
            self.next_token()
            return args

        # Move to the first argument
        self.next_token()
        
        # Parse the first argument
        args.append(self.parse_expression(Precedence.LOWEST))

        # Parse additional arguments separated by commas
        while self.peek_token_is(TokenType.COMMA):
            # Move past the comma
            self.next_token()
            # Move to the next argument
            self.next_token()
            
            # Parse the argument
            args.append(self.parse_expression(Precedence.LOWEST))

        # Expect a right parenthesis at the end
        if not self.expect_peek(TokenType.RPAREN):
            return None

        return args


def print_ast(program: Program):
    """
    Print the Abstract Syntax Tree with a visually appealing tree structure, 
    avoiding redundant arrows and names.
    
    Args:
        program (Program): The parsed program to print.
    """
    def _print_node(node, prefix="", is_last=True):
        """
        Recursively print nodes in a tree-like structure.
        
        Args:
            node: The AST node to print.
            prefix (str): The current prefix for tree branches.
            is_last (bool): Whether this node is the last child of its parent.
        """
        connector = "└── " if is_last else "├── "
        if node is None:
            print(f"{prefix}{connector}None")
            return
        
        # Print the current node
        if isinstance(node, Program):
            print(f"{prefix}{connector}Program")
            new_prefix = prefix + ("    " if is_last else "│   ")
            for i, stmt in enumerate(node.statements):
                _print_node(stmt, new_prefix, i == len(node.statements) - 1)
        
        elif isinstance(node, LetStatement):
            print(f"{prefix}{connector}LetStatement")
            new_prefix = prefix + ("    " if is_last else "│   ")
            _print_node(node.name, new_prefix, False)
            _print_node(node.value, new_prefix, True)
        
        elif isinstance(node, ReturnStatement):
            print(f"{prefix}{connector}ReturnStatement")
            new_prefix = prefix + ("    " if is_last else "│   ")
            _print_node(node.return_value, new_prefix, True)
        
        elif isinstance(node, ExpressionStatement):
            print(f"{prefix}{connector}ExpressionStatement")
            new_prefix = prefix + ("    " if is_last else "│   ")
            _print_node(node.expression, new_prefix, True)
        
        elif isinstance(node, Identifier):
            print(f"{prefix}{connector}Identifier: {node.value}")
        
        elif isinstance(node, IntegerLiteral):
            print(f"{prefix}{connector}IntegerLiteral: {node.value}")
        
        elif isinstance(node, BooleanLiteral):
            print(f"{prefix}{connector}Boolean: {node.value}")
        
        elif isinstance(node, PrefixExpression):
            print(f"{prefix}{connector}PrefixExpression")
            new_prefix = prefix + ("    " if is_last else "│   ")
            print(f"{new_prefix}├── Operator: {node.operator}")
            _print_node(node.right, new_prefix, True)
        
        elif isinstance(node, InfixExpression):
            print(f"{prefix}{connector}InfixExpression")
            new_prefix = prefix + ("    " if is_last else "│   ")
            print(f"{new_prefix}├── Operator: {node.operator}")
            _print_node(node.left, new_prefix, False)
            _print_node(node.right, new_prefix, True)
        
        elif isinstance(node, BlockStatement):
            print(f"{prefix}{connector}BlockStatement")
            new_prefix = prefix + ("    " if is_last else "│   ")
            for i, stmt in enumerate(node.statements):
                _print_node(stmt, new_prefix, i == len(node.statements) - 1)
        
        elif isinstance(node, IfExpression):
            print(f"{prefix}{connector}IfExpression")
            new_prefix = prefix + ("    " if is_last else "│   ")
            _print_node(node.condition, new_prefix, False)
            _print_node(node.consequence, new_prefix, False)
            if node.alternative:
                _print_node(node.alternative, new_prefix, True)
        
        elif isinstance(node, FunctionLiteral):
            print(f"{prefix}{connector}FunctionLiteral")
            new_prefix = prefix + ("    " if is_last else "│   ")
            print(f"{new_prefix}├── Parameters:")
            params_prefix = new_prefix + ("    " if len(node.parameters) > 0 else "")
            for i, param in enumerate(node.parameters):
                print(f"{params_prefix}└── {param.value}" if i == len(node.parameters) - 1 else f"{params_prefix}├── {param.value}")
            _print_node(node.body, new_prefix, True)
        
        elif isinstance(node, CallExpression):
            print(f"{prefix}{connector}CallExpression")
            new_prefix = prefix + ("    " if is_last else "│   ")
            _print_node(node.function, new_prefix, False)
            print(f"{new_prefix}└── Arguments:")
            args_prefix = new_prefix + ("    " if len(node.arguments) > 0 else "")
            for i, arg in enumerate(node.arguments):
                _print_node(arg, args_prefix, i == len(node.arguments) - 1)
        
        elif isinstance(node, GroupedExpression):
            print(f"{prefix}{connector}GroupedExpression")
            new_prefix = prefix + ("    " if is_last else "│   ")
            _print_node(node.expression, new_prefix, True)
        
        else:
            print(f"{prefix}{connector}Unknown Node Type: {type(node)}")

    print("Abstract Syntax Tree:")
    _print_node(program)


def main():
    # Example usage with multiple types of expressions
    input_code = """
    let x = 5;
    let y = true;
    return 5 + 5;
    5 - 5;
    5 * 5;
    5 / 5;
    2 > 3;
    3 < 2;
    !true;
    -5;
    let add = fn(x, y) { 
        return x + y; 
    }; 
    add(5, 10); 
    """
    
    lexer = Lexer(input_code)
    parser = Parser(lexer)
    
    program = parser.parse_program()
    
    # Print the complete AST
    print_ast(program)
    
    # Print any parsing errors
    if parser.errors:
        print("\nParsing Errors:")
        for error in parser.errors:
            print(error)

if __name__ == "__main__":
    main()
