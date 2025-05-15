
import unittest

def is_balanced_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return len(stack) == 0

class TestBalancedParentheses(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(is_balanced_parentheses(""))

    def test_single_pair(self):
        self.assertTrue(is_balanced_parentheses("()"))

    def test_nested(self):
        self.assertTrue(is_balanced_parentheses("(())"))

    def test_unbalanced_left(self):
        self.assertFalse(is_balanced_parentheses("(()"))

    def test_unbalanced_right(self):
        self.assertFalse(is_balanced_parentheses("())"))

    def test_crossed(self):
        self.assertFalse(is_balanced_parentheses("())("))

    def test_multiple_nested(self):
        self.assertTrue(is_balanced_parentheses("((()))"))

    def test_extra_opening(self):
        self.assertFalse(is_balanced_parentheses("((()"))

    def test_extra_closing(self):
        self.assertFalse(is_balanced_parentheses("(()))"))

if __name__ == "__main__":
    unittest.main()
