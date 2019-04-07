from grammar_converter import GrammarConverter
from grammar_file import GrammarFile


if __name__ == "__main__":

    # filename = input("Input filename with grammar: ")
    filename = "grammar.json"

    try:
        g = GrammarFile.create_grammar_from_file(filename)
    except Exception as e:
        print(e)
    else:
        g_without_recursion = GrammarConverter.delete_left_recursion(g)
        g_without_eps_productions = GrammarConverter.delete_eps_productions(g)

        GrammarFile.save_grammar_to_file(g_without_recursion, "grammar_without_recursion.json")
        GrammarFile.save_grammar_to_file(g_without_eps_productions, "grammar_without_eps_productions.json")

        print("Loaded grammar:\n{}".format(g))
        print("\nWithout left recursion:\n{}".format(g_without_recursion))
        print("\nWithout eps productions:\n{}".format(g_without_eps_productions))
