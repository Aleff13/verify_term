from terms import reference_terms
from term_checker import TermChecker

if __name__ == "__main__":
    input_term = str(input("Type a term: "))
    similarity_limit = 0.8

    checker = TermChecker(reference_terms)
    results = checker.verify_similarity(input_term)

    if results:
        print(f"The term '{input_term}' has similarity with:")
        for term, similarity in results:
            print(f"Term: {term}, Similarity: {similarity:.2f}")
    else:
        print(f"Nenhum termo semelhante encontrado para '{input_term}'")
