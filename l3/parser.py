from parse_tree import ParseTree


class Parser:
    def __init__(self, string):
        self.string = string
        self.numbers = [str(i) for i in range(10)]
        self.identifiers = list(chr(i) for i in range(65, 91))
        self.identifiers.extend([chr(i) for i in range(97, 123)])
        self.index = 0
        self.tree = None
        self.parse_error = ""

    def get_tree(self):
        return self.tree

    def accept_string(self):
        return self._expression()

    def _expression(self):
        return self._arithmetic_expression() and self._rel_operation() and self._arithmetic_expression()

    def _arithmetic_expression(self):
        if self._arithmetic_expression() and self._add_operation() and self._term():
            return True

        if self._add_operation() and self._term():
            return True

        if self._term():
            return True

        return False
        # return (self._arithmetic_expression() and self._add_operation() and self._term()) \
        #     or (self._add_operation() and self._term()) or self._term()

    def _term(self):
        if self._multiplier():
            return True

        if self._term() and self._mul_operation() and self._multiplier():
            return True

        return False
        # return self._multiplier() or (self._term() and self._mul_operation() and self._multiplier())

    def _multiplier(self):

        if not self._primary_expression():

            if self._multiplier():
                if self.string[self.index] == "^":
                    self.index += 1
                    if self._primary_expression():
                        return True
                    else:
                        self.index -= 1

            return False
        return True

    def _primary_expression(self):
        if self._number():
            return True

        if self._identifier():
            return True

        if self.string[self.index] == "(":
            self.index += 1
            if self._arithmetic_expression():
                # проверку добавить
                if self.string[self.index] == ")":
                    self.index += 1
                    return True
                else:
                    self.parse_error = "')' not found after arithmetic expression"
            else:
                self.parse_error = "Arithmetic expression not found after '('"
                self.index -= 1

        return False

    def _add_operation(self):
        if self.string[self.index] in ["+", "-"]:
            self.index += 1
            return True

        return False

    def _mul_operation(self):
        if self.string[self.index] in ["*", "/", "%"]:
            self.index += 1
            return True

        return False

    def _rel_operation(self):
        if self.string[self.index] == "<":
            self.index += 1
            if self._out_of_range():
                self.parse_error = "Relation operator can not be last in string"
                return False

            if self.string[self.index] in [">", "="]:
                self.index += 1

            return True

        if self.string[self.index] == ">":
            self.index += 1
            if self._out_of_range():
                self.parse_error = "Relation operator can not be last in string"
                return False

            if self.string[self.index] == "=":
                self.index += 1

            return True

        if self.string[self.index] == "=":
            self.index += 1
            return True

        return False

    def _number(self):
        count = 0
        while True:
            if self._out_of_range():
                break
            if self.string[self.index] in self.numbers:
                self.index += 1
                count += 1
            else:
                break

        return bool(count)

    def _identifier(self):
        count = 0
        while True:
            if self._out_of_range():
                break
            if self.string[self.index] in self.identifiers:
                self.index += 1
                count += 1
            else:
                break

        return bool(count)

    def _out_of_range(self):
        return self.index > (len(self.string) - 1)

    def __repr__(self):
        return f"{self.index}"
