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
        eps_produced_nonterminals = GrammarConverter.find_eps_produced_nonterminals(g)

        return g

    @staticmethod
    def find_eps_produced_nonterminals(g: Grammar) -> set:
        res_set = set()
        for left, rights in g.productions.items():
            for right in rights:
                if len(right) == 1 and right[0] == Grammar.EPS:
                    res_set.add(left)

        count = len(res_set)
        while True:
            for left, rights in g.productions.items():
                for right in rights:
                    if set(right).issubset(res_set):
                        res_set.add(left)
            if len(res_set) != count:
                count = len(res_set)
            else:
                break

        return res_set
