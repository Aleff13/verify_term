import unittest
from src.term_checker import TermChecker

class TermCheckerTestClass(unittest.TestCase):

    def test_assertCan_Check_Term(self):
        term = "shooter"
        service = TermChecker([term])
        result, similarity = service.verify_similarity("shootar")[0]

        self.assertIs(term, result)
    
    def test_assertDont_Have_Similarity(self):
        term = "shooter"
        service = TermChecker([term])
        result = service.verify_similarity("baloon")

        self.assertIs(0, len(result))

if __name__ == "__main__":
    unittest.main()