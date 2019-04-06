from automata import Automata


class DFAFromNFA:

    def __init__(self, nfa):
        self.dfa = self._build_DFA(nfa)
        self.min_dfa = self._minimize_DFA()

    def get_DFA(self):
        return self.dfa

    def get_minimized_DFA(self):
        return self.min_dfa

    def _build_DFA(self, nfa: Automata):
        all_states = {}
        e_closure = {}
        count = 1

        state1 = nfa.get_e_closure(nfa.start_state)
        e_closure[nfa.start_state] = state1
        dfa = Automata(nfa.language)
        dfa.set_start_state(count)
        states = [[state1, count]]
        all_states[count] = state1
        count += 1

        while len(states):
            [state, from_index] = states.pop()
            for char in dfa.language:
                tr_states = nfa.get_transitions(state, char)
                for s in list(tr_states)[:]:
                    if s not in e_closure:
                        e_closure[s] = nfa.get_e_closure(s)
                    tr_states = tr_states.union(e_closure[s])
                if len(tr_states):
                    if tr_states not in all_states.values():
                        states.append([tr_states, count])
                        all_states[count] = tr_states
                        to_index = count
                        count += 1
                    else:
                        to_index = [k for k, v in all_states.items() if v == tr_states][0]
                    dfa.add_transitions(from_index, to_index, char)

        for value, state in all_states.items():
            if nfa.final_states[0] in state:
                dfa.add_final_states(value)

        return dfa

    def _minimize_DFA(self):
        pass