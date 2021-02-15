# C Interfaces and Implementations
TIMESTAMP: 1611024742

## Preface

- `anonymous@ftp.cs.princeton.edu:/pub/packages/cii`

## Introduction

### Literate Programs

### Programming Style

### Effiency

### Further Reading

- The Standard C Library
- C: A Reference Manual
- The Dictionary of Standard C
- The UNIX Programming Environment
- etc.

## Interfaces and Implementations

### Interfaces

### Implementations

### Abstract Data Types

- `#define T Stack_T;`, `#undef T`
- `Stack_free` takes a `T *` so it can set the pointer to NULL

### Client Responsibilities

- Unchecked runtime errors, checked runtime errors, exceptions
- `struct elem` inside `struct T`
- No way to guarantee the parameters are valid `Stack_T`s
- Why `const T` doesn't work

### Efficiency

## Atoms

### Interface

### Implementation

- Converting `int` to string
- `NELEMS`
- `ALLOC` vs `NEW`

## Exceptions and Assertions

### Interface

### Implementation

### Assertions

## Memory Management

### Interface

### Production Implementation

### Checking Implementation

## More Memory Management

### Interface

### Implementation

## Lists

### Interface

### Implementation

## Tables

### Interface

### Example: Word Frequencies

### Implementation

## Sets

### Interface

### Example: Cross-Reference Listing

### Implementation

## Dynamic Arrays

### Interface

### Implementation

## Sequences

### Interface

### Implementation

## Rings

### Interface

### Implementation

## Bit Vectors

### Interface

### Implementation

## Formatting

### Interface

### Implementation

## Low-Level Strings

### Interface

### Example: Printing Identifiers

### Implementation

## High-Level Strings

### Interface

### Implementation

## Extended-Precision Arithmetic

### Interface

### Implementation

## Arbitrary-Precision Arithmetic

### Interface

### Example: A Calculator

### Implementation

## Multiple-Precision Arithmetic

### Interface

### Example: Another Calculator

### Implementation

## Threads

### Interfaces

### Examples

### Implementations

