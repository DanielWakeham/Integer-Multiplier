# This program implements the Groebner Basis Rewrite algorithm found in:
#
# “Formal verification of integer multipliers by combining grobner basiswith logic reduction”,
# 2016 Design, Automation Test in EuropeConference Exhibition (DATE)
#
# Algorithm 1 Grobner Basis Rewriting (GB-Rew)
#
# Input: Variables V, Circuit Model G notes: V is 
# Output: Model G_n rewritten wrt V
#  1. for g_i (belongs to) G do /* in reverse order of leading monomials */
#  2.    lv <- lm(g_i)
#  3.    r <- g_i - lv
#  4.    while Vars(r) (not set of) V do
#  5.        Choose v_t (belongs to) Vars(r)
#  6.        Choose g_t (belongs to) G st lm(g_t) = v_t
#  7.        r <- Spoly(r, g_t)
#  8.        r <- XOR-AND-Rule(r)
#  9.    end while
# 10.   g_i <- r + lv
# 11. end for
# 12. G_n <- UpdateModel(G, V) /* remove polynomials whoose leading terms are not in V */
# 13. return G_n
#
# Algorithm 2 Logic Reduction Rewriting
#
# Input: Specification Polynomial p_spec, Circuit Model G
# Output: Circuit Model G
# 1. V <- XORRewritingVariables(G)
# 2. G <- GB-Rew(V, G)
# 3. V <- CommonRewritingVariables(G)
# 4. G <- GB-Rew(V, G)
# 5. return G