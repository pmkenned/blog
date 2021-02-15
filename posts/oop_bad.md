# Object-Oriented Programming is Bad
TIMESTAMP: 1613014289

## Clarifying the claims being made

- Things that are not the problem
  - classes: can be useful
  - performance: high-performance isn't needed everywhere
  - abstraction: OOP does tend to produce abstractions that aren't any good, but the problem is not with abstraction as such
  - aesthetics: OOP makes this worse, but aesthetics do matter
- Competing paradigms
  - procedural & imperative
    - the default, obvious way to do things
    - shared state can become difficult to manage
  - procedural & functional
    - minimize state
  - object-oriented & imperative
    - segregate state
  - object-oriented & functional
    - do both
    - may be the ideal way to organize high-level code
 - What is the target of the criticism
   - inheritance isn't the target of the criticism
     - nobody defends it anymore
   - polymorphism isn't the target either
     - it's not exclusive to OOP anyway
   - **encapsulation is the target**
     - it doesn't work at a fine-grained level

## Why does OOP dominate?

- imposition of management?
  - plausible, but unlikely
- Java
  - simpler than Win32 API, cross-platform, less cryptic
  - familiar: curly braces, C-style
  - namespaces: appealing over no header files
  - garbage collection: appealing to not manage memory
  - exceptions: appealing over return error codes
  - subject.verb(object) is intuitive grammar
  - GUIs seems object-oriented by nature
- appeal of OOP
  - Java maybe could have been procedural and still been successful
  - so the question remains: why does OOP dominate?
  - what is a unit of code abstraction bigger than a function and a data type? a combination
  - OOP seemed to present a unit of abstractions and set of guidelines for larger systems

## What does OOP not work?

- an OOP program can be thought of as a graph of objects communicating via messages
- messages send copies of state (not references)
  - objects are, themselves, state, so messages cannot pass object references
  - thus, for an object to send a message to another object, it must hold a private reference to it
  - if an object, A, is sending messages to object B, B must be part part of A's private state
- if multiple objects could send messages to the same object, then we have the problem of shared state
  - yes, the state of the object is "encapsulated", but that's a very weak form of encapsulation
- to take encapsulation seriously, we would need a strict hierarchy of objects
  - to deal with cross-cutting concerns, messages must be passed up and down the hierarchy
  - nobody writes programs this way
- what about half-assed encapsulation?
  - what often happens is that new requirements come up, and then you have to either create extra classes to handle the cross-cutting concerns, or you break the rule of encapsulation and have objects communicate directly
  - if you follow the rules strictly, most things you do end up being very indirect with lots of extra highly-abstract classes to manage things
  - if you follow the rules loosely, what is the point?
- in practice, OOP tends to be like creating a floorplan before the requirements are understood
  - better to start with an absence of structure, rather than impose a structure that doesn't fit the problem and inhibits change
- in procedural code, we can think about how code and data are structured independently
  - in procedural, for code there is just the call graph, not an inheritance graph, composition graph, etc.
  - in OOP, we have to associate all our behaviors with data types and create additional data types to be containers for certain behaviors that don't naturally fit
- Kingdom of Nouns: we get a bunch of "Service", "Managers", "X-ers" and need to ask a bunch of nebulous questions
- OOP tends to make code hard to read
  - things named "X" often don't contain the code for doing what the name would suggest
  - it tends to spread what could be self-contained code and split it up into many separate classes and files
  - if we divide up our code into tiny pieces, are we decreasing the complexity, or just spreading it around and increasing the surface area in the process?

## How should we write code without OOP?

- you can still use classes where appropriate (e.g. abstract data types)
  - when you start asking whether a certain behavior really has a primary association with a certain data type, just make it a plain function
- what about shared state?
  - when in doubt, paramerterize over using globals
  - bundle globals into structs
  - favor pure functions where possible
  - encapsulate (loosely) at the level of namespaces/packages/modules
    - much easier to deal with cross-cutting concerns when there are only a few modules
  - don't be afraid of long functions
    - chopping functions up has cost
    - can also use private functions or self-calling anonymous functions

## Summary

- OOP is bad because encapsulation at a fine-grained level doesn't deliver on its promises
  - cross-cutting concerns, which make up a large portion of what interesting programs do, require either breaking the rule and having objects interact via private preferences to each other which creates an increasingly tangled mess, or having an increasingly difficult to maintain hierarchy of objects with lots of overhead and boilerplate code for communicating across the hierarchy to deal with cross-cutting concerns
  - lots of data types of an excessively abstract nature are introduced to deal with this problem, worsening code readability and maintainability
  - it is better to avoid imposing structure prematurely than to impose a structure that will be hard to change later
- procedural programming should be used instead, using functional programming where possible and with encapsulation used at a course-grained level
