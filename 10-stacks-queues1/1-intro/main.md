# Introduction to Stacks and Queues

## Introduction
Stacks and queues are fundamental linear data structures used to store and manage collections of elements in specific orders.

## Details
- **Stack:** Last-In-First-Out (LIFO) structure, elements added and removed from the top.  
- **Queue:** First-In-First-Out (FIFO) structure, elements added at rear and removed from front.

Stacks are used in expression evaluation and backtracking; queues in buffering and scheduling. They are like a stack of plates where adding or removal is done from the top. They formally support the push and pop operations as well as accessor methods including `top() is_empty() and len()`.

A common example of use of a stack is the web browser that store addresses of recently visited sites such that the user can pop out from existing page to previous one.

Another example is the undo button of a text editor that keeps editing changes in a stack and allows user to revert to the previous ones

Stacks being abstract data types(ADT) are the simplest as well as the most important of all data structures

A queue is collection of objects that are inserted or removed according to first-in, first-out(FIFO) principle. It is a fundamental data structure. A functional or real world example is people waiting at a train station to get tickets for their trips. It can be called first-come, first-serve.
We see queues in real life at gas stations, counters, reservation centers, stores, theatres.

Queue abstract data type (ADT) supports enqueue and dequeue operations. Enqueue adds element to the back of the queue while dequeue removes the first element at the front and returns first element.

Other methods are `first(), is_empty(), len(Q)`.

## Examples
Stack usage: Undo functionality.  
Queue usage: Printer jobs scheduling.

## Key Concepts
- Different rules for element insertion and removal.  
- Both support dynamic sizes.  
- Implementable via arrays or linked lists.

## Summary
Stacks and queues provide structured ways to manage data flow and support various algorithms.
