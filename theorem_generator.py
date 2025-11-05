from random import choice


def random_theorem() -> str:
    theorems = [
        "Pythagorean Theorem: There exist three numbers a b and c, not all the same, such that a^2 + b^2 = c^2",
        "Lagrange's Theorem: If H is a subgroup of a finite group G, then the order of H divides the order of G",
        "Trivial Theorem of Arithmetic: Most positive integers are very, very, very large."
    ]

    return choice(theorems)