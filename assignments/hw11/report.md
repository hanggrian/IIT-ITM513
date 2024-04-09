# Learning report

## Summary

Python is a multi-paradigm language supporting procedural and Object-Oriented
Programming (OOP), which is the focus of this assignment. To apply the OOP
design, I studied features such as built-in annotated functions, the abstraction
helper class and function docstring inheritance.

I then created a `Store` class with abstract methods as instructed. It acts as a
foundation for `Restaurant` and `GroceryStore`, ensuring both have shared
attributes inherited from the superclass, for example, name and sales tax.
`Restaurant` has extra attributes for dining-specific functionality like
occupancy, and can be operated with staged calls with checking in, serving, and
checking out. `Grocery` is much more straightforward with one main function to
sell products given quantity and pricing.

Having implemented all the necessary logic including the abstract methods, I
enhanced them further with checks and hints preventing improper input. Finally,
the subclasses are utilized in `shopping.py` and respective test classes.

## Question 1

> Did you successfully get your assignment done? Did it run? Any error? Did you
  get the correct result? Did you test your program thoroughly?

I have successfully finished the assignment with no known errors. There are also
unit tests that inspect core functionality, albeit with a limited dataset.

## Question 2

> How much time did you spend to complete your assignment?

Completing the assignment took two hours. I then needed several more hours to
draw the class diagram and write this report, totaling almost a full day of
work.

## Question 3

> Did you find the assignment easy or challenging for you?

This assignment is easier because OOP is a common concept and likely this
course's prerequisite. In contrast, previous homework regarding data analysis is
particularly challenging due to less exposure.

## Question 4

> Did you write the program yourself? Did you get any help from anyone?

I work alone in creating the source code, unit tests and diagram graphics.

## Question 5

> When you encountered obstacles to complete your program, how did you resolve
  the issues? Did you use Google to get help? Describe how Google was abled or
  not able to assist you?

To solve an issue I encounter during development, I strive to understand the
underlying problem by collecting relevant information before jumping straight to
online resources such as GitHub and StackOverflow. For example, we could log the
application state to pinpoint which conditions trigger the misbehavior.

## Question 6

> What did you learn from doing this assignment?

As mentioned in the summary, I learned about Python's built-in annotated
functions to provide the OOP paradigm such as property getter, setter and
declaring static method.

## Question 7

> Any other information you would like to share with your instructor? Make sure
  you provide program output on each option.

Although Python natively supports object-oriented design, encapsulation can feel
less intuitive than pure OOP languages. For one, there is no interface in Python
to define abstract-only objects. Moreover, some advanced features also require
external dependencies, for instance, `typing` and `abc`.

Nevertheless, this perspective is not a criticism of Python. I am confident the
developers of Python have their reason and it will all make sense when I am more
experienced with the language.
