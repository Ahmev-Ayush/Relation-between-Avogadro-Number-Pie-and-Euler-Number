"""
Numerical Verification of the Avogadro Relation
Author: Ahmev-Ayush
Date: 2026-02-26

Relation: N_A / 10^23 = 380 / (pi * e^3)  where 380 is Ahmev's Integer
"""

from mpmath import mp, mpf, pi, e, log10, fabs

# Set precision to 100 decimal places
mp.dps = 100

# ==== PARAMETERS ====
k = mpf('380')  # Ahmev's Integer
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

# ==== CORRECTED RELATION WITH DELTA TERM ====
# delta = 5 * sqrt(3) / 10^6
from mpmath import sqrt

delta = 5 * sqrt(mpf('3')) / mpf('1e6')
N_A_corrected = (k**a / (pi**b * e**c) + delta) * mpf('1e23')

absolute_error_corrected = fabs(N_A_exact - N_A_corrected)
relative_error_corrected = absolute_error_corrected / N_A_exact

print()
print("=" * 60)
print("CORRECTED RELATION — WITH DELTA TERM (5√3 / 10⁶)")
print("Relation: N_A / 10^23 = 380 / (pi * e^3) + 5*sqrt(3)/10^6")
print("=" * 60)
print(f"N_A (exact, SI 2019) : {mp.nstr(N_A_exact, 11, strip_zeros=False)}")
print(f"N_A (corrected)      : {mp.nstr(N_A_corrected, 11, strip_zeros=False)}")
print(f"delta value          : {mp.nstr(delta, 9, strip_zeros=False)}")
print(f"Absolute error       : {mp.nstr(absolute_error_corrected, 9, strip_zeros=False)}")
print(f"Relative error       : {mp.nstr(relative_error_corrected, 9, strip_zeros=False)}")

if relative_error_corrected != 0:
    matching_digits_corrected = -int(log10(relative_error_corrected))
    print(f"Matching sig. digits : ~{matching_digits_corrected}")
else:
    print("Matching sig. digits : EXACT (within precision)")
print("=" * 60)