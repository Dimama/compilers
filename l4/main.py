from relation import make_relation
from parse import parse, ParseError
from data import all_tokens, variables, constants, precedence, prefix


if __name__ == "__main__":
    relation = make_relation(all_tokens, variables, constants, prefix, precedence)
    tokens = list(input('> ').strip().replace(" ", ""))
    try:
        print(parse(tokens, all_tokens, relation))
    except ParseError as e:
        print(f"Error in {e.args[0]} token")

