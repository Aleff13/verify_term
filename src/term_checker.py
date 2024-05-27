import Levenshtein

class TermChecker:
    def __init__(self, terms: list[str], similarity_limit=0.8) -> None:
        self.__terms = terms
        self.__similarity_limit = similarity_limit

    def verify_similarity(self, input):
        results = []
        for term in self.__terms:
            similarity = 1 - (Levenshtein.distance(input, term) / max(len(input), len(term)))
            if similarity >= self.__similarity_limit:
                results.append((term, f"{similarity:.2f}"))

        return results