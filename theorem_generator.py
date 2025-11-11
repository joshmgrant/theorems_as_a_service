from random import choice


def random_theorem() -> str:
    theorems = [
        # "Pythagorean Theorem: There exist three numbers $a$, $b$ and $c$, not all the same, such that $a^2 + b^2 = c^2$",
        # "Lagrange's Theorem: If $H$ is a subgroup of a finite group $G$, then the order of $H$ divides the order of $G$",
        # "Trivial Theorem of Arithmetic: Most positive integers are very, very, very large.",
        # "Cayley-Hamilton Theorem: Every square matrix over a commutative ring (such as the real or complex numbers or the integers) satisfies its own characteristic equation.",
        # "Thales' Theorem: If $A$, $B$, and $C$ are distinct points on a circle where the line $AC$ is a diameter, then $\\angle ABC$ is a right angle",
        # "The Fundamental Theorem of Algebra: Every non-zero, single-variable, degree $n$ polynomial with complex coefficients has, counted with multiplicity, exactly $n$ complex roots.",
        # "Banach Fixed Point Theorem: Let $(X, d)$ be a non-empty complete metric space with a contraction mapping $T : X \\rightarrow X$ . Then $T$ admits a unique fixed-point $x^*$ in $X$ (i.e. $T(x^*) = x^*$ ) .",
        # "Fermat's Last Theorem: No three positive integers $a$, $b$, and $c$ satisfy the equation $a^n + b^n = c^n$ for any integer value of $n \\ge 3$",
        # "Noether's Theorem: Every continuous symmetry of the action of a physical system with conservative forces has a corresponding conservation law",
        # "Poincaré–Bendixson Theorem: Given a differentiable real dynamical system defined on an open subset of the plane, every non-empty compact ω-limit set of an orbit, which contains only finitely many fixed points, is either a fixed point, a periodic orbit, or a connected set composed of a finite number of fixed points together with homoclinic and heteroclinic orbits connecting these.",
        "Taylor's Theorem in Several Dimensions: A function $f: R^n \\to R$ is differentiable at $a \\in R^n$ if and only if there exists a linear functional $L: R^n \\to R$ and a function $h: R^n \\to R$ such that $f(x) = f(a) + L(x - a) + h(x)||x-a||, \\lim_{{x \\to a}}h(x) = 0$."
        # "Picard–Lindelöf Theorem: Let $D \\subseteq \\mathbb {{R}} \\times \\mathbb {{R}} ^{{n}}$, and $(t_0,y_0) \\in \\operatorname {{ int }}$. Let $f:D \\to \\mathbb{{R}}^n$ be a function that is continuous in $t$ and Lipschitz continuous in $y$ with the Lipschitz constant independent of $t$. Then there exists some $\\varepsilon > 0$ such that the initial value problem $y'(t)=f(t,y(t)), y(t_0)=y_0}$ has a unique solution $y(t)$ on the interval $[t_0-\\varepsilon ,t_0+\\varepsilon] $.",
    ]

    return choice(theorems)