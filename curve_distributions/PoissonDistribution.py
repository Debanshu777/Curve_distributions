import math

class Poisson:
    def __init__(self, lam):
        """
        Initialize the Poisson distribution with the rate parameter (lambda).
        :param lam: expected number of occurrences (λ)
        """
        self.lam = lam

    def pmf(self, k):
        """
        Probability mass function — calculates the probability of k events.
        :param k: number of events
        :return: probability of exactly k events
        """
        return (math.exp(-self.lam) * self.lam**k) / math.factorial(k)

    def mean(self):
        """
        Returns the mean of the distribution.
        """
        return self.lam

    def variance(self):
        """
        Returns the variance of the distribution.
        """
        return self.lam
