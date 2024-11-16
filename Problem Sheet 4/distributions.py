import math
from math import factorial, comb
import numpy as np


def multinomial_dist(num_of_occurrences, probabilities):
    _num_of_occurrences = np.array(num_of_occurrences)
    _probabilities = np.array(probabilities)

    prod_factorials = np.prod(np.vectorize(factorial)(_num_of_occurrences))
    probabilities_powered = _probabilities ** _num_of_occurrences
    prod_probabilities_powered = np.prod(probabilities_powered)
    term1 = np.divide(factorial(_num_of_occurrences.sum()), prod_factorials)
    return np.multiply(term1, prod_probabilities_powered)


def hypergeometric_dist(x, n, m, k):
    return comb(m, x) * comb((n - m), k - x) / comb(n, k)


def negative_binomial_dist(x, r, p):
    return math.comb(x - 1, r - 1) * (p ** r) * ((1 - p) ** (x - r))
