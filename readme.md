# Similarity Checker Documentation

Introduction
The Similarity Checker is a Python project that analyzes a string to check if it has a certain similarity with a predefined list of terms. The similarity is measured using the Levenshtein distance algorithm. If the similarity is above a specified threshold, the term is considered similar.

Ensure you have Python installed on your system. You can download it from python.org.

Install Required Packages
Install the python-Levenshtein package using pip:

```bash
    pip install python-Levenshtein
```

Usage
Here is the main module used to check for similarity:

```py
from terms import reference_terms
from term_checker import TermChecker

input_term = str(input("Type a term: "))
similarity_limit = 0.8

checker = TermChecker(reference_terms)
results = checker.verify_similarity(input_term)

if results:
    #do something
    for term, similarity in results:
        if (similarity < youLimit):
            #do something
        else:
            #do something
else:
    #do something
```

- input_term: The input string to be checked.
- terms: A list of reference terms to compare against.
- similarity_limit: The similarity threshold (default is 0.8).

References
python-Levenshtein: Python extension for computing string edit distances and similarities.
