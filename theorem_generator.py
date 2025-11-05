from random import choice


def random_theorem() -> str:
    theorems = [
        "Pythagorean Theorem: There exist three numbers a b and c, not all the same, such that a^2 + b^2 = c^2",
        "Lagrange's Theorem: If H is a subgroup of a finite group G, then the order of H divides the order of G",
        "Trivial Theorem of Arithmetic: Most positive integers are very, very, very large."
        "Cayley-Hamilton Theorem: Every square matrix over a commutative ring (such as the real or complex numbers or the integers) satisfies its own characteristic equation.",
        "Thales' Theorem: If A, B, and C are distinct points on a circle where the line AC is a diameter, the angle ∠ ABC is a right angle",
        "The Fundamental Theorem of Algebra: Every non-zero, single-variable, degree n polynomial with complex coefficients has, counted with multiplicity, exactly n complex roots.",
        "The Banach Fixed Point Theorem: Let (X,d) be a non-empty complete metric space with a contraction mapping T : X → X . Then T admits a unique fixed-point x^* in X (i.e. T (x^*) = x^* .",
        "Noether's Theorem: Every continuous symmetry of the action of a physical system with conservative forces has a corresponding conservation law",
        "Fermat's Last Theorem: No three positive integers a, b, and c satisfy the equation a^n + b^n = c^n for any integer value of n greater than 2"
    ]

    return choice(theorems)