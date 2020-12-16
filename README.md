# LSystem

## What is LSystem?
A pure python module for generating iterations from the L-System or Lindenmayer system. 
Please check the [Wikipedia page on L-system][https://en.wikipedia.org/wiki/L-system] for details.

The module gives you the `LSystem` class with the same structure as listed out on Wikipedia page (see the paragraph above). It gives you the following attributes:
* **variables** : A set of symbols that can be replaced
* **constants** : A set of symbols that won't be replaced
* **axiom**	: The initial state of the system.
* **rules**	: The rules for replacing variables with a combination of constants and variables.
* **system**	: A list of iterations that have been formed. The first member is, naturally, the axiom. The list can be expanded using the `iterate()` function member.



### 

## Invitation

### to review
The code has been checked for the examples in Wikipedia. You are invited to cross check the results. Please raise an issue in case of a discrepancy.

### to contribute
You are welcome to improve LSystem and suggest improvements.
