import itertools

from grammar import Grammar, Production


class GrammarConverter:
    """
    Class to delete eps-productions and left recursion in grammar
    """

    @staticmethod
    def delete_left_recursion(g: Grammar) -> Grammar:
        grammar = Grammar(g.non_terminals, g.terminals, g.productions[:], g.start_symbol)
        grammar = GrammarConverter.delete_eps_productions(grammar)

        non_terms = grammar.non_terminals[:]
        n = len(non_terms)
        for i in range(n):
            for j in range(i):
                cur_productions = []
                for p in grammar.productions:
                    if p.left == non_terms[i] and p.right[0] == non_terms[j] and len(p.right) > 1:  # Ai -> Aj a
                        er_productions = grammar.er_productions(p)
                        cur_productions.extend(er_productions[:])
                    else:
                        cur_productions.append(p)
                grammar.update_productions(cur_productions)

            grammar.delete_directly_left_recursion(non_terms[i])

        return grammar

    @staticmethod
    def delete_eps_productions(g: Grammar) -> Grammar:
        grammar = Grammar(g.non_terminals.copy(), g.terminals.copy(), g.productions[:], g.start_symbol)

        eps_produced_nonterminals = GrammarConverter.find_eps_produced_nonterminals(grammar)
        if len(eps_produced_nonterminals) == 0:
            return grammar

        grammar.delete_eps_productions()

        new_productions = []
        for production in g.productions:
            non_terms_positions = [i for i, value in enumerate(production.right) if value in eps_produced_nonterminals]
            combinations = []
            for i in range(len(non_terms_positions)):
                combinations.extend(itertools.combinations(non_terms_positions, i+1))

            for combination in combinations:
                new_right = [production.right[i] for i in range(len(production.right)) if i not in combination]
                if new_right:
                    new_productions.append(Production(production.left, new_right))

        grammar.productions.extend(new_productions)
        if grammar.start_symbol in eps_produced_nonterminals:
            new_start = grammar.start_symbol + "'"
            grammar.add_production(new_start, [grammar.start_symbol])
            grammar.add_production(new_start, [Grammar.EPS])
            grammar.start_symbol = new_start

        return grammar

    @staticmethod
    def find_eps_produced_nonterminals(g: Grammar) -> set:
        res_set = set()
        for production in g.productions:
            if len(production.right) == 1 and production.right[0] == Grammar.EPS:
                res_set.add(production.left)

        count = len(res_set)
        while True:
            for production in g.productions:
                if set(production.right).issubset(res_set):
                    res_set.add(production.left)
            if len(res_set) != count:
                count = len(res_set)
            else:
                break

        return res_set
