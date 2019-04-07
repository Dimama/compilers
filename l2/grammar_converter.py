from grammar import Grammar


class GrammarConverter:
    """
    Class to delete eps-productions and left recursion in grammar
    """

    @staticmethod
    def delete_left_recursion(g: Grammar) -> Grammar:
        return g

    @staticmethod
    def delete_eps_productions(g: Grammar) -> Grammar:
        return g
