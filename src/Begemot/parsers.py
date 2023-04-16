from .tokens import TOKENS
from .math.minus import minus
from .math.plus import plus
from .boxes import NumBox
from rply import ParserGenerator

# fmt: off
pg = ParserGenerator(TOKENS, precedence=[
    ("left", ["PLUS", "MINUS"])
])
# fmt: on


@pg.production("main : expr")
def main(p: list):
    """"""
    return p[0]


@pg.production("expr : expr PLUS expr")
@pg.production("expr : expr MINUS expr")
def expr_op(p: list) -> None:
    """"""
    lhs, op, rhs, *_ = p

    _ltok_int = lhs.value
    _rtok_int = rhs.value
    _op_tok_type = op.gettokentype()

    _op_cbs = {"PLUS": plus, "MINUS": minus}
    return NumBox(_op_cbs[_op_tok_type](_ltok_int, _rtok_int))


@pg.production("expr : NUM")
def expr_num(p: list):
    return NumBox(int(p[0].getstr()))

@pg.production("expr : PRINT expr")
def expr_print(p: list):
    print(p[1].value)


parser = pg.build()
