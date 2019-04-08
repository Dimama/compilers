
class Production:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Grammar:
    """
    Class describing grammar
    """
    EPS = "EPS"

    def __init__(self, non_terminals: set, terminals: set, productions: list, start_symbol: str):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def add_production(self, left, right):
        self.productions.append(Production(left, right))

    def delete_eps_productions(self):
        for production in self.productions:
            if len(production.right) == 1 and production.right[0] == self.EPS:
                self.productions.remove(production)

    def _repr_productions(self):
        repr_string = ""
        for production in self.productions:
            repr_string += "\n {0} -> {1}".format(production.left, "".join(production.right))

        return repr_string

    def __repr__(self):
        return "Nonterminals: {0}\nTerminals: {1}\nStart: {2}\nProductions:{3}".format(self.non_terminals,
                                                                                       self.terminals,
                                                                                       self.start_symbol,
                                                                                       self._repr_productions())
