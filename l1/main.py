"""
    # 1. regexp -> NFA
    # 2. NFA -> DFA
    # 3. DFA -> min DFA
"""

from subprocess import check_call

from nfa import NFAFromRegExp
from dfa import DFAFromNFA


if __name__ == "__main__":
    regexp = input("Input regular expression: ")

    nfa = NFAFromRegExp(regexp).get_NFA()
    dfa_builder = DFAFromNFA(nfa)
    dfa = dfa_builder.get_DFA()
    min_dfa = dfa_builder.get_minimized_DFA()

    print(nfa)
    print(dfa)
    print(min_dfa)

    nfa.display_graph("nfa")
    dfa.display_graph("dfa")
    min_dfa.display_graph("min_dfa")

    strings = ["abb", "ab", "ba", "aaabb", ""]
    for s in strings:
        print("Accept {}: {}".format(s, dfa.accept_string(s)))

    check_call(["eog", "nfa.png"])
    check_call(["eog", "dfa.png"])
    check_call(["eog", "min_dfa.png"])
