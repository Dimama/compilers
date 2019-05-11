from unittest import TestCase

from relation import make_relations
from parse import parse
from data import all_tokens, constants, variables, precedence, prefix


class ParserTest(TestCase):
    def setUp(self):
        self.relations = make_relations(all_tokens, variables, constants, prefix, precedence)

    def test1(self):
        tokens = "a < b".split()
        parse_res = parse(tokens, all_tokens, self.relations)
        self.assertEqual(parse_res.result, "a b <")

    def test2(self):
        tokens = "a b c".split()
        parse_res = parse(tokens, all_tokens, self.relations)
        self.assertEqual(parse_res.is_correct, False)

    def test3(self):
        tokens = "( ( ( a / b ) ) )".split()
        parse_res = parse(tokens, all_tokens, self.relations)
        self.assertEqual(parse_res.result, "a b /")

    def test4(self):
        tokens = "( a mod b ) & c".split()
        parse_res = parse(tokens, all_tokens, self.relations)
        self.assertEqual(parse_res.result, "a b mod c &")

    def test5(self):
        tokens = "a mod b mod c +".split()
        parse_res = parse(tokens, all_tokens, self.relations)
        self.assertEqual(parse_res.is_correct, False)

    def test6(self):
        tokens = "a and c xor ( b or c ) and 1".split()
        parse_res = parse(tokens, all_tokens, self.relations)
        self.assertEqual(parse_res.result, "a c and b c or xor 1 and")

    def test7(self):
        tokens = "+' b * ( a -\" c )".split()
        parse_res = parse(tokens, all_tokens, self.relations)
        self.assertEqual(parse_res.result, "b a c -\" * +'")
