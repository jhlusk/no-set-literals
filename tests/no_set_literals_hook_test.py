import ast

import pytest

from no_set_literals.no_set_literals_hook import SetLiteral, Visitor


@pytest.mark.parametrize(
    "expression,literals",
    [
        ("{1, 2, 3}", [SetLiteral(line=1, col=0)]),
        ("set((1, 2, 3))", []),
    ],
)
def test_non_dict_exprs(expression, literals):
    visitor = Visitor()
    visitor.visit(ast.parse(expression))
    assert visitor.literals == literals
