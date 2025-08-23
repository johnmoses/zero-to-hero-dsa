# Monotonic Stack Applications

## Introduction

Monotonic stacks are specialized stack data structures used to solve problems that require finding the next or previous smaller or larger element efficiently. They maintain their elements in sorted order, either increasing or decreasing.

## Details

A monotonic stack can be either:

- **Increasing Monotonic Stack:** Elements strictly increase from the bottom to the top.
- **Decreasing Monotonic Stack:** Elements strictly decrease from the bottom to the top.

This data structure allows fast, linear-time solutions to problems involving nearest smaller/larger elements, histogram maximum area, and others.

Common use cases include:

- Finding the Next Greater Element.
- Largest Rectangle in Histogram.
- Stock Span problems.

## Examples

Classic problems solved with monotonic stacks:

- Nearest smaller element to the left/right.
- Largest rectangle in a histogram.
- Rainwater trapping problems.

Monotonic stacks reduce brute-force quadratic approaches to efficient linear-time solutions.

## Key Concepts

- Stack operations preserving monotonicity.
- Pushing and popping based on comparisons.
- Using stacks to maintain candidate elements for queries.
- Application to both array indexes and values.

## Summary

Monotonic stacks provide an elegant and efficient approach to a class of problems involving order relations in sequences. They are essential tools in competitive programming and algorithm design for linear time complexity optimizations.
