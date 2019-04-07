class Grammar:
    """
    Class describing grammar
    """

    def __init__(self, non_terminals: set, terminals: set, productions: dict, start_symbol: str):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol

    def _repr_productions(self):
        repr_string = ""
        for left, rights in self.productions.items():
            for right in rights:
                repr_string += "\n {0} -> {1}".format(left, "".join(right))

        return repr_string

    def __repr__(self):
        return "Nonterminals: {0}\nTerminals: {1}\nStart: {2}\nProductions:{3}".format(self.non_terminals,
                                                                                       self.terminals,
                                                                                       self.start_symbol,
                                                                                       self._repr_productions())
