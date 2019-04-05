from automata_build_rules import AutomataRules


class NFAFromRegExp:
    def __init__(self, regexp):
        self.star = "*"
        self.plus = "|"
        self.dot = "."
        self.open_bracket = "("
        self.close_bracket = ")"
        self.operators = [self.plus, self.dot]
        self.regexp = regexp
        self.alphabet = [chr(i) for i in range(65, 91)]
        self.alphabet.extend([chr(i) for i in range(97, 123)])
        self.alphabet.extend([chr(i) for i in range(48, 58)])
        self._build_NFA()

    def get_NFA(self):
        return self.nfa

    def _build_NFA(self):
        language = set()
        self.stack = []
        self.automata = []
        previous = "EPS"

        for char in self.regexp:
            if char in self.alphabet:
                language.add(char)
                if previous != self.dot and (previous in self.alphabet or previous in [self.close_bracket, self.star]):
                    self._add_operator_to_stack(self.dot)
                self.automata.append(AutomataRules.build_basic_struct(char))

            elif char == self.open_bracket:
                if previous != self.dot and (previous in self.alphabet or previous in [self.close_bracket, self.star]):
                    self._add_operator_to_stack(self.dot)
                self.stack.append(char)

            elif char == self.close_bracket:
                if previous in self.operators:
                    raise Exception("Error processing {} after {}".format(char, previous))
                while True:
                    if len(self.stack) == 0:
                        raise Exception("Error processing {}. Stack is empty".format(char))
                    el = self.stack.pop()
                    if el == self.open_bracket:
                        break
                    elif el in self.operators:
                        self._process_operator(el)

            elif char == self.star:
                if previous in self.operators or previous == self.open_bracket or previous == self.star:
                    raise Exception("Error processing {} after {}".format(char, previous))
                self._process_operator(char)

            elif char in self.operators:
                if previous in self.operators or previous == self.open_bracket:
                    raise Exception("Error processing {} after {}".format(char, previous))
                else:
                    self._add_operator_to_stack(char)
            else:

                raise ValueError("Symbol {} is not supported".format(char))

            previous = char

        # process operators in stack
        while len(self.stack):
            operator = self.stack.pop()
            self._process_operator(operator)

        if len(self.automata) > 1:
            print(self.automata)
            raise Exception("Parse regexp failed")

        self.nfa = self.automata.pop()
        self.nfa.language = language

    def _add_operator_to_stack(self, char):
        while True:
            if len(self.stack) == 0:
                break
            top = self.stack[-1]
            if top == self.open_bracket:
                break
            if top == char or top == self.dot:
                operator = self.stack.pop()
                self._process_operator(operator)
            else:
                break
        self.stack.append(char)

    def _process_operator(self, operator):
        if len(self.automata) == 0:
            raise Exception("Error processing operator {}. Stack is empty".format(operator))
        if operator == self.star:
            a = self.automata.pop()
            self.automata.append(AutomataRules.build_star_struct(a))
        elif operator in self.operators:
            if len(self.automata) < 2:
                raise Exception("Need more operands for operator {}".format(operator))
            a = self.automata.pop()
            b = self.automata.pop()
            if operator == self.plus:
                self.automata.append(AutomataRules.build_plus_struct(b, a))
            elif operator == self.dot:
                self.automata.append(AutomataRules.build_dot_struct(b, a))
