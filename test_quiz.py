import unittest

from demo import Question

class TestQuestion(unittest.TestCase):
    def test_correct_answer(self):
        pytanie = Question("What is the capital of Poland?", {"a": "Warsaw", "b": "Krakow","c": "Gdansk","d": "Wroclaw"}, "a")
        self.assertTrue(pytanie.check_answer("a"))
        self.assertFalse(pytanie.check_answer("b"))


if __name__ == '__main__':
    unittest.main()