import argparse
import ast
import traceback
from collections.abc import Sequence
from typing import NamedTuple


class SetLiteral(NamedTuple):
    line: int
    col: int


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.literals = []

    def visit_Set(self, node: ast.Set) -> None:
        if isinstance(node, ast.Set):
            lt = SetLiteral(node.lineno, node.col_offset)
            self.literals.append(lt)


def check_file(filename: str) -> int:
    try:
        with open(filename, "rb") as f:
            ast_obj = ast.parse(f.read(), filename=filename)
    except SyntaxError:
        print(f"{filename} - Could not parse ast")
        print()
        print("\t" + traceback.format_exc().replace("\n", "\n\t"))
        print()
        return 1

    visitor = Visitor()
    visitor.visit(ast_obj)

    for lt in visitor.literals:
        print(f"{filename}:{lt.line}:{lt.col} - set literal")

    return int(bool(visitor.literals))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to run")
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        retv |= check_file(filename)
    return retv


if __name__ == "__main__":
    raise SystemExit(main())
