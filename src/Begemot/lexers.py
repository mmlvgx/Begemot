from .tokens import TOKENS
from rply import LexerGenerator


lg = LexerGenerator()


view = TOKENS.items()

# Add rules
for tok in view:
    name, pattern = tok
    lg.add(name, pattern)

# Ignore rules
lg.ignore(r"\s+")


lexer = lg.build()
