from relation import make_relations
from parse import parse
from data import all_tokens, variables, constants, precedence, prefix


if __name__ == "__main__":
    relations = make_relations(all_tokens, variables, constants, prefix, precedence)
    tokens = input('Input sequence separate by space: ').strip().split()
    print(parse(tokens, all_tokens, relations))
