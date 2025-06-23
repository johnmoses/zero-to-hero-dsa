# Stacks

A stack is a collection of objects that are inserted or removed according to last-in, first-out(LIFO) principle. They are like a stack of plates where adding or removal is done from the top. They formally support the push and pop operations as well as accessor methods including `top() is_empty() and len()`.

A common example of use of a stack is the web browser that store addresses of recently visited sites such that the user can pop out from existing page to previous one.

Another example is the undo button of a text editor that keeps editing changes in a stack and allows user to revert to the previous ones

Stacks being abstract data types(ADT) are the simplest as well as the most important of all data structures

There are many ways of creating stacks, we will look at a few of them

## Array Stack

This is an array-based stack implementation.

## Queue Stack

This is a `deque()` implementation of a stack

## Linked List Stack

The linked list has two methods addHead(item) and removeHead() that run in constant time and are very good in implementing stacks

## Monotonic Stack

The word "monotonic" means a list or a function is either always increasing, or always decreasing.

It is like a regular stack with one key distinction in the push operation: Before we push a new element onto the stack, we first check if adding it breaks the monotonic condition. If it does, then we pop the top element off the stack until pushing the new element no longer breaks the monotonic condition.

## Problems

- Valid Parenthesis (Leetcode #20 Grind)
- Largest Rectangle in Histogram (Leetcode #84, Grind)
- Reverse String (Leetcode #344)
- Next Greater Element I (Leetcode #496)

- Evaluate Reverse Polish Notation (Leetcode #150)
- Min Stack (Leetcode #155)
- Daily Temperatures (Leetcode #739)
