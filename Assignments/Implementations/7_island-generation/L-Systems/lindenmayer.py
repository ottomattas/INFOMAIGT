import random

class LSystem:
    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules

    def evaluate(self, iterations):
        current = self.axiom
        for i in range(iterations):
            new = []
            for c in current:
                if c in self.rules:
                    new.append(str(self.rules[c]))
                else:
                    new.append(c)

            current = ''.join(new)

        return current

class Rule:
    def __init__(self, rule):
        self.rule = rule

    def __str__(self):
        return self.rule

class StochasticRule:
    #A stochastic rule consists of tuples of probabilities and production rules
    def __init__(self, rules):
        self.rules = rules

    def __str__(self):
        rng = random.random()
        for p, r in self.rules:
            if rng <= p:
                return r
            rng -= p
