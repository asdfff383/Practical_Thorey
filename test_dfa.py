
import unittest

def is_accepted_by_dfa(binary_string):
    state = 0  # Start in state 0
    for bit in binary_string:
        if bit not in '01':
            return False
        if bit == '1':
            state = (state + 1) % 3
    return state == 0

class TestDFA(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_accepted_by_dfa(""))

    def test_zero_only(self):
        self.assertTrue(is_accepted_by_dfa("0"))

    def test_single_one(self):
        self.assertFalse(is_accepted_by_dfa("1"))

    def test_two_ones(self):
        self.assertFalse(is_accepted_by_dfa("11"))

    def test_three_ones(self):
        self.assertTrue(is_accepted_by_dfa("111"))

    def test_mixed_accepted(self):
        self.assertTrue(is_accepted_by_dfa("1101"))  # 3 ones

    def test_mixed_rejected(self):
        self.assertFalse(is_accepted_by_dfa("1011"))  # 4 ones

    def test_six_ones(self):
        self.assertTrue(is_accepted_by_dfa("111111"))

    def test_invalid_input(self):
        self.assertFalse(is_accepted_by_dfa("10a11"))

if __name__ == "__main__":
    unittest.main()
