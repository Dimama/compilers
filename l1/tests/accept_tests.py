from unittest import TestCase

from nfa import NFAFromRegExp
from dfa import DFAFromNFA


class Test1(TestCase):

    def setUp(self):
        self.regexp = "(a|b)*"
        self.nfa = NFAFromRegExp(self.regexp).get_NFA()
        self.dfa = DFAFromNFA(self.nfa).get_DFA()

    def test_empty(self):
        self.assertEqual(True, self.dfa.accept_string(""))

    def test_ba(self):
        self.assertEqual(True, self.dfa.accept_string("ba"))

    def test_ab(self):
        self.assertEqual(True, self.dfa.accept_string("ab"))

    def test_a(self):
        self.assertEqual(True, self.dfa.accept_string("a"))

    def test_aaa(self):
        self.assertEqual(True, self.dfa.accept_string("aaa"))

    def test_aabb(self):
        self.assertEqual(True, self.dfa.accept_string("aabb"))

    def test_abc(self):
        self.assertEqual(False, self.dfa.accept_string("abc"))


class Test2(TestCase):

    def setUp(self):
        self.regexp = "(a|b)*abb"
        self.nfa = NFAFromRegExp(self.regexp).get_NFA()
        self.dfa = DFAFromNFA(self.nfa).get_DFA()

    def test_empty(self):
        self.assertEqual(False, self.dfa.accept_string(""))

    def test_ba(self):
        self.assertEqual(False, self.dfa.accept_string("ba"))

    def test_ab(self):
        self.assertEqual(False, self.dfa.accept_string("ab"))

    def test_babb(self):
        self.assertEqual(True, self.dfa.accept_string("babb"))

    def test_abb(self):
        self.assertEqual(True, self.dfa.accept_string("abb"))

    def test_ababab(self):
        self.assertEqual(False, self.dfa.accept_string("ababab"))

    def test_bbbbabb(self):
        self.assertEqual(True, self.dfa.accept_string("bbbbabb"))


class Test3(TestCase):

    def setUp(self):
        self.regexp = "b(a|b)(bb|aa)a"
        self.nfa = NFAFromRegExp(self.regexp).get_NFA()
        self.dfa = DFAFromNFA(self.nfa).get_DFA()

    def test_empty(self):
        self.assertEqual(False, self.dfa.accept_string(""))

    def test_babba(self):
        self.assertEqual(True, self.dfa.accept_string("babba"))

    def test_bbbba(self):
        self.assertEqual(True, self.dfa.accept_string("bbbba"))

    def test_bbaaa(self):
        self.assertEqual(True, self.dfa.accept_string("bbaaa"))

    def test_baaaa(self):
        self.assertEqual(True, self.dfa.accept_string("baaaa"))

    def test_aba(self):
        self.assertEqual(False, self.dfa.accept_string("aba"))

    def test_babb(self):
        self.assertEqual(False, self.dfa.accept_string("babb"))

    def test_baaaaa(self):
        self.assertEqual(False, self.dfa.accept_string("baaaaa"))

    def test_bbbbaa(self):
        self.assertEqual(False, self.dfa.accept_string("bbbbaa"))


class Test4(TestCase):
    def setUp(self):
        self.regexp = "a*b*c*d*"
        self.nfa = NFAFromRegExp(self.regexp).get_NFA()
        self.dfa = DFAFromNFA(self.nfa).get_DFA()

    def test_empty(self):
        self.assertEqual(True, self.dfa.accept_string(""))

    def test_abcd(self):
        self.assertEqual(True, self.dfa.accept_string("abcd"))

    def test_ad(self):
        self.assertEqual(True, self.dfa.accept_string("ad"))

    def test_bc(self):
        self.assertEqual(True, self.dfa.accept_string("bc"))

    def test_abbcccdddd(self):
        self.assertEqual(True, self.dfa.accept_string("abbcccdddd"))

    def test_dcba(self):
        self.assertEqual(False, self.dfa.accept_string("dcba"))

    def test_abcde(self):
        self.assertEqual(False, self.dfa.accept_string("abcde"))

    def test_acd(self):
        self.assertEqual(True, self.dfa.accept_string("acd"))

    def test_123(self):
        self.assertEqual(False, self.dfa.accept_string("123"))
