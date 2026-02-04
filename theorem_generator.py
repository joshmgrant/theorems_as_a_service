from random import choice

"""
Mathematical contributions

Want to contribute a theorem to this service? Excellent!

To add a theorem,
- add a theorem as an entry at the bottom of the list _theorems_,
- (recommended) follow the Local development steps below to verify the app still works as expected.

The theorems do allow formating via [MathJax](https://docs.mathjax.org/en/stable/), and there are a few examples in the previously added theorems.

For example, the first theorem is the Pythagorean theorem:
"Pythagorean Theorem: There exist three numbers $a$, $b$ and $c$, not all the same, such that $a^2 + b^2 = c^2$",

$$ delimit inline mathematical notation, and the whole string uses "" quotes.

Additions will be reviewed and validated. I appreciate all contributions!
"""
def random_theorem() -> str:
    theorems = [
        "Pythagorean Theorem: There exist three numbers $a$, $b$ and $c$, not all the same, such that $a^2 + b^2 = c^2$",
        "Lagrange's Theorem: If $H$ is a subgroup of a finite group $G$, then the order of $H$ divides the order of $G$",
        "Trivial Theorem of Arithmetic: Most positive integers are very, very, very large.",
        "Cayley-Hamilton Theorem: Every square matrix over a commutative ring (such as the real or complex numbers or the integers) satisfies its own characteristic equation.",
        "Thales' Theorem: If $A$, $B$, and $C$ are distinct points on a circle where the line $AC$ is a diameter, then $\\angle ABC$ is a right angle",
        "The Fundamental Theorem of Algebra: Every non-zero, single-variable, degree $n$ polynomial with complex coefficients has, counted with multiplicity, exactly $n$ complex roots.",
        "Banach Fixed Point Theorem: Let $(X, d)$ be a non-empty complete metric space with a contraction mapping $T : X \\rightarrow X$ . Then $T$ admits a unique fixed-point $x^*$ in $X$ (i.e. $T(x^*) = x^*$ ) .",
        "Fermat's Last Theorem: No three positive integers $a$, $b$, and $c$ satisfy the equation $a^n + b^n = c^n$ for any integer value of $n \\ge 3$",
        "Noether's Theorem: Every continuous symmetry of the action of a physical system with conservative forces has a corresponding conservation law",
        "Poincaré–Bendixson Theorem: Given a differentiable real dynamical system defined on an open subset of the plane, every non-empty compact ω-limit set of an orbit, which contains only finitely many fixed points, is either a fixed point, a periodic orbit, or a connected set composed of a finite number of fixed points together with homoclinic and heteroclinic orbits connecting these.",
        "Taylor's Theorem in Several Dimensions: A function $f: R^n \\to R$ is differentiable at $a \\in R^n$ if and only if there exists a linear functional $L: R^n \\to R$ and a function $h: R^n \\to R$ such that $f(x) = f(a) + L(x - a) + h(x)||x-a||, \\lim_{{x \\to a}}h(x) = 0$.",
        "Sharkovskii's Theorem: If $f$ is a discrete dynamical system on the real line and has a periodic point of period 2 and has a point of period 3, then there exist points of all periods, including chaotic orbits.",
        "Four Colour Theorem: No more than four colors are required to colour the regions of any map so that no two adjacent regions have the same colour.",
        "Jordan–Hölder Theorem: Any two composition series of a given group are equivalent",
        "Intermediate Value Theorem: If $f: R \\to R$ is a continuous function whose domain contains the interval $[a, b]$ and $s$ is a number such that $f(a) < s < f (b)$, then there exists some $x$ between $a$ and $b$ such that $f(x) = s$",
        "Spectral Theorem: If A is Hermitian on V, then there exists an orthonormal basis of V consisting of eigenvectors of A. Each eigenvalue of A is real.",
        "Arrow's Impossibility Theorem: No ranked-choice procedure for group decision-making can satisfy the requirements of rational choice.",
        "Abel-Ruffini Theorem: There is no solution in radicals to general polynomial equations of degree five or higher with arbitrary coefficients."
        # "Picard–Lindelöf Theorem: Let $D \\subseteq \\mathbb {{R}} \\times \\mathbb {{R}} ^{{n}}$, and $(t_0,y_0) \\in \\operatorname {{ int }}$. Let $f:D \\to \\mathbb{{R}}^n$ be a function that is continuous in $t$ and Lipschitz continuous in $y$ with the Lipschitz constant independent of $t$. Then there exists some $\\varepsilon > 0$ such that the initial value problem $y'(t)=f(t,y(t)), y(t_0)=y_0}$ has a unique solution $y(t)$ on the interval $[t_0-\\varepsilon ,t_0+\\varepsilon] $.",
    ]

    return choice(theorems)
