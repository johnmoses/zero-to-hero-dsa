# Master Theorem

## Introduction

The Master Theorem provides a straightforward way to determine the time complexity of divide and conquer algorithms that follow a specific recurrence form. It simplifies solving recurrences common to many recursive algorithms.

## Details

The Master Theorem applies to recurrences of the form:

\[
T(n) = aT\left(\frac{n}{b}\right) + f(n)
\]

where:

- \(a \geq 1\) is the number of subproblems,
- \(b > 1\) is the factor by which the problem size is divided,
- \(f(n)\) represents the cost outside the recursive calls.

The theorem classifies the solution based on comparison between \(f(n)\) and \(n^{\log_b a}\):

1. If \(f(n) = O\left(n^{\log_b a - \epsilon}\right)\) for some \(\epsilon > 0\), then \(T(n) = \Theta\left(n^{\log_b a}\right)\).
2. If \(f(n) = \Theta\left(n^{\log_b a} \log^k n\right)\) for some \(k \geq 0\), then \(T(n) = \Theta\left(n^{\log_b a} \log^{k+1} n\right)\).
3. If \(f(n) = \Omega\left(n^{\log_b a + \epsilon}\right)\) for some \(\epsilon > 0\), and if \(af\left(\frac{n}{b}\right) \leq cf(n)\) for some \(c < 1\), then \(T(n) = \Theta(f(n))\).

## Examples

- **Merge Sort:** \(T(n) = 2T(n/2) + O(n)\), case 2, complexity \(O(n \log n)\).
- **Binary Search:** \(T(n) = T(n/2) + O(1)\), case 1, complexity \(O(\log n)\).
- **Strassen's Matrix Multiplication:** \(T(n) = 7T(n/2) + O(n^2)\), complexity approximately \(O(n^{2.81})\).

## Key Concepts

- Analyzing recursive time complexities easily.
- Determining dominant terms based on growth rates.
- Applying to a wide class of divide and conquer algorithms.

## Summary

The Master Theorem is a powerful tool to analyze the complexity of divide and conquer algorithms, allowing quick determination of asymptotic behavior from the recurrence relation.
