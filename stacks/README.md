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
