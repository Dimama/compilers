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
        states = list(self.dfa.states)
        n = len(states)
        unchecked = dict()
        count = 1
        distinguished = []
        equivalent = dict(zip(range(len(states)), [{s} for s in states]))
        pos = dict(zip(states, range(len(states))))

        for i in range(n - 1):
            for j in range(i + 1, n):
                if not ([states[i], states[j]] in distinguished or [states[j], states[i]] in distinguished):
                    eq = 1
                    to_append = []
                    for char in self.dfa.language:
                        s1 = self.dfa.get_transitions(states[i], char)
                        s2 = self.dfa.get_transitions(states[j], char)
                        if len(s1) != len(s2):
                            eq = 0
                            break
                        if len(s1) > 1:
                            raise BaseException("Multiple transitions detected in DFA")
                        elif len(s1) == 0:
                            continue
                        s1 = s1.pop()
                        s2 = s2.pop()
                        if s1 != s2:
                            if [s1, s2] in distinguished or [s2, s1] in distinguished:
                                eq = 0
                                break
                            else:
                                to_append.append([s1, s2, char])
                                eq = -1
                    if eq == 0:
                        distinguished.append([states[i], states[j]])
                    elif eq == -1:
                        s = [states[i], states[j]]
                        s.extend(to_append)
                        unchecked[count] = s
                        count += 1
                    else:
                        p1 = pos[states[i]]
                        p2 = pos[states[j]]
                        if p1 != p2:
                            st = equivalent.pop(p2)
                            for s in st:
                                pos[s] = p1
                            equivalent[p1] = equivalent[p1].union(st)

        new_found = True
        while new_found and len(unchecked) > 0:
            new_found = False
            for p, pair in list(unchecked.items()):
                for tr in pair[2:]:
                    if [tr[0], tr[1]] in distinguished or [tr[1], tr[0]] in distinguished:
                        unchecked.pop(p)
                        distinguished.append([pair[0], pair[1]])
                        new_found = True
                        break

        for pair in unchecked.values():
            p1 = pos[pair[0]]
            p2 = pos[pair[1]]
            if p1 != p2:
                st = equivalent.pop(p2)
                for s in st:
                    pos[s] = p1
                equivalent[p1] = equivalent[p1].union(st)

        if len(equivalent) == len(states):
            return self.dfa
        else:
            return self.dfa.build_from_equivalent_states(pos)
