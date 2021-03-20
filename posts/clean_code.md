# Clean Code
TIMESTAMP: 1614269925

## Lesson 1
Source: [Clean Code - Uncle Bob / Lesson 1](https://www.youtube.com/watch?v=7EmboKQH8lM)

- Opinions on clean code
  - Clean code does one thing well
  - Clean code reads like well-written prose
  - Clean code looks like it was written by someone who cares
  - Each routine does what you expected
- Example of code refactoring: 40:00 to 52:30
- How to write functons that do one thing
  - Extract code from functions until they cannot be further extracted
  - Move the functions into appropriately named classes, packages, modules, files
- A function can be thought of as a class
  - It contains a set of "functions" (i.e. units of code) that manipulate a set of variables
- Guidelines
  - Keep functions short
  - Keep level of indentation minimal
  - Kepp list of parameters minimal
  - Almost never pass booleans into functions, just write two functions
  - Don't use output parameters
  - Avoid switch statements
    - Use inheritance and polymorphism
    - Follow open/closed principle: open for extension, closed for modification
    - Switch statements create depenencies
  - Avoid side-effects
    - Lambdas for managing pairs of functions (e.g. open, close)
  - Command and query separation
    - If it returns void, it must have side-effects
    - So, if it returns a value, don't modify the system
    - This separates commands from queries
  - Use exceptions, keep the code minimal
  - DRY

## Lesson 2
Source: [Clean Code - Uncle Bob / Lesson 2](https://www.youtube.com/watch?v=2a_ytyt9sf8)

- Comments are not a pure good
- Express yourself in code if possible
- Comment as a last resort
- Comments degrade over time
- Comments are often highlighted in washed out colors
- TODO comments: complete or delete before checking in
- Don't check in commented out code
- Don't put comments on code that exists elsewhere
- Statistics
  - Files average around 50 to 100 lines
  - Line length average around 30 to 40 characters
- Identifier lengths
  - The length of a variable name should be proportional to the scope that contains it
  - The length of a function name should be _inversely_ proportional to the scope
  - Names of classes follow the same rule as functions
- Prefer pair programming over code reviews

## Lesson 3
Source: [Clean Code - Uncle Bob / Lesson 3](https://www.youtube.com/watch?v=Qjywrq2gM8o)

- Doubling rate of programmers is about 5 years
  - At any given time, half of programmers have less than 5 years of experience
- Only ship quality code

## Lesson 4
Source: [Clean Code - Uncle Bob / Lesson 4](https://www.youtube.com/watch?v=58jGpV2Cg50)

## Lesson 5
Source: [Clean Code - Uncle Bob / Lesson 5](https://www.youtube.com/watch?v=sn0aFEMVTpA)

## Lesson 6
Source: [Clean Code - Uncle Bob / Lesson 6](https://www.youtube.com/watch?v=l-gF0vDhJVI)
