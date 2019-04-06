class Automata:
    EPSILON = "E"

    def __init__(self, language=(0, 1)):
        self.states = set()
        self.start_state = None
        self.final_states = []
        self.transitions = {}
        self.language = set(language)

    def set_start_state(self, state):
        self.start_state = state
        self.states.add(state)

    def add_final_states(self, states):
        if isinstance(states, int):
            states = [states]
        self.final_states += [s for s in states if s not in self.final_states]

    def add_transitions(self, from_state, to_state, value):
        if isinstance(int, str):
            value = set(value)
        self.states.add(from_state)
        self.states.add(to_state)
        if from_state in self.transitions:
            if to_state in self.transitions[from_state]:
                self.transitions[from_state][to_state] = self.transitions[from_state][to_state].union(value)
            else:
                self.transitions[from_state][to_state] = value
        else:
            self.transitions[from_state] = {to_state: value}

    def add_transition_dict(self, transitions):
        for from_state, to_states in transitions.items():
            for state in to_states:
                self.add_transitions(from_state, state, to_states[state])

    def get_transitions(self, state, key):
        if isinstance(state, int):
            state = [state]
        tr_states = set()
        for st in state:
            if st in self.transitions:
                for tns in self.transitions[st]:
                    if key in self.transitions[st][tns]:
                        tr_states.add(tns)
        return tr_states

    def new_build_from_number(self, start_num):
        translations = {}
        for i in list(self.states):
            translations[i] = start_num
            start_num += 1
        rebuild = Automata(self.language)
        rebuild.set_start_state(translations[self.start_state])
        rebuild.add_final_states(translations[self.final_states[0]])
        for from_state, to_states in self.transitions.items():
            for state in to_states:
                rebuild.add_transitions(translations[from_state], translations[state], to_states[state])

        return rebuild, start_num

    def get_e_closure(self, find_state):
        all_states = set()
        states = {find_state}
        while len(states):
            state = states.pop()
            all_states.add(state)
            if state in self.transitions:
                for tns in self.transitions[state]:
                    if Automata.EPSILON in self.transitions[state][tns] and tns not in all_states:
                        states.add(tns)
        return all_states

    def accept_string(self, string):
        current_state = self.start_state
        for ch in string:
            st = list(self.get_transitions(current_state, ch))
            if not len(st):
                return False
            current_state = st[0]
        return current_state in self.final_states

    def display_graph(self, filename):
        from graphviz import Digraph
        g = Digraph("G", filename)
        g.attr(rankdir='LR', size='8,5')
        g.attr('node', shape='doublecircle')
        for state in self.states:
            if state in self.final_states:
                g.node(str(state))

        g.attr("node", shape="circle")
        for from_state, to_states in self.transitions.items():
            for state in to_states:
                for char in to_states[state]:
                    g.edge(str(from_state), str(state), label=char)

        g.view()

    def get_dot_file(self):
        dot_file_str = "digraph DFA {\nrankdir=LR\n"
        if len(self.states) != 0:
            dot_file_str += "root=s1\nstart [shape=point]\nstart->s{}\n".format(self.start_state)
            for state in self.states:
                if state in self.final_states:
                    dot_file_str += "s{} [shape=doublecircle]\n".format(state)
                else:
                    dot_file_str += "s{} [shape=circle]\n".format(state)
            for from_state, to_states in self.transitions.items():
                for state in to_states:
                    for char in to_states[state]:
                        dot_file_str += 's{}->s{} [label="{}"]\n'.format(from_state, state, char)
        dot_file_str += "}"

    def __repr__(self):
        text = "language: {" + ", ".join(map(str, self.language)) + "}\n"
        text += "states: {" + ", ".join(map(str, self.states)) + "}\n"
        text += "start state: " + str(self.start_state) + "\n"
        text += "final states: {" + ", ".join(map(str, self.final_states)) + "}\n"
        text += "transitions:\n"
        for from_state, to_states in self.transitions.items():
            for state in to_states:
                for char in to_states[state]:
                    text += "    " + str(from_state) + " -> " + str(state) + " on '" + char + "'\n"

        return text
