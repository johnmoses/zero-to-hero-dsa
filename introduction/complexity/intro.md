# Algorithm Complexity

## Three different types of complexity

Big O (Big O): A complexity that is going to be less than or equal to the worst time a program can take.

Big Ω (Omega): It is a complexity that is going to be at least more than the best case.

Big θ (Theta): It is a complexity that is within the bound of the worst and the best case.

## Time complexity

Time complexity measures the amount of time an algorithm takes to complete as a function of the input size. It’s a way to estimate the running time of an algorithm. The common ones are shown below.

- O(1): Constant time. The running time doesn’t change with the input size. Example: Accessing an array element by index.

- O(log n): Logarithmic time. The running time increases logarithmically as the input size increases. Example: Binary search in a sorted array.

- O(n): Linear time. The running time increases linearly with the input size. Example: Iterating through an array.

- O(n log n): Log-linear time. Common in efficient sorting algorithms like mergesort and quicksort.

- O(n²): Quadratic time. The running time grows quadratically with the input size. Example: Nested loops, such as in bubble sort.

- O(2^n): Exponential time. The running time doubles with each additional input element. Example: Recursive algorithms solving the Towers of Hanoi.

- O(n!): Factorial time. The running time grows factorially with the input size. Example: Brute-force solutions to the traveling salesman problem.

## Scenarios

Best Case: The scenario where the algorithm performs the minimum number of steps.

Worst Case: The scenario where the algorithm performs the maximum number of steps.

Average Case: The expected scenario, considering all possible inputs.

## Space complexity

Space complexity measures the amount of memory an algorithm uses as a function of the input size.

Big O Notation for Space Complexity: Just like time complexity, space complexity can be expressed in Big O notation.

- O(1): Constant space. The algorithm uses a fixed amount of memory regardless of input size. Example: Variables storing sums or counters.

- O(n): Linear space. The memory usage grows linearly with the input size. Example: Storing an additional array or list.

- O(n²): Quadratic space. The memory usage grows quadratically with the input size. Example: Storing a 2D matrix.

## Extra space

- Auxiliary Space: The extra space or temporary space used by an algorithm.

- In-place Algorithm: An algorithm that uses a constant amount of extra space, typically O(1).

## Average time complexity of different data structures

Data                structure Access  Search Insertion Deletion
Array               O(1)      O(N)     O(N)     O(N)
Singly Linked list  O(N)      O(N)     O(1)     O(1)
Doubly Linked List  O(N)      O(N)     O(1)     O(1)
Stack               O(N)      O(N)     O(1)     O(1)
Queue               O(N)      O(N)     O(1)     O(1)
Hash Table          O(1)      O(1)     O(1)     O(1)
Binary Search Tree  O(log N)  O(log N) O(log N) O(log N)
AVL Tree            O(log N)  O(log N) O(log N) O(log N)
B Tree              O(log N)  O(log N) O(log N) O(log N)
Red Black Tree      O(log N)  O(log N) O(log N) O(log N)

## Categories by runtime

Logarithmic: O(log n) Binary Search

Linear: O(n) Linear Search

Superlinear: O(n log n) Heap Sort, Merge Sort

Polynomial: O(n^c) Strassen’s Matrix Multiplication, Bubble Sort, Selection Sort, Insertion Sort, Bucket Sort

Exponential: O(c^n) Tower of Hanoi

Factorial: O(n!) Determinant Expansion by Minors, Brute force Search algorithm for Traveling Salesman Problem
