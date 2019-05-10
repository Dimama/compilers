from unittest import TestCase

from relation import make_relation
from parse import parse
from data import all_tokens, constants, variables, precedence, prefix


class ParserTest(TestCase):
    def setUp(self):
        self.relation = make_relation(all_tokens, variables, constants, prefix, precedence)

    def test1(self):
        tokens = list("a<b")
        parse_res = parse(tokens, all_tokens, self.relation)
        self.assertEqual(parse_res, "ab<")
