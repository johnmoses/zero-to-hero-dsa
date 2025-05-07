# Monotonic Stack

The word "monotonic" means a list or a function is either always increasing, or always decreasing.

It is like a regular stack with one key distinction in the push operation: Before we push a new element onto the stack, we first check if adding it breaks the monotonic condition. If it does, then we pop the top element off the stack until pushing the new element no longer breaks the monotonic condition.

Monotonic stacks are generally used for solving questions of the type - next greater element, next smaller element, previous greater element and previous smaller element. We are going to create a template for each of the format, and then use them to solve variety of problems.

Types of monotonic stack

- Strictly increasing - every element of the stack is strictly greater than the previous element. Example - [1, 4, 5, 8, 9]
- Non-decreasing - every element of the stack is greater than or equal to the previous element. Example - [1, 4, 5, 5, 8, 9, 9]
- Strictly decreasing - every element of the stack is strictly smaller than the previous element - [9, 8, 5, 4, 1]
- Non-increasing - every element of the stack is smaller than or equal to the previous element. - [9, 9, 8, 5, 5, 4, 1]
