"""
Numerical Verification of the Avogadro Relation
Author: Ahmev-Ayush
Date: 2026-02-26

Relation: N_A / 10^23 = 380 / (pi * e^3)
"""

from mpmath import mp, mpf, pi, e, log10, fabs

# Set precision to 100 decimal places
mp.dps = 100

# ==== PARAMETERS ====
k = mpf('380')  # Integer discovered in this work
a = 1           # Integer exponent of k
b = 1           # Integer exponent of pi
c = 3           # Integer exponent of e

# ==== ACCEPTED VALUE ====
# As of 2019 SI redefinition, Avogadro's number is EXACTLY:
N_A_exact = mpf('6.02214076e23')

# ==== COMPUTED VALUE ====
N_A_computed = (k**a / (pi**b * e**c)) * mpf('1e23')

# ==== ERROR ANALYSIS ====
absolute_error = fabs(N_A_exact - N_A_computed)
relative_error = absolute_error / N_A_exact

print("=" * 60)
print("AVOGADRO RELATION — NUMERICAL VERIFICATION")
print("=" * 60)
print(f"N_A (exact, SI 2019) : {mp.nstr(N_A_exact, 9, strip_zeros=False)}")
print(f"N_A (computed)       : {mp.nstr(N_A_computed, 9, strip_zeros=False)}")
print(f"Absolute error       : {mp.nstr(absolute_error, 9, strip_zeros=False)}")
print(f"Relative error       : {mp.nstr(relative_error, 9, strip_zeros=False)}")

if relative_error != 0:
    matching_digits = -int(log10(relative_error))
    print(f"Matching sig. digits : ~{matching_digits}")
else:
    print("Matching sig. digits : EXACT (within precision)")
print("=" * 60)