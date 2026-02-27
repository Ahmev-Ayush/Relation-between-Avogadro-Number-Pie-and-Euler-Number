# Avogadro's Number: A Novel Relation with π, e, and an Integer

## Author
**Ahmev-Ayush**
Date of Discovery: 24-02-2026
Published: 26-02-2026


## The Relation

This repository documents a mathematical coincidence (or deeper relation)
connecting Avogadro's number ($N_A$) with fundamental mathematical constants:

$$
\frac{N_A}{10^{23}} = \frac{A_{\text{int}}^a}{\pi^b \cdot e^c} 
$$

Where:
| Symbol | Value | Description              |
|--------|-------|--------------------------|
| $N_A$  | 6.02213210 × 10²³ mol⁻¹ | Avogadro's number (computed via this relation) |
| $N_A$  | 6.02214076 × 10²³ mol⁻¹ | Avogadro's number (2019 SI exact) |
| $A_{\text{int}}$ | 380   | **Ahmev's Integer** — the key integer in this relation |
| $a$    | 1   | Integer exponent |
| $b$    | 1   | Integer exponent of π = 3.14159... |
| $c$    | 3   | Integer exponent of e (euler's number = 2.71828...) |

Substituting these values:

$$
\frac{N_A}{10^{23}}  = \frac{380}{\pi \cdot e^3}
$$



## Numerical Verification

The relation is accurate to **4 decimal places**, yielding a value of $N_A \approx 6.02213210 \times 10^{23} \text{ mol}^{-1}$. This represents an **Absolute error** of $\approx 8.66 \times 10^{-6}$ compared to the exact 2019 SI value ($6.02214076 \times 10^{23}$). See [`proofs/numerical_verification.py`](https://github.com/Ahmev-Ayush/Relation-between-Avogadro-Number-Pie-and-Euler-Number/blob/main/proofs_numerical_verification.py) for full-precision verification.



## Interesting Fact: Higher Accuracy with a Correction Term

If a small correction term $\delta$ is added to the right-hand side of the relation:

$$
\frac{N_A}{10^{23}} = \frac{380}{\pi \cdot e^3} + \delta, \quad \text{where } \delta = \frac{5\sqrt{3}}{10^{6}}
$$

then $N_A$ achieves **8 decimal place accuracy**, matching the 2019 SI exact value $6.02214076 \times 10^{23} \text{ mol}^{-1}$.

## Story of Discovery

Curious about how this relation was found? Read [DISCOVERY.md](DISCOVERY.md) for the full story behind the discovery — the thought process, the steps, and the moment the pattern emerged.


## License

This work is licensed under [CC BY 4.0](LICENSE.txt).
You are free to share and adapt, but **must give appropriate credit**.

## How to Cite (Not available right now)

If you reference this finding, please cite using the
[CITATION.cff](CITATION.cff) file in this repository.

## Disclaimer

This is presented as a mathematical observation/coincidence. Whether it
reflects a deeper physical or mathematical truth is an open question.