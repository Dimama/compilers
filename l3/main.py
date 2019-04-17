from parse_tree import print_tree
from parser import Parser

if __name__ == "__main__":
    string = "false & ~ A ! ~true & B & C"
    print(string)
    p = Parser(string)
    if p.accept_string():
        print_tree(p.get_tree())

