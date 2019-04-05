from nfa import NFAFromRegExp

if __name__ == "__main__":

    # 1. regexp -> NFA
    # 2. NFA -> DFA
    # 3. DFA -> min DFA

    regexp = input("Input regular expression: ")
    nfa = NFAFromRegExp(regexp).get_NFA()
    print(nfa)

    nfa.display_graph("graph.png")
