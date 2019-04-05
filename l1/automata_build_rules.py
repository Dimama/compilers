from automata import Automata


class AutomataRules:

    @staticmethod
    def build_basic_struct(value):
        state1 = 1
        state2 = 2
        basic = Automata()
        basic.set_start_state(state1)
        basic.add_final_states(state2)
        basic.add_transitions(state1, state2, value)

        return basic

    @staticmethod
    def build_plus_struct(a: Automata, b: Automata):
        a, m1 = a.new_build_from_number(2)
        b, m2 = b.new_build_from_number(m1)

        plus = Automata()
        plus.set_start_state(1)
        plus.add_final_states(m2)
        plus.add_transitions(plus.start_state, a.start_state, Automata.EPSILON)
        plus.add_transitions(plus.start_state, b.start_state, Automata.EPSILON)
        plus.add_transitions(a.final_states[0], plus.final_states[0], Automata.EPSILON)
        plus.add_transitions(b.final_states[0], plus.final_states[0], Automata.EPSILON)
        plus.add_transition_dict(a.transitions)
        plus.add_transition_dict(b.transitions)

        return plus

    @staticmethod
    def build_star_struct(a: Automata):
        a, m1 = a.new_build_from_number(2)

        star = Automata()
        star.set_start_state(1)
        star.add_final_states(m1)
        star.add_transitions(star.start_state, a.start_state, Automata.EPSILON)
        star.add_transitions(star.start_state, star.final_states[0], Automata.EPSILON)
        star.add_transitions(a.final_states[0], star.final_states[0], Automata.EPSILON)
        star.add_transitions(a.final_states[0], a.start_state, Automata.EPSILON)
        star.add_transition_dict(a.transitions)

        return star

    @staticmethod
    def build_dot_struct(a: Automata, b: Automata):
        a, m1 = a.new_build_from_number(1)
        b, m2 = b.new_build_from_number(m1)

        dot = Automata()
        dot.set_start_state(1)
        dot.add_final_states(m2 - 1)

        # to remove eps-transitions
        trans = b.transitions.pop(b.start_state)
        for key, value in trans.items():
            b.add_transitions(a.final_states[0], key, value)

        # with eps-transitions
        # #dot.add_transitions(a.final_states[0], b.start_state, Automata.EPSILON)
        dot.add_transition_dict(a.transitions)
        dot.add_transition_dict(b.transitions)

        return dot
