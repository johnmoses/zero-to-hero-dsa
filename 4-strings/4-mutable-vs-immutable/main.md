# Mutable vs Immutable Strings

## Introduction
Strings can be mutable or immutable depending on the programming language. This affects how strings can be modified after creation.

## Details
- **Immutable strings:** Once created, their content cannot be changed. Operations that seem to modify a string actually create a new one. Examples: Python, Java.
- **Mutable strings:** Can be changed in place without creating new objects. Examples: C++ std::string.

Choosing mutable or immutable strings influences performance and memory usage.

## Examples
In Python, modifying a string creates a new string. In C++, you can modify characters directly.

## Key Concepts
- Immutable strings offer safety and simplicity.  
- Mutable strings provide flexibility and efficiency for many changes.  
- Understand your language’s string behavior to write optimal code.

## Summary
Knowing string mutability helps predict how string operations behave under the hood and guides efficient programming.
