import unittest


def multiply(a: int, b: int) -> int:
    return a * b

# Usually test live in a tests file or module, not inline


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        text_x = 5
        text_y = 10

        self.assertEqual(multiply(text_x, text_y), 50, 'should be 50')


if __name__ == '__main__':
    unittest.main()
